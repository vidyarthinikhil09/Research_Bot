import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai import Crew, Process
from Agents import ContentAgents
from Tasks import ContentTasks

# Silence logs (CRITICAL)
os.environ["CREWAI_VERBOSE"] = "false"
os.environ["LANGCHAIN_VERBOSE"] = "false"

def run_crew(topic: str) -> str:
    load_dotenv()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        temperature=0.3
    )

    agents = ContentAgents(llm)
    tasks = ContentTasks()

    planner = agents.planner_agent()
    researcher = agents.researcher_agent()
    writer = agents.writer_agent()
    editor = agents.editor_agent()

    task_plan = tasks.plan_task(planner, topic)
    task_research = tasks.research_task(researcher, topic)
    task_write = tasks.write_task(writer, topic)
    task_edit = tasks.edit_task(editor)

    crew = Crew(
        agents=[planner, researcher, writer, editor],
        tasks=[task_plan, task_research, task_write, task_edit],
        process=Process.sequential,
        verbose=False
    )

    result = crew.kickoff()
    return str(result)
