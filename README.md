# Microservices with Docker & Kubernetes

## Overview
This project demonstrates a simple microservices architecture using Python (Flask), Docker, and Kubernetes. It consists of two independent services that communicate with each other and are orchestrated using Kubernetes.

---

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Testing](#testing)
- [CI/CD Pipeline](#cicd-pipeline)
- [Example Output](#example-output)
- [Authors](#authors)
- [License](#license)

---


## Project Structure
```
requirements.txt
k8s/
  service.yaml
  service1-deployment.yaml
  service2-deployement.yaml
service1/
  app.py
  Dockerfile
  test_app.py
service2/
  app.py
  Dockerfile
  test_app.py
```

---

## Getting Started

### Prerequisites
- Docker Desktop with Kubernetes enabled (or Minikube)
- kubectl

### 1. Build Docker Images
```powershell
copy requirements.txt service1\
copy requirements.txt service2\
docker build -t service1:latest .\service1
docker build -t service2:latest .\service2
```

### 2. Deploy to Kubernetes
```powershell
kubectl apply -f .\k8s\
```

### 3. Check Status
```powershell
kubectl get pods
kubectl get services
```

---

## Testing

### Manual Testing
1. Port-forward a service to your local machine:
   ```powershell
   kubectl port-forward service/service1 8080:80
   ```
2. Access `http://localhost:8080/` in your browser or with curl/Postman.
3. Test `/call-service2` endpoint for inter-service communication.

### Automated Testing (CI/CD)
Unit tests are provided for both services using `pytest`. These are run automatically in the CI/CD pipeline.
To run locally:
```powershell
pip install pytest
pytest service1/test_app.py
pytest service2/test_app.py
```

---

## CI/CD Pipeline

This project includes a GitHub Actions workflow for CI/CD automation:
- **Build & Lint:** Installs dependencies and lints Python code with flake8.
- **Automated Testing:** Runs pytest-based unit tests for both services.
- **Docker Build & Push:** Builds Docker images for both services and pushes them to Docker Hub (configure your Docker Hub credentials as repository secrets: `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`).
- **Deploy:** Placeholder for automated deployment to a cloud Kubernetes cluster (add your `kubectl` commands as needed).

Workflow file: `.github/workflows/ci-cd.yml`

---

- Managed dependencies with a shared `requirements.txt`
- Automated deployment and scaling with Kubernetes Deployments and Services
- Inter-service communication within the cluster



## Example Output
![Kubernetes Services Screenshot] (screenshots/<img width="761" height="223" alt="Screenshot 2025-07-23 193730" src="https://github.com/user-attachments/assets/523b9706-6a94-4a5f-8305-a3a1c2eedf3f" />
.png)

## Authors
- Pallapothu Yegneswar Guptha

## License
This project is licensed under the MIT License.
