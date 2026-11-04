from fastapi import APIRouter, Depends, Request

from app.agent.service import AgentService
from app.api.controller import agent_controller
from app.api.controller.agent_controller import generate_agent_response
from app.schema.agent_schema import AgentRequest, AgentResponse

router = APIRouter(prefix="/api/v1/agent", tags=["AI Agent"])


def get_agent_service(request: Request) -> AgentService:
    return request.app.state.agent_service


@router.post(
    path="/chat",
    response_model=AgentResponse,
)
def chat_with_agent(
    request: AgentRequest,
    agent_service: AgentService = Depends(get_agent_service),
) -> AgentResponse:
    return generate_agent_response(
        request=request,
        agent_service=agent_service,
    )
