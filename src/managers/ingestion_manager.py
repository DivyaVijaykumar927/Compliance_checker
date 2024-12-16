import os
from managers.chunk_manager import ChunkManager

class IngestionManager:
    def __init__(self, upload_dir="./uploaded_files"):
        self.upload_dir = upload_dir
        os.makedirs(self.upload_dir, exist_ok=True)
    
    async def save_and_process(self, file):
        """
        Save the uploaded file and process it.

        Args:
            file (UploadFile): The uploaded file.

        Returns:
            str: Path to the saved file.
        """
        file_path = os.path.join(self.upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # Trigger chunking after saving
        ChunkManager().split_document(file_path)
        return file_path
