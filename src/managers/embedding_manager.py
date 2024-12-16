import pickle
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import FAISS
from configuration.config import MODEL_NAME, VECTORSTORE_PATH

class EmbeddingManager:
    def create_embeddings(self, file_path: str):
        """
        Create embeddings and save them in a vector store.

        Args:
            file_path (str): Path to the document.
        """
        with open(file_path, "r") as f:
            content = f.read()
        
        hf_embeddings = HuggingFaceBgeEmbeddings(model_name=MODEL_NAME)
        vectorstore = FAISS.from_texts([content], hf_embeddings)

        with open(VECTORSTORE_PATH, "wb") as f:
            pickle.dump(vectorstore, f)
