from pathlib import Path

# Get the current directory
current_dir = Path(__file__).resolve()

# Go two directories back
parent_dir = current_dir.parents[2]

print(parent_dir)
