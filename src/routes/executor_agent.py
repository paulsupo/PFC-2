from fastapi import APIRouter, Depends, HTTPException
from pydantic import ValidationError

from src.controller.agents.executor_agent import executor_agent
from src.model.routes import ExecutorAgentRequest

router = APIRouter()

@router.post("/executor-agent/")
async def executor_agent_endpoint(request: ExecutorAgentRequest):
    try:
        result = await executor_agent(
            request.query
        )   
        return {"response": result}
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
