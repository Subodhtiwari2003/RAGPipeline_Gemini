from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.modules.ingestion import load_and_chunk_data
from app.modules.storage import index_documents
from app.modules.retrieval import run_financial_analysis

import os
print("LangSmith API Key:", os.getenv("LANGCHAIN_API_KEY"))
print("Tracing Enabled:", os.getenv("LANGCHAIN_TRACING_V2"))
print("Project:", os.getenv("LANGCHAIN_PROJECT"))


app = FastAPI(title="AI Financial Research Agent")

# Data Models
class IngestRequest(BaseModel):
    urls: list[str]

class QueryRequest(BaseModel):
    question: str

@app.post("/ingest")
async def ingest_data(request: IngestRequest):
    """Scrape URLs and Index them into Vector Store"""
    try:
        chunks = load_and_chunk_data(request.urls)
        index_documents(chunks)
        return {"status": "success", "message": f"Indexed {len(chunks)} chunks"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze")
async def analyze(request: QueryRequest):
    """Run the RAG Agent"""
    try:
        # LangSmith will automatically trace this call due to @traceable
        answer = run_financial_analysis(request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))# FastAPI Entry Point
