import pytest
from fastapi.testclient import TestClient
from integration_module import app  # Import the FastAPI app from the integration module

client = TestClient(app)

# Sample CSV content for testing
SAMPLE_CSV = """age,income,sales
25,50000,200
30,60000,300
35,70000,400
"""

@pytest.fixture
def upload_csv():
    """
    Upload a sample CSV for testing.
    """
    response = client.post(
        "/upload_csv/",
        files={"file": ("test.csv", SAMPLE_CSV, "text/csv")},
    )
    assert response.status_code == 200
    return response.json()

def test_upload_csv(upload_csv):
    """
    Test the CSV upload functionality.
    """
    assert "message" in upload_csv
    assert "columns" in upload_csv
    assert upload_csv["columns"] == ["age", "income", "sales"]

def test_descriptive_statistics(upload_csv):
    """
    Test descriptive statistics functionality.
    """
    query = {"query": "Give me descriptive statistics for the income column."}
    response = client.post("/communicate/", json=query)
    assert response.status_code == 200
    result = response.json()
    assert result["action"] == "descriptive statistics"
    assert result["column"] == "income"
    assert "statistics" in result
    assert "mean" in result["statistics"]

def test_visualization(upload_csv):
    """
    Test visualization functionality.
    """
    query = {"query": "Show me a histogram of the sales column."}
    response = client.post("/communicate/", json=query)
    assert response.status_code == 200
    result = response.json()
    assert result["action"] == "visualization"
    assert result["column"] == "sales"
    assert "plot_path" in result
