from langgraph.graph import StateGraph, START, END
from src.model.routes import AgentState
from pydantic import BaseModel

from src.controller.agents.product_owner   import product_owner_agent
from src.controller.agents.development_team import development_team_agent
from src.controller.agents.com_master       import com_master_agent
from src.controller.agents.scrum_master     import scrum_master_agent


def _build_graph():
    wf = StateGraph(AgentState)
    wf.add_node("product_owner",    product_owner_agent)
    wf.add_node("development_team", development_team_agent)
    wf.add_node("com_master",       com_master_agent)
    wf.add_node("scrum_master",     scrum_master_agent)

    wf.add_edge(START, "product_owner")
    wf.add_edge("product_owner",    "development_team")
    wf.add_edge("development_team", "com_master")
    wf.add_edge("com_master",       "scrum_master")
    wf.add_edge("scrum_master",     END)
    return wf.compile()


_graph = _build_graph()


async def executor_agent(query: str) -> str:
    initial_state = {"keys": {"query": query}}
    final_state: AgentState = await _graph.ainvoke(initial_state)
    return final_state["keys"]["response"]        
