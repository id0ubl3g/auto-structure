# Auto Structure

## Overview
The Auto Structure is a modular and extensible framework for building scalable Python projects. Inspired by Vite, it emphasizes simplicity, performance, and clean architecture.

## Venv Prerequisites

Before using Auto Structure, ensure that Python's virtual environment (venv) is set up on your system.

### Steps to Set Up `venv`
To install the `python3-venv` package, run the following command:

```sh
sudo apt install python3-venv
```

## Getting Started 

### To create a new project with Auto Structure, use the following command:

```sh
python3 run.py -n project_name
```

Replace project name with the desired name of your project. Auto Structure will generate a pre-configured directory structure based on your requirements.

## Base Structures

### 1. Lightweight API

This structure is suitable for lightweight APIs without database integration:

```
project_name
├── src
│   ├── modules
│   ├── utils/shared
│   ├── temp
│   ├── logs
│   └── api
├── tests
├── config
└── docs
```

#### Notes Lightweight API

- Scalability: Although this structure is simple, it still allows for easy expansion by adding more modules, utility functions, or API endpoints as the project grows.

- Customizability: The structure is flexible and can be easily adapted to different types of Python projects. You can add or remove directories as necessary for your specific use case.

### 2. Extended API

This structure is designed for more complex APIs with database integration:

```
project_name
├── app
│   ├── controllers
│   ├── services
│   ├── modules
│   ├── routes
│   ├── models
│   ├── views/handlers
│   ├── utils/shared
│   ├── temp
│   └── logs
├── tests
├── config
└── docs
```

#### Notes Extended API

- The API with Database Integration structure includes additional folders (`controllers`, `services`,` models`, and `views/handlers`) to support database management and MVC-style architecture.

- Both structures ensure separation of concerns, making them easy to scale and maintain.

Use the appropriate structure based on your project complexity and requirements.

## Get Ready, Activate, Run!

- **Virtual Environment**: It's highly recommended to use a virtual environment to manage your project dependencies and avoid conflicts with system-wide packages.

- **Automatic Dependency Installation**: Auto Structure automatically installs all the necessary dependencies when you create your project, so there's no need for manual installation. Just navigate to the root directory of your project and run the setup command, and you're ready to go!<br>
To activate the virtual environment manually, use the following command:

    ```sh
    cd project_name
    source .venv/bin/activate
    ```