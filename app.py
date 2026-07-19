from graph.workflow import graph


def ask_construction_ai(question: str):

    result = graph.invoke(
        {
            "question": question,
            "route": "",
            "tool_name": None,
            "tool_input": {},
            "retrieved_documents": [],
            "tool_result": None,
            "answer": ""
        }
    )

    return {
        "answer": result["answer"],
        "route": result["route"],
        "tool_name": result["tool_name"],
        "retrieved_documents": result["retrieved_documents"]
    }