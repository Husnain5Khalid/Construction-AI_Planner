from rag.loader import PDFLoader
from rag.splitter import DocumentSplitter

loader = PDFLoader(
    "data/Construction_Project_Specification_Sample.pdf"
)

documents = loader.load()

splitter = DocumentSplitter()

chunks = splitter.split(documents)

print(len(chunks))

print(chunks[0].page_content)
print(chunks[0].metadata)