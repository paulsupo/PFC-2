from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

async def com_master_agent(state):
    state_dict = state["keys"]
    string_dt = state_dict["string_dt"]
    # llm = ChatOpenAI(temperature=0)

    # prompt = (
    #     "Eres Product Owner. Convierte la petición en una user story en formato "
    #     "'Como <usuario> quiero <acción> para <beneficio>'.\n\n"
    #     f"Petición: {state.keys['query']}"
    # )
    # result = await llm.ainvoke([HumanMessage(content=prompt)])

    # state.keys["user_story"] = result.content
    
    string_cm = string_dt + "estas "
    return {
        "keys": {
            "string_cm": string_cm,
        }
    }
