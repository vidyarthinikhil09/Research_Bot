from crewai import Task

# help(Task)


class ContentTasks:
    
    def plan_task(self, agent, topic):
        return Task(
            description=f"Create a detailed content outline for the topic: '{topic}'. include 3 main section headers.",
            expected_output="A st   ructured list of 3 section headers with brief descriptions for each.",
            agent=agent
        )

    def research_task(self, agent, topic):
        return Task(
            description=f"Based on the plan, research key facts for the topic '{topic}'. Use the Search Tool.",
            expected_output="A list of 3-5 key facts, statistics, or definitions found during research.",
            agent=agent
        )

    def write_task(self, agent, topic):
        return Task(
            description=f"Write a full blog post about '{topic}' using the Research Brief and the Outline.",
            expected_output="A 400-word blog post in Markdown format, with headers and bullet points.",
            agent=agent
        )

    def edit_task(self, agent):
        return Task(
            description="Review the blog post. Fix any awkward phrasing. Ensure it has a professional tone.",
            expected_output="The final, polished blog post ready for publishing.",
            agent=agent
        )