from pydantic import BaseModel, Field, field_validator
from app.util.constant import (
    AGENT_REQUEST_DESC,
    AGENT_REQUEST_EXAMPLE,
    AGENT_RESPONSE_DESC,
    EMPTY_MESSAGE,
)


class AgentRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=10000,
        description=AGENT_REQUEST_DESC,
        examples=[AGENT_REQUEST_EXAMPLE],
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError(EMPTY_MESSAGE)

        return value


class AgentResponse(BaseModel):
    response: str = Field(
        description=AGENT_RESPONSE_DESC,
    )
