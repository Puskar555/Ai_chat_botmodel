from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import openai
import pandas as pd
import io
import matplotlib.pyplot as plt
from pathlib import Path

# Initialize FastAPI app
app = FastAPI()

# Path to the frontend folder
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

# Global variable for uploaded data
uploaded_data = None

# OpenAI API Key
openai.api_key = "your_openai_api_key"  # Replace with actual API key


@app.get("/", response_class=HTMLResponse)
async def serve_frontend():
    """
    Serve the index.html file.
    """
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/static/{filename}")
async def serve_static(filename: str):
    """
    Serve static frontend files (CSS, JS).
    """
    file_path = FRONTEND_DIR / filename
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)


# Other backend endpoints (e.g., /upload_csv/, /communicate/) remain unchanged
