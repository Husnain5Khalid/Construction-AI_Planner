from agents.tool_selector import select_tool
from agents.parameter_extractor import extract_parameters
from agents.response_generator import generate_response

from tools.executor import execute_tool


class ToolAgent:

    def run(self, question: str):

        tool = self._choose_tool(question)

        params = self._extract_parameters(question)

        result = self._execute_tool(tool, params)

        response = self._generate_response(question, result)

        return response

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

    def _generate_response(self, question: str, result):

        return generate_response(question, result)