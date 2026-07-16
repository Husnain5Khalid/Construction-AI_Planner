from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model


class ConstructionVectorStore:

    def __init__(self):

        self.embedding_model = get_embedding_model()

        self.persist_directory = "vector_db"

    def create(self, documents):

        return Chroma.from_documents(
            documents=documents,
            embedding=self.embedding_model,
            persist_directory=self.persist_directory
        )

    def load(self):

        return Chroma(
            persist_directory=self.persist_directory,
            embedding_function=self.embedding_model
        )

'''
Without persist_directory:

Database

↓

Memory

↓

Lost after restart

With it:

Database

↓

vector_db/

↓

Saved on disk

Next time you run the application:

No need to recreate embeddings.


'''