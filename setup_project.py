import os

folders = [
    "backend/routes",
    "backend/services",
    "backend/rag_pipeline",
    "backend/risk_engine",
    "backend/models",
    "backend/utils",
    "backend/config",
    "data/documents",
    "embeddings",
    "frontend",
    "docker"
]

files = [
    "backend/app.py",
    "backend/config/settings.py",
    "backend/utils/helpers.py",
    "requirements.txt",
    "README.md"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for file in files:
    with open(file, "w") as f:
        pass

print("Project structure created successfully!")