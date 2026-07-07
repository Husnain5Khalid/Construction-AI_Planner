from agents.tool_selector import select_tool


class ToolAgent:

    def run(self, question: str):

        tool = self._choose_tool(question)

        return tool

    def _choose_tool(self, question: str):

        tool = select_tool(question)

        return tool.tool_name
    
    