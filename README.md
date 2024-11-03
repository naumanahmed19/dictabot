# Dictabot

## How to Run the Project

### Prerequisites

- Anaconda or Miniconda

### Installation

1. **Clone the repository:**

### Create a conda environment:

```sh
conda create --name dictabot python=3.8
```

### Activate the conda environment:

```sh
conda activate dictabot
```

### Install the dependencies:

```sh
pip install -r requirements.txt
```

## Running the Application

Ensure you are in the project directory.

```sh
uvicorn main:app --reload
```

Run the FastAPI server using uvicorn:

Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the application running.

## API Documentation

FastAPI automatically generates interactive API documentation. You can access it at the following URLs once the server is running:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Project Structure

```
dictabot/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── items.py
│   ├── main.py
│   └── dependencies.py
├── requirements.txt
└── README.md
```