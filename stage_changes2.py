#pip install GitPython
import os
import git

# Set repository path (current directory in this case)
repo_path = '.'

# Path to the .txt file that contains the list of relative paths
txt_file_path = 'files_to_stage.txt'

# Open the .txt file and extract just the file names
with open(txt_file_path, 'r') as f:
    files_to_stage = [os.path.basename(line.strip()) for line in f.readlines()]

# Initialize repository object
repo = git.Repo(repo_path)

# Fetch all changes (even uncommitted ones)
# 'untracked', 'index.diff(None)' to get all modified, added, deleted files
changed_files = [item.a_path for item in repo.index.diff(None)] + repo.untracked_files

# Compare and stage only files whose basenames are listed in the .txt file
for file in changed_files:
    # Extract the basename from the full path and check if it's in the list
    if os.path.basename(file) in files_to_stage:
        print(f'Staging file: {file}')
        repo.git.add(file)

# You can also commit staged changes with a message if needed:
# repo.git.commit('-m', 'Staging specific files based on .txt list')
