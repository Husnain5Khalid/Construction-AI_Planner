from rag.embeddings import get_embedding_model

embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "Concrete grade for columns"
)

print(type(vector))

print(len(vector))

