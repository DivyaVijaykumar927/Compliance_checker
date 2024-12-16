from fastapi import APIRouter, HTTPException
from managers.embedding_manager import EmbeddingManager

router = APIRouter()

@router.post("/embed/")
def generate_embeddings(file_path: str):
    """
    API to generate embeddings for a chunked document.

    Args:
        file_path (str): Path to the document.

    Returns:
        dict: Embedding generation status.
    """
    try:
        manager = EmbeddingManager()
        manager.create_embeddings(file_path)
        return {"message": "Embeddings generated and saved successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding failed: {str(e)}")
