import chainlit as cl
import time
import asyncio
from main import run_crew

MAX_TOPIC_LEN = 80
COOLDOWN_SECONDS = 60

@cl.on_chat_start
async def start():
    cl.user_session.set("busy", False)
    cl.user_session.set("last_time", 0)

    await cl.Message(
        content="👋 **Welcome to Agentic Content Studio**\n\nEnter a topic to generate a professional blog post.",
        author="Assistant"
    ).send()

@cl.on_message
async def handle_message(message: cl.Message):
    topic = message.content.strip()

    # Guardrail 1
    if len(topic) > MAX_TOPIC_LEN:
        await cl.Message(
            content=f"❌ Topic too long (max {MAX_TOPIC_LEN} chars).",
            author="Assistant"
        ).send()
        return

    # Guardrail 2
    if cl.user_session.get("busy"):
        await cl.Message(
            content="⏳ Please wait, your request is processing.",
            author="Assistant"
        ).send()
        return

    # Guardrail 3
    now = time.time()
    if now - cl.user_session.get("last_time", 0) < COOLDOWN_SECONDS:
        await cl.Message(
            content="⏳ Please wait a minute before trying again.",
            author="Assistant"
        ).send()
        return

    cl.user_session.set("busy", True)
    cl.user_session.set("last_time", now)

    # 🔁 SINGLE status message
    status = cl.Message(
        content="🧠 Planner is creating the outline...",
        author="Assistant"
    )
    await status.send()

    try:
        # Run crew safely (no streaming)
        result = await asyncio.to_thread(run_crew, topic)

        # Update status once more
        status.content = "✅ Article ready"
        await status.update()

        # Final output
        await cl.Message(
            content=result,
            author="Assistant"
        ).send()

    except Exception:
        await cl.Message(
            content="⚠️ Service temporarily unavailable. Please try later.",
            author="Assistant"
        ).send()

    finally:
        cl.user_session.set("busy", False)
