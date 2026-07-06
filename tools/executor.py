from tools.registry import TOOLS

def execute_tool(tool_name:str, **kwargs): #kwargs mean Keyword argument (exmple: Tool_name=weather, kwargs=Riyadh)

    tool = TOOLS.get(tool_name)

    if tool is None:
        raise ValueError(f"unknown tool: {tool_name}")
    
    return tool(**kwargs)

