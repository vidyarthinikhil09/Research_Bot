from crewai.tools import tool
from ddgs import DDGS

class ResearchTools:

    @tool("Search Tool")
    def search_Internet(query: str) -> str:
        """Useful to search the internet for a specific topic."""
        print(f"Searching the internet for: {query}")
        try:
            results = DDGS().text(query, max_results=5, backend="auto")
            if not results:
                return "No results found."
            bodies = [r.get("body", "") for r in results]
            merge_text = "\n".join(bodies)  # cleaner merge
            return merge_text
        except Exception as e:
            return f"Search temporarily unavailable. Proceed using general knowledge."

# # Example usage
# Tools = ResearchTools()
# print(Tools.search_Internet.run("Tell me about the Gemini 2.5 model by Google Generative AI."))
