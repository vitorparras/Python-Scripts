import os
import subprocess

def is_git_repo(path):
    """Check if a given directory is a git repository."""
    return subprocess.call(['git', '-C', path, 'status'],
                           stderr=subprocess.STDOUT,
                           stdout=open(os.devnull, 'w')) == 0

def fetch_changes(path):
    """Fetch changes for the git repository."""
    print(f'Fetching changes in {path}...')
    subprocess.call(['git', '-C', path, 'fetch'])

def has_uncommitted_changes(path):
    """Check if there are uncommitted changes in the repository."""
    result = subprocess.run(['git', '-C', path, 'status', '--porcelain'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    return result.stdout != b''

def commit_changes(path, message):
    """Commit changes in the repository with the provided message."""
    print(f'Committing changes in {path} with message: {message}')
    subprocess.call(['git', '-C', path, 'add', '--all'])
    subprocess.call(['git', '-C', path, 'commit', '-m', message])

def pull_changes(path):
    """Pull changes from the remote repository."""
    print(f'Pulling changes in {path}...')
    subprocess.call(['git', '-C', path, 'pull'])

def process_repo(path):
    """Process a single git repository."""
    fetch_changes(path)
    if has_uncommitted_changes(path):
        print(f'Uncommitted changes found in {path}')
        user_input = input('Enter commit message or type "skip" to skip this repository: ')
        if user_input.lower() == 'skip':
            print(f'Skipping {path}')
            return False
        else:
            commit_changes(path, user_input)
            pull_changes(path)
    else:
        pull_changes(path)
    print(f'')    
    print(f'-----------------------------------------')    
    print(f'')   
    return True

def process_directory(root_path):
    """Process all directories in the first level to find and update git repositories."""
    for entry in os.listdir(root_path):
        dir_path = os.path.join(root_path, entry)
        if os.path.isdir(dir_path) and is_git_repo(dir_path):
            print(f'Processing repository at {dir_path}')
            if not process_repo(dir_path):
                continue  # Skip to the next directory in the root

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f'')    
    print(f'')    
    print(f'Starting to process repositories in {script_directory}')
    print(f'')    
    print(f'-----------------------------------------')    
    print(f'')   
    process_directory(script_directory)
    print(f'')     
    print('Finished processing repositories.')
    print(f'')   
    print(f'')   
    print(f'-----------------------------------------')    
