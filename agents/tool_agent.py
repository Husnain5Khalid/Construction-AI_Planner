from agents.tool_selector import select_tool
from agents.parameter_extractor import extract_parameters


class ToolAgent:

    def run(self, question: str):

        tool = self._choose_tool(question)

        params = self._extract_parameters(question)

        print("Tool:", tool)
        print("Parameters:", params)

        return params

    def _choose_tool(self, question: str):

        tool = select_tool(question)

        return tool.tool_name

    def _extract_parameters(self, question: str):

        return extract_parameters(question)