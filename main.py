from fastapi import FastAPI
from controllers import (
    chunk_controller,
    embedding_controller,
    ingestion_controller,
)

app = FastAPI()

# Include routers
app.include_router(chunk_controller.router, prefix="/api/chunks")
app.include_router(embedding_controller.router, prefix="/api/embeddings")
app.include_router(ingestion_controller.router, prefix="/api/ingest")

@app.get("/")
def read_root():
    return {"message": "Welcome to the PDF processing API"}
