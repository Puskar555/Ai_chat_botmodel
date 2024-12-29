# File: communication_module.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Initialize the FastAPI app
app = FastAPI()

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"  # Replace with your actual API key

# Define request and response models
class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    response: str

# Route to handle user queries
@app.post("/communicate", response_model=QueryResponse)
async def communicate(query_request: QueryRequest):
    """
    Process user queries using OpenAI GPT.
    """
    try:
        # Send query to OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Specify GPT model
            prompt=query_request.query,
            max_tokens=150,
            temperature=0.7,
        )
        # Extract and return the model's response
        return QueryResponse(response=response.choices[0].text.strip())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

# Sample endpoint for testing
@app.get("/")
async def root():
    return {"message": "Communication module is running!"}

