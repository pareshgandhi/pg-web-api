from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import httpx

app = FastAPI()

GITHUB_API_URL = "https://api.github.com/users/{}/gists"


class Gist(BaseModel):
    id: str
    description: Optional[str]
    url: str


@app.get("/{username}", response_model=List[Gist])
async def get_gists(username: str,
                    page_num: int = Query(1, ge=1),
                    results_per_page: int = Query(10, ge=1, le=100)):
    """
    Get public gists for the given GitHub username (with pagination).

    :param username: GitHub username
    :param page_num: The page number
    :param results_per_page: Number of results per page, limited to 100
    :returns: List of Gists
    """

    async with httpx.AsyncClient() as client:
        url = GITHUB_API_URL.format(username)
        parameters = {"page": page_num, "per_page": results_per_page}
        response = await client.get(url, params=parameters)
        if response.status_code != 200:
            raise HTTPException(
                status_code=response.status_code,
                detail="User not found or error fetching gists"
            )

        gists = response.json()
        return [
            {
                "id": gist["id"],
                "description": gist["description"],
                "url": gist["html_url"]
            } for gist in gists
        ]
