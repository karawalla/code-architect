import os
from git import Repo
from git.exc import GitCommandError
from typing import Optional

def clone_repository(url: str, local_path: str, branch: Optional[str] = None) -> tuple[str, str]:
    """Clone a git repository to a local path.
    
    Args:
        url: Repository URL
        local_path: Local path to clone to
        branch: Optional branch to checkout
        
    Returns:
        tuple[str, str]: (local path, repo name)
        
    Raises:
        GitCommandError: If clone fails
    """
    try:
        # Extract repo name from URL
        repo_name = url.rstrip("/").split("/")[-1]
        if repo_name.endswith(".git"):
            repo_name = repo_name[:-4]
            
        # Create full path
        full_path = os.path.join(local_path, repo_name)
        
        # Clone repo
        repo = Repo.clone_from(url, full_path)
        
        # Checkout specific branch if provided
        if branch and branch != repo.active_branch.name:
            repo.git.checkout(branch)
            
        return full_path, repo_name
        
    except GitCommandError as e:
        raise GitCommandError(f"Failed to clone repository: {str(e)}", e.status)
