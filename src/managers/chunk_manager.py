from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

class ChunkManager:
    def split_document(self, file_path: str):
        """
        Split the document into chunks.

        Args:
            file_path (str): Path to the document.

        Returns:
            list: List of chunks.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError("Document not found.")
        
        with open(file_path, "r") as f:
            content = f.read()
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(content)
        return chunks
