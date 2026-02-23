# ExpenseTracker

A simple web-based expense tracking application built with Python Flask.

## Features
- Add expenses with title, amount, and category
- View all expenses in a table
- Delete individual expenses
- Filter expenses by category
- View total amount spent

## Tech Stack
- Backend: Python Flask
- Frontend: HTML, CSS, Vanilla JS
- Containerization: Docker
- CI/CD: GitHub Actions

## Running Locally
```bash
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## Running with Docker
```bash
docker pull yourusername/expense-tracker:latest
docker run -p 5000:5000 yourusername/expense-tracker:latest
```
Visit http://localhost:5000

## CI/CD Pipeline Stages
1. **Clone** – Checkout source code
2. **Build** – Install dependencies and verify build
3. **Docker** – Build and push image to DockerHub

## Project Structure
```
ExpenseTracker/
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── README.md
├── .github/workflows/ci.yml
└── templates/
    └── index.html
```