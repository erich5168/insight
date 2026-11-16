from pathlib import Path

# EXECUTE: uv run python src/insight/utils/paths.py

# Sentinel File Approach.

# Finde the project root until you find `pyproject.toml` or `uv.lock` file
# - Always find root path
# - By going up layer by layer

def get_project_root() -> Path:
    
    # 1. Find current file path
    current_file = Path(__file__).resolve()
    
    #2. Loop through `current_file.parents`
    for parent in current_file.parents:
        
        # Each parent folder check if there is "pyuproject.toml"
        if Path(parent / "pyproject.toml").exists():
            print(f"Found pyproject.toml in {parent}")
            return parent
    
    raise FileNotFoundError("Could not find project root(pyproject.toml missing)")
    
# root = get_project_root()
# print(f"This is the Root: {root}")