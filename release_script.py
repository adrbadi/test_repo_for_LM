import subprocess
import sys

def run_command(command):
    """Run a shell command and return its output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {command}\n{e.stderr}")
        sys.exit(1)

def main(branch_to_merge):
    # Step 1: Merge branch with --no-commit --no-ff
    print(f"Running: git merge {branch_to_merge} --no-commit --no-ff")
    run_command(f"git merge {branch_to_merge} --no-commit --no-ff")

    # Step 2: Run git reset
    print("Running: git reset")
    run_command("git reset")

    # Step 3: Execute stage_changes.py script
    print("Running stage_changes.py script")
    run_command("python stage_changes.py")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python chain_git_operations.py <branch_to_merge>")
        sys.exit(1)

    branch_to_merge = sys.argv[1]
    main(branch_to_merge)
