# Week 5: Deploying Machine Learning Models

This week, I explored how to deploy a trained machine learning model and make it accessible for predictions. I learned how to load a saved model, serve predictions through an API, and package the application using Docker.

## Topics

- Loading serialized machine learning models with Pickle
- Generating predictions using `predict_proba()`
- Building prediction APIs with FastAPI
- Running applications with Uvicorn
- Managing dependencies with `uv` and lockfiles
- Containerizing applications with Docker

## Practical Work

Using the provided lead-scoring model, I explored how a trained model can be reused to predict the probability of a lead converting.

The deployment workflow covers:

- Loading the saved model from `pipeline.bin`
- Generating conversion probabilities for new lead data
- Running and testing the prediction API
- Inspecting the project dependencies and Docker configuration
- Building and running a Docker container

## Homework

The Week 5 homework focuses on deploying the provided lead-scoring model. The exercises cover environment setup, model predictions, API testing, Docker configuration, and containerized deployment.

## Setup and Usage

### Prerequisites

- Python 3.11
- [uv](https://docs.astral.sh/uv/)
- [Docker](https://docs.docker.com/) (optional, for containerized deployment)

### 1. Clone the repository

```bash
git clone <https://github.com/giftyhealthtech/ml-zoomcamp-2026>
cd <05-deployment>
```

Navigate to the Week 5 homework directory.

### 2. Install dependencies

```bash
uv sync --locked
```

### 3. Run the prediction API

```bash
uv run uvicorn predict:app --host 0.0.0.0 --port 9696
```

Check the health endpoint:

```bash
curl http://localhost:9696/health
```

Send a prediction request to the /predict endpoint using a JSON payload containing the lead's features.

The API returns a conversion probability and a boolean conversion prediction.

### 4. Run with Docker (optional)

Build the Docker image:

```bash
docker build -t zoomcamp-model:2026-hw5 .
```

Run the container:

```bash
docker run --rm -p 9696:9696 zoomcamp-model:2026-hw5
```

Ensure Docker is installed and running before executing these commands.

## Key Things I Learned

- A trained model can be saved and reused for predictions without retraining it.
- `predict_proba()` provides class probabilities that help estimate the likelihood of an outcome.
- APIs make machine learning models accessible to other applications.
- Dependency lockfiles support reproducible environments.
- Docker packages an application and its environment to simplify deployment.

## Acknowledgements

Thanks to [DataTalksClub](https://github.com/DataTalksClub) for the Machine Learning Zoomcamp curriculum and practical exercises.

Course repository: https://github.com/DataTalksClub/machine-learning-zoomcamp