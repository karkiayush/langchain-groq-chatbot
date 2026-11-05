from contextlib import asynccontextmanager

from fastapi import FastAPI
from langserve import add_routes

from app.agent.agent_service import AgentService
from app.tool.web_search import create_web_search_tool
from app.llm.groq_client import get_groq_llm
from app.api.route.agent_router import router
from app.util.logger import setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Application startup
    setup_logger()

    llm = get_groq_llm()
    search_tool = create_web_search_tool()

    agent_service = AgentService(
        llm=llm,
        tools=[search_tool],
    )

    # Store the initialized AgentService in application state.
    # app.state allows us to share application-level objects (e.g., services,
    # database connections, Redis clients) across different parts of the application.
    #
    # This avoids reinitializing the LLM, tools, and agent for every incoming request.
    # The same AgentService instance can be retrieved through request.app.state
    # and injected into route handlers using FastAPI's Depends().
    app.state.agent_service = agent_service

    yield

    # Application shutdown
    app.state.agent_service = None


app = FastAPI(
    title="GenAI Agent API",
    description="Groq LLM Agent with Google Serper Web Search",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(router)
