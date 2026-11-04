from langchain_groq import ChatGroq
from app.config.settings import settings

from app.utils.constant import API_KEY_MISSING


def get_groq_llm() -> ChatGroq:
    if not settings.GROQ_API_KEY:
        raise ValueError(API_KEY_MISSING)

    return ChatGroq(
        model=settings.GROQ_MODEL,
        api_key=settings.GROQ_API_KEY,
        # temperature=settings.GROQ_TEMPERATURE,
    )
