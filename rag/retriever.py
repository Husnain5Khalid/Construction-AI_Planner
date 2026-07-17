from rag.vector_store import ConstructionVectorStore

class ConstructionRetriever:

    def __init__(self):
        vector_store = ConstructionVectorStore()

        self.db = vector_store.load()
    
    def retrieve(
        self,
        query: str,
        k: int = 3
    ):
        
        results = self.db.similarity_search(   #We don't manually create the query embedding. similarity_search() handles that using the embedding model you supplied when loading the database.
            query=query,
            k=k
        )

        return results
    

        