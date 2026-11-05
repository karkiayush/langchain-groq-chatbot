# for the langgraph.json, the agent should point to the langchain agent object created by AgentService, not to the Service class itself
# agent_service.agent ---- no

from app.llm.groq_client import get_groq_llm
from app.tool.web_search import create_web_search_tool
from app.agent.agent_service import AgentService

llm = get_groq_llm()
web_search_tool = create_web_search_tool()

agent_service = AgentService(
    llm=llm,
    tools=[web_search_tool],
)

# now exposing langchain agent object - for langgraph CLI
# This exposes your existing LangChain agent as a module-level variable that LangGraph CLI can import.
agent = agent_service.agent
