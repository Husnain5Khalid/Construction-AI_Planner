from rag.loader import PDFLoader

loader = PDFLoader(
    "data/Construction_Project_Specification_Sample.pdf"
)

documents = loader.load()

print(type(documents))
print(len(documents))
print(documents[0])


