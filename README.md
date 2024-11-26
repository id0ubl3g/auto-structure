<div align="center">
    <img src=".github/crane-logo.png" alt="Crane Logo" width="130">
    <h1><b>Auto Structure</b></h1>
    <p>Flexible Flask API structures for any project, inspired by Vite.</p>
    <p>
        <img src="https://img.shields.io/github/last-commit/id0ubl3g/auto-structure?style=flat&logo=git&logoColor=white&color=0080ff" alt="Last Commit">
        <img src="https://img.shields.io/github/languages/top/id0ubl3g/auto-structure?style=flat&color=0080ff" alt="Top Language">
        <img src="https://img.shields.io/github/languages/count/id0ubl3g/auto-structure?style=flat&color=0080ff" alt="Languages Count">
    </p>
</div>

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)  
    - [Steps to Set Up `venv`](#steps-to-set-up-venv)  
- [Getting Started](#getting-started)
- [Available Project Structures](#available-project-structures)
- [Base Structures](#base-structures)  
    - [1. Lightweight API](#1-lightweight-api)
        - [Notes Lightweight API](#notes-lightweight-api)  
    - [2. Extended API](#2-extended-api)  
        - [Notes Extended API](#notes-extended-api)  
- [Get Ready, Activate, Code!](#get-ready-activate-code)
- [License](#license)

## Overview

Auto Structure provides modular and extensible solutions for building scalable Python projects. Inspired by Vite, it emphasizes simplicity, performance, and clean architecture. This tool helps automate the process of setting up a clean and organized project structure for your Python applications.

## Project Structure

```plaintext
└── auto-structure/
    ├── .github/
    │   ├── crane-logo.png
    ├── src/
    │   ├── modules/
    │   │   └── create_structures.py
    │   ├── utils/
    │   │   ├── shared/
    │   │   │   └── shared.py
    │   │   ├── style_outputs.py
    │   │   └── system_utils.py
    ├── config/
    │   └── path.config.py
    ├── docs/
    │   ├── base_structures.py
    │   └── write_gitignore.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    └── run.py
```

## Prerequisites

Before using Auto Structure, ensure that Python's virtual environment (venv) is set up on your system.

### Steps to Set Up `venv`
To install the `python3-venv` package, run the following command:

```sh
sudo apt install python3-venv
```

Ensure Python 3 is installed. You can verify by running:
```sh
python3 --version
```

If Python 3 is not installed, you can install it using the following command:

```sh
sudo apt update
sudo apt install python3 python3-venv
```

For additional information on how to install Python on your system, visit the official Python website: [ Download Python](https://www.python.org/downloads/)

## Getting Started 

To create a new project with Auto Structure, use the following command:

```sh
python3 run.py -n project_name
```

Replace project_name with the desired name of your project. Auto Structure will generate a pre-configured directory structure based on your choice.

## Available Project Structures

Auto Structure currently supports two base structures:

- Lightweight API: Ideal for small applications or microservices.

- Extended API: Designed for more complex APIs, including database support.


## Base Structures

### 1. Lightweight API

This structure is suitable for lightweight APIs, ideal for microservices:

```plaintext
└── project_name/
    ├── src/
    │   ├── modules/
    │   ├── utils/
    │   │   └── shared/
    │   ├── temp/
    │   ├── logs/
    │   └── api/
    ├── tests/
    ├── config/
    └── docs/
```

#### Notes Lightweight API

- **Design Purpose**:
    - Although this structure is simple, it allows for easy expansion by adding more modules, utility functions, or API endpoints as the project grows.

    - Flexible for different types of Python projects. You can add or remove directories to fit your specific use case.

- **Installed Libraries**:
    - `Flask`: Lightweight web framework.
    - `flask-cors`: Middleware for Cross-Origin requests.
    - `flasgger`: Swagger integration for API documentation.
    - `gunicorn`: WSGI HTTP server for deploying your application.

### 2. Extended API

This structure is designed for more complex APIs with PostgreSQL database integration:

```plaintext
└── project_name/
    ├── app/
    │   ├── controllers/
    │   ├── services/
    │   ├── modules/
    │   ├── routes/
    │   ├── models/
    │   ├── views/
    │   │   └── handlers/
    │   ├── utils/
    │   │   └── shared/
    │   ├── temp/
    │   └── logs/
    ├── tests/
    ├── config/
    └── docs/
```

#### Notes Extended API

- **Design Purpose**:
    - Designed for APIs that require more robust database management.
    - Promotes a better structure for scalability and maintainability, especially when dealing with databases.

- **Installed Libraries**:
    - `Flask`: Lightweight web framework.
    - `flask-cors`: Middleware for Cross-Origin requests.
    - `flasgger`: Swagger integration for API documentation.
    - `gunicorn`: WSGI HTTP server for deploying your application.
    - `psycopg2-binary`: PostgreSQL database adapter for Python.
    - `Flask-SQLAlchemy`: SQL toolkit and ORM for database operations.

- **Included Folders**:
    - `controllers`: Encapsulates the business logic of the  - application.
    - `services`: Provides reusable functions or external integrations.
    - `routes`: Defines and organizes the API endpoints.
    - `models`: Manages database schemas and ORM logic.
    - `views/handlers`: Handles user interfaces or error responses.


## Get Ready, Activate, Code!

- **Virtual Environment**: It's highly recommended to use a virtual environment to manage your project dependencies and avoid conflicts with system-wide packages.

- **Automatic Dependency Installation**: Auto Structure will install all necessary dependencies when creating your project. However, if you need to install them manually, run the following:

    ```sh
    pip install -r requirements.txt
    ```

- **Activate Virtual Environment**: After creating the project, navigate to the project folder and activate the virtual environment:

    ```sh
    cd project_name
    source .venv/bin/activate
    ```

## License

This project is licensed under the terms of the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0). See the [LICENSE](./LICENSE) file for details.