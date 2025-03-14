from fastapi import APIRouter, HTTPException
import os

from models.repo_schemas import RepoRequest, RepoResponse
from utils.git import clone_repository, GitCommandError

router = APIRouter()

@router.post("/repos", response_model=RepoResponse)
async def create_repo(request: RepoRequest) -> RepoResponse:
    """Clone a GitHub repository to local storage.
    
    Args:
        request: Repository details including URL and optional branch
        
    Returns:
        RepoResponse with local path and repository details
        
    Raises:
        HTTPException: If clone fails or invalid input
    """
    try:
        repos_path = os.getenv("REPOS_PATH", "./repos")
        local_path, repo_name = clone_repository(
            str(request.url),
            repos_path,
            request.branch
        )
        
        return RepoResponse(
            local_path=local_path,
            repo_name=repo_name,
            branch=request.branch
        )
        
    except GitCommandError as e:
        raise HTTPException(
            status_code=400,
            detail=f"Failed to clone repository: {str(e)}"
        )
