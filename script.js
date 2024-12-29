// File: script.js

// URLs for backend endpoints
const UPLOAD_URL = "http://localhost:8000/upload_csv/";
const QUERY_URL = "http://localhost:8000/communicate/";

// Select DOM elements
const fileInput = document.getElementById("file-input");
const uploadBtn = document.getElementById("upload-btn");
const queryInput = document.getElementById("user-query");
const queryBtn = document.getElementById("query-btn");
const resultsDiv = document.getElementById("results");

// Event listener for file upload
uploadBtn.addEventListener("click", async () => {
  if (!fileInput.files[0]) {
    alert("Please select a file to upload.");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  try {
    const response = await fetch(UPLOAD_URL, {
      method: "POST",
      body: formData,
    });

    if (response.ok) {
      const result = await response.json();
      alert(`File uploaded successfully. Columns: ${result.columns.join(", ")}`);
    } else {
      const error = await response.json();
      alert(`Error: ${error.detail}`);
    }
  } catch (error) {
    console.error("Error uploading file:", error);
    alert("Failed to upload file. Please try again.");
  }
});

// Event listener for query submission
queryBtn.addEventListener("click", async () => {
  const query = queryInput.value.trim();

  if (!query) {
    alert("Please enter a query.");
    return;
  }

  try {
    const response = await fetch(QUERY_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });

    if (response.ok) {
      const result = await response.json();
      displayResults(result);
    } else {
      const error = await response.json();
      alert(`Error: ${error.detail}`);
    }
  } catch (error) {
    console.error("Error processing query:", error);
    alert("Failed to process query. Please try again.");
  }
});

// Function to display results
function displayResults(data) {
  resultsDiv.innerHTML = ""; // Clear previous results

  if (data.action === "descriptive statistics") {
    const stats = data.statistics;
    const statsList = Object.keys(stats)
      .map((key) => `<li>${key}: ${stats[key]}</li>`)
      .join("");
    resultsDiv.innerHTML = `<ul>${statsList}</ul>`;
  } else if (data.action === "visualization") {
    const imgPath = data.plot_path;
    resultsDiv.innerHTML = `<img src="${imgPath}" alt="Visualization">`;
  } else {
    resultsDiv.innerHTML = "<p>Unknown action. No results to display.</p>";
  }
}
