import os
import subprocess
import requests

def list_repos(username):
    """List all repositories for a given GitHub username."""
    print(f'Fetching repositories for user {username}...')
    print('')
    print('')
    url = f'https://api.github.com/users/{username}/repos'
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    repos = response.json()
    print(f'Found {len(repos)} repositories.')
    print('')
    print('')
    return repos

def clone_repo(repo_url, repo_name):
    """Clone the repository if it doesn't exist."""
    if not os.path.exists(repo_name):
        print(f'Cloning repository {repo_name} from {repo_url}...')
        subprocess.call(['git', 'clone', repo_url])
        print(f'Repository {repo_name} cloned successfully.')
    else:
        print(f'Failed to clone repository {repo_name}, the repository already exists in the folder.')

def main():
    print('')
    print('')
    username = input('Enter the GitHub username: ')
    try:
        repos = list_repos(username)
    except requests.RequestException as e:
        print(f'Error fetching repositories: {e}')
        return

    if not repos:
        print('No repositories found.')
        return

    print('Repositories:')
    for i, repo in enumerate(repos, 1):
        print(f'{i}. {repo["name"]}')

    print('')
    print('')
    selected_repos = input('Enter the numbers of the repositories to download (comma-separated): ')
    selected_indices = [int(x.strip()) - 1 for x in selected_repos.split(',')]

    print('')
    print('')
    for i in selected_indices:
        if i >= 0 and i < len(repos):
            repo = repos[i]
            print(f'')    
            print(f'-----------------------------------------')    
            print(f'')   
            print(f'Processing repository {repo["name"]}...')
            clone_repo(repo['clone_url'], repo['name'])
        else:
            print(f'Invalid selection: {i + 1}')

    print(f'')    
    print(f'-----------------------------------------')    
    print(f'')   
    print('Finished processing repositories.')

if __name__ == "__main__":
    main()
