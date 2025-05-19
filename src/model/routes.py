from pydantic import BaseModel
from typing import Dict, Any

class QueryRequest(BaseModel):
    query: str

class AgentState(BaseModel):
    keys: Dict[str, Any] = {}

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        return setattr(self, key, value)

class ExecutorAgentRequest(BaseModel):
    query: str