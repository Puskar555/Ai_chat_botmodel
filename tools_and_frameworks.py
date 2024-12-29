# File: tools_and_frameworks.py

def choose_tools_and_frameworks():
    """
    Select and document the tools and frameworks for building the AI system.
    """
    tools = {
        "NLP Tools": [
            "OpenAI GPT (API for conversational AI).",
            "Hugging Face Transformers (for fine-tuning NLP models).",
            "SpaCy (lightweight NLP library for preprocessing).",
        ],
        "Data Analysis Tools": [
            "Pandas (data manipulation).",
            "NumPy (numerical computing).",
            "Scikit-learn (machine learning).",
            "TensorFlow or PyTorch (for deep learning if needed).",
        ],
        "Visualization Libraries": [
            "Matplotlib (basic charts).",
            "Seaborn (statistical visualization).",
            "Plotly (interactive visualizations).",
        ],
        "Backend Frameworks": [
            "Flask or FastAPI (lightweight Python frameworks for building APIs).",
        ],
        "Frontend Frameworks": [
            "React.js (component-based UI development).",
            "Next.js (React-based framework with server-side rendering).",
        ],
        "Database": [
            "PostgreSQL (structured data).",
            "MongoDB (unstructured data).",
        ],
        "Deployment Platforms": [
            "AWS (S3 for storage, Lambda for serverless functions).",
            "Google Cloud (BigQuery for large-scale data).",
            "Azure (Data analysis and AI services).",
        ],
    }

    # Print the selected tools and frameworks
    print("==== Tools and Frameworks ====")
    
    for category, items in tools.items():
        print(f"\n{category}:")
        for idx, item in enumerate(items, start=1):
            print(f"  {idx}. {item}")

# Run the function to display the tools and frameworks
if __name__ == "__main__":
    choose_tools_and_frameworks()
