from sentence_transformers import SentenceTransformer
class embedding:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    def embed_documents(self,items):
        embeddings = self.model.encode(items)
        return embeddings.tolist()
    def embed_query(self,query):
        return self.model.encode(query).tolist()