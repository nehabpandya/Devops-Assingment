ACEest_Fitness and Gym Application
This project is a foundational Flask web application for a fitness and gym management system. As part of a DevOps assignment, it demonstrates key practices including version control with Git, containerization with Docker, and automated CI/CD using GitHub Actions.

Project Overview
The application serves as a starting point for managing core functionalities relevant to a gym. It is built with Python and the Flask framework. The project is designed with an automated workflow that ensures every code change is thoroughly tested and can be deployed consistently.

Key features of the DevOps pipeline include:

Version Control: All code changes are managed using Git and hosted on GitHub.

Unit Testing: The application's core logic is validated using the Pytest framework.

Containerization: The entire application and its dependencies are packaged into a portable Docker container for environmental consistency.

CI/CD: A GitHub Actions workflow automatically builds the Docker image and runs the unit tests on every push to the main branch.

Getting Started Locally
To run this application on your local machine, follow these steps.

Prerequisites
Python 3.9+

pip (Python package installer)

Docker (for containerization)

Setup
Clone the Repository:

git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)
cd YOUR_REPOSITORY_NAME

Install Dependencies:
It is recommended to use a virtual environment.

pip install -r requirements.txt

Run the Application:
You can run the application directly or inside a Docker container.

Using Python:

python app.py

Using Docker:
First, build the Docker image:

docker build -t ace-fitness-app .

Then, run the container:

docker run -p 5000:5000 ace-fitness-app

The application will be accessible at http://localhost:5000.

Running Tests
Unit tests are written using Pytest. To run them locally and ensure the application's integrity, use the following command:

pytest

CI/CD Pipeline with GitHub Actions
A Continuous Integration/Continuous Delivery (CI/CD) pipeline is configured using GitHub Actions. This workflow is defined in .github/workflows/main.yml.

The pipeline triggers on every push to the main branch and performs the following automated tasks:

Build Docker Image: The Dockerfile is used to build a new Docker image of the application.

Run Tests: The Pytest unit tests are executed inside the newly built Docker container.

A successful workflow run confirms that the code is functional and stable before any further deployment steps. You can view the status of the pipeline under the "Actions" tab of this repository.

Author
Neha Pandya - https://github.com/nehabpandya/Devops-Assingment
