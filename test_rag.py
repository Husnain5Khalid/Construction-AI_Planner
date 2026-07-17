from rag.rag_agent import RAGAgent

agent = RAGAgent()

question = "What concrete grade is used for columns?"

answer = agent.run(question)

print(answer)