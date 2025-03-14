from pydantic import BaseModel, HttpUrl

class RepoRequest(BaseModel):
    url: HttpUrl
    branch: str | None = None

class RepoResponse(BaseModel):
    local_path: str
    repo_name: str
    branch: str | None = None
