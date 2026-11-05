import logging

from app.agent.agent_service import AgentService
from app.schema.agent_schema import AgentRequest, AgentResponse

logger = logging.getLogger(__name__)


def generate_agent_response(
    request: AgentRequest,
    agent_service: AgentService,
) -> AgentResponse:
    logger.info("Agent API request received.")

    response = agent_service.generate_response(user_message=request.message)

    return AgentResponse(response=response)
