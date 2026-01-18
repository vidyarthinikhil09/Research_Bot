from textwrap import dedent
from crewai import Agent
from tools import ResearchTools


class ContentAgents:
    def __init__(self, llm):
        self.llm = llm

    def planner_agent(self):
        return Agent(
            role="Senior Content Strategist",
            goal="Plan a comprehensive, logical outline for the given topic.",
            backstory=dedent("""\
                You are a veteran Content Strategist at a top-tier tech publication.
                Your strength is seeing the 'Big Picture'. You despise fluff.
                You break complex topics into logical, linear sections."""),
            llm=self.llm,
            verbose=False,
            allow_delegation=False
        )

    def researcher_agent(self):
        return Agent(
            role="Tech Researcher",
            goal="Gather in-depth facts and statistics for the planned sections.",
            backstory=dedent("""\
                You are a meticulous researcher. You love digging into details.
                You don't write articles; you write 'Research Briefs' full of data.
                You have access to search tools."""),
            tools=[ResearchTools.search_Internet],
            llm=self.llm,
            verbose=False
        )

    def writer_agent(self):
        return Agent(
            role="Lead Technical Writer",
            goal="Convert research briefs into an engaging, polished article.",
            backstory=dedent("""\
                You are a gifted storyteller. You take dry facts and turn them into
                compelling narratives. You follow the structure provided by the Strategist
                and use the facts provided by the Researcher."""),
            llm=self.llm,
            verbose=False
        )

    def editor_agent(self):
        return Agent(
            role="Chief Editor",
            goal="Review the final piece for flow, tone, and accuracy.",
            backstory=dedent("""\
                You are the final gatekeeper. You ensure the content is professional,
                grammatically correct, and delivers value to the reader.
                You aggregate the final result into a clean Markdown format."""),
            llm=self.llm,
            verbose=False
        )
    
