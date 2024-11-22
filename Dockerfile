FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "src.github_api_server:app", "--host", "0.0.0.0", "--port", "8080"]
