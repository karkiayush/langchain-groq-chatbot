# from fastapi import FastAPI
# from langserve import add_routes
#
# from app.agent.service import AgentService
# from app.tool.web_search import create_web_search_tool
# from app.llm.groq_client import get_groq_llm
# from app.util.logger import setup_logger
#
#
# def main():
#     setup_logger()
#
#     llm = get_groq_llm()
#     search_tool = create_web_search_tool()
#
#     agent = AgentService(llm=llm, tools=[search_tool])
#
#     print("\n===== Groq AI Agent =====")
#     print("Type 'exit' to quit.\n")
#
#     while True:
#         user_message = input("You: ").strip()
#
#         if user_message.lower() == "exit":
#             print("Goodbye 👋")
#             break
#
#         if not user_message:
#             continue
#
#         response = agent.generate_response(user_message=user_message)
#         print(f"Assistant: {response}\n")
#
#
# if __name__ == "__main__":
#     main()


from contextlib import asynccontextmanager

from fastapi import FastAPI
from langserve import add_routes

from app.agent.service import AgentService
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

    # Store shared service in application state
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


# Register custom REST API routes
app.include_router(router)


# Expose LangChain agent through LangServe
# This is an additional interface, separate from our custom REST API.
# See the LangServe explanation below.
