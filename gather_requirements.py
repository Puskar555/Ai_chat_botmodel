# File: gather_requirements.py

def gather_requirements():
    """
    Gather and document the functional and non-functional requirements
    for the AI software.
    """
    requirements = {
        "Functional Requirements": [
            "Enable natural language communication using NLP.",
            "Provide recommendations for AI algorithm selection.",
            "Generate AI algorithm code based on user inputs.",
            "Perform analysis on structured (e.g., CSV) and unstructured data (e.g., text).",
            "Visualize analysis results (charts, graphs, etc.).",
        ],
        "Non-functional Requirements": [
            "System should respond to user queries in under 2 seconds.",
            "Ensure data privacy and secure communication with encryption.",
            "Support scaling to handle up to 1,000 concurrent users.",
        ],
        "Technology Stack": {
            "Backend": "Python with Flask or FastAPI",
            "Frontend": "React.js",
            "Database": "PostgreSQL for structured data; MongoDB for unstructured data.",
            "Libraries": {
                "NLP": ["OpenAI GPT", "Hugging Face Transformers", "SpaCy"],
                "Data Analysis": ["Pandas", "NumPy", "Scikit-learn"],
                "Visualization": ["Matplotlib", "Seaborn", "Plotly"],
            },
        },
        "Data Requirements": [
            "Support text data (e.g., user queries, raw documents).",
            "Support tabular data (e.g., CSV files).",
            "Optional: Image data for advanced analysis.",
        ],
    }

    # Print the requirements document
    print("==== Requirements Document ====")
    print("\nFunctional Requirements:")
    for idx, req in enumerate(requirements["Functional Requirements"], start=1):
        print(f"{idx}. {req}")

    print("\nNon-functional Requirements:")
    for idx, req in enumerate(requirements["Non-functional Requirements"], start=1):
        print(f"{idx}. {req}")

    print("\nTechnology Stack:")
    for key, value in requirements["Technology Stack"].items():
        if isinstance(value, list):
            print(f"{key}:")
            for item in value:
                print(f"  - {item}")
        elif isinstance(value, dict):
            print(f"{key}:")
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {', '.join(sub_value)}")
        else:
            print(f"{key}: {value}")

    print("\nData Requirements:")
    for idx, req in enumerate(requirements["Data Requirements"], start=1):
        print(f"{idx}. {req}")

# Run the function to display the requirements document
if __name__ == "__main__":
    gather_requirements()
