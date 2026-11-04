import logging

from langchain_groq import ChatGroq
from langchain.agents import create_agent

from app.agent.prompts import SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class AgentService:
    def __init__(self, llm: ChatGroq, tools: list):
        self.agent = create_agent(
            model=llm,
            tools=tools,
            system_prompt=SYSTEM_PROMPT,
        )

    def generate_response(self, user_message: str) -> str:
        logger.info("Processing user request.")
        messages = [
            {
                "role": "user",
                "content": user_message,
            }
        ]
        agent_input = {"messages": messages}
        response = self.agent.invoke(input=agent_input)

        # print(response)

        print("======================================")
        print("Response: ", response)
        print("======================================")
        return response["messages"][-1].content
