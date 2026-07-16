from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter
from rag.vector_store import ConstructionVectorStore

loader = PDFLoader(
    "data/Construction_Project_Specification_Sample.pdf"
)

documents = loader.load()

splitter = DocumentSplitter()

chunks = splitter.split(documents)

vector_store = ConstructionVectorStore()

db = vector_store.create(chunks)

print("Database Created Successfully!")
print(f"Total Chunks: {len(chunks)}")