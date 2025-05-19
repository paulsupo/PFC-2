from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

async def product_owner_agent(state):
    state_dict = state["keys"]
    string_que = state_dict["query"]          
    # llm = ChatOpenAI(temperature=0)

    # prompt = (
    #     "Eres Product Owner. Convierte la petición en una user story en formato "
    #     "'Como <usuario> quiero <acción> para <beneficio>'.\n\n"
    #     f"Petición: {state.keys['query']}"
    # )
    # result = await llm.ainvoke([HumanMessage(content=prompt)])

    # state.keys["user_story"] = result.content
    string_po = string_que + " hola "
    return {
        "keys": {
            "string_po": string_po,
        }
    }
