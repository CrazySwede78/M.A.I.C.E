```python
import pinecone
import os

class PineconeVectorDB:
    def __init__(self):
        self.index_name = "creative-writing-projects"
        self.api_key = os.getenv("PINECONE_API_KEY")
        pinecone.init(api_key=self.api_key)
        if self.index_name not in pinecone.deployment_info():
            pinecone.create_index(name=self.index_name, metric="cosine", shards=1)

    def upsert_vectors(self, item_id, vector):
        pinecone.upsert(index_name=self.index_name, ids=[item_id], vectors=[vector])

    def query_vectors(self, vector, top_k=5):
        results = pinecone.query(index_name=self.index_name, queries=[vector], top_k=top_k)
        return results.ids[0], results.scores[0]

    def delete_index(self):
        pinecone.deactivate(index_name=self.index_name)
        pinecone.delete_index(index_name=self.index_name)

    def __del__(self):
        pinecone.deinit()
```