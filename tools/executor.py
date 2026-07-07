from tools.registry import TOOL_REGISTRY

 #kwargs mean Keyword argument (exmple: Tool_name=weather, kwargs=Riyadh)
from tools.registry import TOOL_REGISTRY

def execute_tool(tool_name: str, **kwargs):
    print("===== EXECUTOR START =====")
    print("Tool:", tool_name)
    print("Kwargs:", kwargs)

    tool = TOOL_REGISTRY.get(tool_name)

    print("Function:", tool)

    if tool is None:
        raise ValueError(f"Unknown tool: {tool_name}")

    result = tool(**kwargs)

    print("Tool Result:", result)
    print("===== EXECUTOR END =====")

    return result



    
