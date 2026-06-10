from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot. TavilySearchResults is a library that is like a tool that allows us to search the web and get 
    results. We are using it here as an example of a tool that can be integrated into our chatbot graph.

    TavilySearchResults searches the live internet for real-time information. It scans blogs, news outlets, academic papers, and general websites to 
    find facts that occurred after an LLM's knowledge cutoff date
    """
    tools=[TavilySearchResults(max_results=2)] # Hands back the top 2 most relevant results from our live web search
    return tools

def create_tool_node(tools):
    """
    creates and returns a tool node for the graph
    """
    return ToolNode(tools=tools)


