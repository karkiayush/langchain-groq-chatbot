from langchain_groq import ChatGroq

from app.chatbot.prompts import SYSTEM_PROMPT


class ChatbotService:
    # injecting LLM through constructor instead of initializing ChatGroq directly inside ChatBotService aka DI
    def __init__(self, llm: ChatGroq):
        self.llm = llm

    def generate_response(self, user_message: str) -> str:
        messages = [
            ("system", SYSTEM_PROMPT),
            ("human", user_message),
        ]

        response = self.llm.invoke(messages)
        return response.content
