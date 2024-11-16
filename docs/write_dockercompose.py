DOCKERCOMPOSE_API_DB = """version: "3.9"

services:
  flask_app:
    container_name: flask_app
    image: flask_app
    build: .
    ports:
      - "5000:5000"
    environment:
      - POSTGRES_URL=${POSTGRES_URL}
    depends_on:
      - postgres_db

  postgres_db:
    container_name: postgres_db
    image: postgres:12
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_DB=${POSTGRES_DB}
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata: {}
"""