from rag.retriever import ConstructionRetriever

retriever = ConstructionRetriever()

results = retriever.retrieve(
    "What concrete grade is used for columns?"
)

print(results)

for doc in results:

    print(doc.page_content)

    print("=" * 50)

for doc in results:

    print(doc.metadata)

    