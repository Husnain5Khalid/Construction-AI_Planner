from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import GROQ_API_KEY, MODEL_NAME
from prompts.rag import RAG_SYSTEM_PROMPT
from rag.retriever import ConstructionRetriever


class RAGAgent:

    def __init__(self):

        self.retriever = ConstructionRetriever()

        self.llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=MODEL_NAME,
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", RAG_SYSTEM_PROMPT),
                (
                    "human",
                    """
Context:
{context}

Question:
{question}
"""
                )
            ]
        )

        self.chain = self.prompt | self.llm

    def _retrieve_context(self, question):

        documents = self.retriever.retrieve(question)

        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        return context

    def run(self, question: str):

        context = self._retrieve_context(question)

        response = self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )

        return response.content