from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

async def scrum_master_agent(state):
    state_dict = state["keys"]
    string_cm = state_dict["string_cm"]
    # llm = ChatOpenAI(temperature=0)

    # prompt = (
    #     "Eres Product Owner. Convierte la petición en una user story en formato "
    #     "'Como <usuario> quiero <acción> para <beneficio>'.\n\n"
    #     f"Petición: {state.keys['query']}"
    # )
    # result = await llm.ainvoke([HumanMessage(content=prompt)])

    # state.keys["user_story"] = result.content
    
    string_sm = string_cm + "hoy "
    return {
        "keys": {
            "response": string_sm,
        }
    }
