from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME


class LLMAgent:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are a helpful construction AI assistant."
                ),
                (
                    "human",
                    "{question}"
                )
            ]
        )

        self.chain = self.prompt | self.llm

    def run(self, question):

        response = self.chain.invoke(
            {
                "question": question
            }
        )

        return response.content
    