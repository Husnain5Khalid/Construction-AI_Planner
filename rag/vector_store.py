from langchain_chroma import Chroma

from rag.embeddings import get_embedding_model
from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter


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


def ingest_pdf(pdf_path: str):
    """
    Complete PDF ingestion pipeline.
    """

    # Load PDF
    loader = PDFLoader(pdf_path)
    documents = loader.load()

    # Split into chunks
    splitter = DocumentSplitter()
    chunks = splitter.split(documents)

    # Store in ChromaDB
    vector_store = ConstructionVectorStore()
    vector_store.create(chunks)

    return len(chunks)