import os
import github
from github import Github

# Helper function to recursively build the structured HTML representation of the repo
def get_html_repo_structure(path='.', prefix='', is_last=False):
    html_structure = []

    try:
        items = sorted(os.listdir(path))
    except FileNotFoundError:
        print(f"Path not found: {path}")
        return html_structure

    for i, item in enumerate(items):
        if item.startswith('.'):
            continue  # Skip hidden files and directories
        item_path = os.path.join(path, item)
        is_current_last = i == len(items) - 1

        # Add branch markers for the tree structure
        branch_marker = '└── ' if is_current_last else '├── '
        new_prefix = prefix + ('    ' if is_current_last else '│   ')

        if os.path.isdir(item_path):
            # Directory: Use expandable HTML with branch markers
            html_structure.append(f"{prefix}{branch_marker}<details><summary><b>{item}/</b></summary>")
            html_structure.extend(get_html_repo_structure(item_path, new_prefix))
            html_structure.append(f"{prefix}</details>")
        else:
            # File: Show file name with branch marker
            html_structure.append(f"{prefix}{branch_marker}{item}")

    return html_structure

# Function to update the repo_structure.html file
def update_structure_file(structure):
    try:
        with open('Documentation/repo_structure.html', 'w') as f:
            f.write('\n'.join(structure))
        print("repo_structure.html updated successfully.")
    except IOError as e:
        print(f"Error writing to repo_structure.html: {e}")

# Function to update the README.md with the new HTML structure
def update_README(structure):
    try:
        with open('Documentation/PROJECT_STRUCTURE.md', 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("PROJECT_STRUCTURE.md not found.")
        return

    start_marker = '<!-- START_STRUCTURE -->'
    end_marker = '<!-- END_STRUCTURE -->'

    start_index = content.find(start_marker)
    end_index = content.find(end_marker)

    if start_index != -1 and end_index != -1:
        new_content = (
            content[:start_index + len(start_marker)] +
            '\n<pre>\n' + '\n'.join(structure) + '\n</pre>\n' +
            content[end_index:]
        )
        try:
            with open('Documentation/PROJECT_STRUCTURE.md', 'w') as f:
                f.write(new_content)
            print("PROJECT_STRUCTURE.md updated with new structure.")
        except IOError as e:
            print(f"Error writing to PROJECT_STRUCTURE.md: {e}")
    else:
        print("Markers not found in PROJECT_STRUCTURE.md. Structure not updated.")

# Main function to compare and update repository structure
def main():
    gh_token = os.getenv('GH_TOKEN')
    gh_repo = os.getenv('GITHUB_REPOSITORY')

    if not gh_token or not gh_repo:
        print("Environment variables GH_TOKEN and GITHUB_REPOSITORY must be set.")
        return

    g = Github(gh_token)
    repo = g.get_repo(gh_repo)

    current_structure = get_html_repo_structure()

    try:
        # Fetch the contents of repo_structure.html from GitHub
        contents = repo.get_contents("Documentation/repo_structure.html")
        existing_structure = contents.decoded_content.decode().split('\n')
    except github.GithubException:
        existing_structure = None

    if current_structure != existing_structure:
        update_structure_file(current_structure)
        update_README(current_structure)
        print("Repository structure updated.")
    else:
        print("No changes in repository structure.")

if __name__ == "__main__":
    main()
