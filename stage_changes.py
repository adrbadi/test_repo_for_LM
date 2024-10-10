import subprocess

def stage_files_from_txt(txt_file):
    # Read the file names from the txt file and print them for debugging
    with open(txt_file, 'r') as f:
        file_names = f.read().splitlines()
        print("File names read from txt file:")
        for file_name in file_names:
            print(file_name)
    
    # Get the list of changed files
    result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
    changed_files = result.stdout.splitlines()
    print("\nChanged files:")
    for line in changed_files:
        print(line)
    
    # Stage the files that match the names in the txt file
    for line in changed_files:
        status, file_name = line[:2], line[3:]
        if file_name in file_names:
            subprocess.run(['git', 'add', file_name])
            print(f"Staged: {file_name}")
        else:
            print(f"Not staged: {file_name}")

# Specify the path to the txt file containing the file names
txt_file = 'files_to_stage.txt'

# Stage the files
stage_files_from_txt(txt_file)
