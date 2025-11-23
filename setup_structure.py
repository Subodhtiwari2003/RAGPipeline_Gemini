import os

# Define the base directory
base_dir = "RAGPipeline_Gemini"

# Define the folder structure
folders = [
    "app/core",
    "app/modules",
    "app/prompts"
]

# Define the files with their paths
files = {
    "app/core/config.py": "# Environment variables & Settings\n",
    "app/core/logging.py": "# Custom logger setup\n",
    "app/modules/ingestion.py": "# Scrapes and chunks data\n",
    "app/modules/storage.py": "# Handles Embeddings & ChromaDB\n",
    "app/modules/retrieval.py": "# RAG Logic & Generation\n",
    "app/prompts/templates.py": "# Prompts stored separately\n",
    "app/main.py": "# FastAPI Entry Point\n",
    ".env": "# Secrets (API Keys)\n",
    "Dockerfile": "# Docker Image configuration\n",
    "docker-compose.yml": "# Container Orchestration\n",
    "requirements.txt": "# Dependencies\n"
}

def create_structure():
    # Create base directory
    os.makedirs(base_dir, exist_ok=True)

    # Create subfolders
    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

    # Create files
    for filepath, content in files.items():
        full_path = os.path.join(base_dir, filepath)
        with open(full_path, "w") as f:
            f.write(content)

    print(f"✅ Project structure created under '{base_dir}'")

if __name__ == "__main__":
    create_structure()