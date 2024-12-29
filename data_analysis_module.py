# File: data_analysis_module.py

import pandas as pd
import matplotlib.pyplot as plt
from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
import io

# Initialize the FastAPI app
app = FastAPI()

class AnalysisRequest(BaseModel):
    column: str  # Column to analyze (e.g., for statistics or visualization)

@app.post("/upload_csv/")
async def upload_csv(file: UploadFile):
    """
    Endpoint to upload a CSV file for analysis.
    """
    try:
        if not file.filename.endswith(".csv"):
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
        
        # Read the uploaded CSV into a Pandas DataFrame
        content = await file.read()
        data = pd.read_csv(io.StringIO(content.decode("utf-8")))
        return {"message": "File uploaded successfully.", "columns": list(data.columns)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")

@app.post("/analyze/")
async def analyze(file: UploadFile, analysis_request: AnalysisRequest):
    """
    Perform basic analysis on the uploaded data.
    """
    try:
        # Read the uploaded CSV into a Pandas DataFrame
        content = await file.read()
        data = pd.read_csv(io.StringIO(content.decode("utf-8")))
        
        if analysis_request.column not in data.columns:
            raise HTTPException(status_code=400, detail="Invalid column name.")
        
        # Generate descriptive statistics
        stats = data[analysis_request.column].describe().to_dict()

        # Plot a histogram of the column
        plt.figure(figsize=(8, 6))
        data[analysis_request.column].hist(bins=20, color='blue', alpha=0.7)
        plt.title(f"Distribution of {analysis_request.column}")
        plt.xlabel(analysis_request.column)
        plt.ylabel("Frequency")
        plt.grid(True)

        # Save the plot
        plt.savefig("distribution_plot.png")

        return {"message": "Analysis complete.", "statistics": stats, "plot_path": "distribution_plot.png"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during analysis: {str(e)}")

