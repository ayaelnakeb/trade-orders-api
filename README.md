## Trade Orders API


A simple FastAPI application that lets you create and retrieve trade orders. The project is containerized with Docker, deployed on AWS EC2, and uses a GitHub Actions pipeline for continuous integration and deployment (CI/CD).

## Features
**Create Orders:** POST /orders with details like symbol, price, quantity, and order type.

**List Orders:** GET /orders returns all previously submitted orders.

**Database:** Uses SQLite (or PostgreSQL) with SQLAlchemy models.

**Automated Tests:** A basic test suite ensures the core endpoints work correctly.

**CI/CD Pipeline:** GitHub Actions automatically runs tests on pull requests and deploys to AWS EC2 on merges to main.


## Technologies Used
FastAPI (Python web framework)

SQLAlchemy (ORM)

Docker (Containerization)

GitHub Actions (CI/CD)

AWS EC2 (Deployment)
