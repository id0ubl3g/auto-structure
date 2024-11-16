DOCKER_API = """FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN python -m venv .venv

RUN .venv/bin/pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD [".venv/bin/python", "run.py"]

"""

DOCKER_API_DB = """FROM python:3.10-slim-buster

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && pip install python-dotenv

EXPOSE 5000

CMD ["python", "run.py"]
"""