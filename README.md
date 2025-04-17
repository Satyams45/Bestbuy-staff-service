# Best Buy Staff-Service Microservice

This microservice handles CRUD operations for staff information using FastAPI.

## 📌 Features
- Add, retrieve, update, and delete staff records
- Fully RESTful API
- Dockerized and deployed on Azure AKS
- CI/CD with GitHub Actions

## 🚀 Endpoints
- GET `/staff` - Get all staff
- GET `/staff/{id}` - Get staff by ID
- POST `/staff` - Create new staff
- PUT `/staff/{id}` - Update staff
- DELETE `/staff/{id}` - Delete staff

## 🐳 Docker Image
[Docker Hub Image](https://hub.docker.com/r/satyams45/bestbuy-staff-service)

## 📦 Deployment
- Azure Kubernetes Service (AKS)
- LoadBalancer exposes the API publicly

## ⚙️ CI/CD
- GitHub Actions builds, tests, and pushes Docker image to Docker Hub

## 🧪 Issues Faced
- Needed to expose FastAPI on correct port for AKS
- Docker tag mismatch resolved with `latest` naming convention
