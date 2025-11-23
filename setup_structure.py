import os

# No base_dir — we use current directory
folders = [
    "app/core",
    "app/modules",
    "app/prompts"
]

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

def create_structure_here():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for filepath, content in files.items():
        with open(filepath, "w") as f:
            f.write(content)

    print("✅ Structure added to current directory")

if __name__ == "__main__":
    create_structure_here()