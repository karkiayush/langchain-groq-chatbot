import logging

from langchain_groq import ChatGroq
from langchain.agents import create_agent

from app.agent.agent_prompt import SYSTEM_PROMPT
from app.util.constant import (
    USER_REQUEST_PROCESSING,
    AGENT_RESPONSE_GENERATED,
    AGENT_EXECUTION_FAILED,
)

logger = logging.getLogger(__name__)


class AgentService:
    def __init__(self, llm: ChatGroq, tools: list):
        self.agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt=SYSTEM_PROMPT,
        )

    def generate_response(self, user_message: str) -> str:
        logger.info(USER_REQUEST_PROCESSING)
        messages = [
            {
                "role": "user",
                "content": user_message,
            }
        ]
        agent_input = {"messages": messages}
        try:
            response = self.agent.invoke(input=agent_input)
            logger.info(AGENT_RESPONSE_GENERATED)
            return response["messages"][-1].content
        except Exception:
            logger.exception(AGENT_EXECUTION_FAILED)
            raise
