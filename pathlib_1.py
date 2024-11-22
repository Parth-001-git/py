from pathlib import Path

# Create a Path object for the current working directory
path = Path.cwd() / "data.txt"

# Ensure the file exists
path.touch(exist_ok=True)