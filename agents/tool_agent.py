from agents.tool_selector import select_tool
from agents.parameter_extractor import extract_parameters

from tools.executor import execute_tool


class ToolAgent:

    def run(self, question: str):
        print("Step 1: Choosing tool...")
        tool = self._choose_tool(question)

        print("Tool Selected:", tool)

        print("Step 2: Extracting parameters...")
        params = self._extract_parameters(question)

        print("Parameters Extracted:", params)

        print("Step 3: Executing tool...")
        result = self._execute_tool(tool, params)

        print("Step 4: Tool execution completed.")

        print("Result:", result)

        return result

        
    def _choose_tool(self, question: str):

        tool = select_tool(question)

        return tool.tool_name

    def _extract_parameters(self, question: str):

        return extract_parameters(question)

    def _execute_tool(self, tool: str, params):

        return execute_tool(
            tool,
            **params.model_dump(exclude_none=True)
        )