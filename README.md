# API-service-fastapi

<br>

## Contents:
- [Description](#description)
- [Technology](#technology)
- [Customization and startup](#customization-and-startup)
- [Testing the microservice](#testing-the-microservice)
<br>


## Description

Microservice for path search by ID element in hierarchical data structure.


## Technology

<details><summary>List</summary>

**Programming languages, libraries and modules:**

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)

**Framework, extensions and libraries:**

[![FastAPI](https://img.shields.io/badge/FastAPI-v0.115.2-blue?logo=FastAPI)](https://fastapi.tiangolo.com/)

</details>


## Customization and startup

1. Cloning a repository.
    ```bash
   git clone https://github.com/Ilya-kutylev/API-service-fastapi.git
   cd API-service-fastapi
   ```
2. Installing and updating package managers (pip, pipenv).
    ```bash
   pip install --upgrade pip \
   && pip install pipenv
    ```
3. Creating a virtual environment and installing dependencies.
    ```bash
   pipenv install
   pipenv shell
    ```
4. Customizing hierarchy data.

   - Make sure that the structure.json file with hierarchical data is in the root directory of the project.


5. Application startup.
    ```bash
   uvicorn app.main:app
    ```
   - It is possible to add parameters to specify the host and port if required.
    ```
   uvicorn app.main:app --host --port
    ```

### Launching a microservice via Docker

Make sure that Docker is installed and running on your computer before launching a microservice via Docker.

   - Create images and elevate containers.
   ```bash
   docker-compose up --build -d
   ```
   - To stop and delete containers, run the following command.
   ```bash
   docker-compose down
   ```


## Testing the microservice

To test the microservice, we will use the `pytest` framework. Follow the steps below to run the tests.

1. Installing the necessary dependencies.

   - Before running the tests, make sure all dependencies are installed. Run the following command:
   ```bash
   pipenv install Pipfile.lock
   ```
2. Running tests.

   - To run all the tests, run the command:
   ```bash
   pytest
   ```
   - For detailed output of passed and failed tests, include the -v flag in the command:
   ```bash
   pytest -v
   ```
   - To run a specific test, run the following command:
   ```bash
   pytest tests/test_main.py::<name_test>
   ```
   - You can use the `pytest-html` plugin to create a detailed HTML report of test execution:
   ```bash
   pytest --html=report.html
   ```
##