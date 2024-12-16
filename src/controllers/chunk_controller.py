from fastapi import APIRouter, HTTPException
from managers.chunk_manager import ChunkManager

router = APIRouter()

@router.post("/chunk/")
def chunk_document(file_path: str):
    """
    API to chunk a document into smaller parts.

    Args:
        file_path (str): Path to the document.

    Returns:
        dict: Chunked data.
    """
    try:
        manager = ChunkManager()
        chunks = manager.split_document(file_path)
        return {"message": "Document chunked successfully", "chunks": chunks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chunking failed: {str(e)}")

