# GitHub Gists API

A simple API that interacts with the GitHub to return a list of a user's public gists, with pagination support.

## Setup

### Prerequisites
- Docker
- Docker compose
- Python 3.9+ (only for local development/testing)

### Installation

- Clone the repository

## If you want to develop/test locally
- Create virtual environment (either using pyenv or python3 -m venv)
- Activate the virtual environment
- Install dependencies
```bash
pip3 install -r requirements.txt
```

### Running with Docker

1. **Build docker image and start the Docker container**:
```bash
docker compose up -d --build
```

2. **Ensure that the docker container is up and running**:
```bash
docker compose ps
```
The status should be `Up`

3. **Following command should run various unit tests successfully**:
```bash
docker compose exec github-gists-api pytest tests/
```
   

4. Access the API at http://localhost:8080/octocat on your host machine.

   Note: This should return gists for the user `octocat`


### Running the API Locally

Ensure that the port 8080 is not in use. If in use then stop the service that has taken the port 8080.
```bash
docker compose down
```

Start the API with Uvicorn:
```bash
uvicorn src.github_api_server:app --host 0.0.0.0 --port 8080
```

Access the API at http://localhost:8080/octocat
Note: This should return gists for the user `octocat`


### Pagination

The API supports pagination with the following query parameters:

- **`page_num`** (default: 1): The page number of results to return.
- **`results_per_page`** (default: 10, max: 100): The number of gists to return per page.

http://localhost:8080/octocat?page_num=2&results_per_page=3

This returns the second page of gists for `octocat`, with up to 3 results per page.

### Running tests locally

Tests can also be run locally using command below:
```bash
pytest tests/
```

This should run various unit tests successfully.
