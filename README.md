# 🕸️ MeshApp – Python Microservice Demo for Istio Service Mesh

This project demonstrates a simple **3-tier Python microservice** architecture that:
- Runs locally via **Docker Compose**
- Deploys to **Kubernetes** with **Istio Service Mesh**
- Showcases **service-to-service communication**, **canary deployments**, and **observability**

---

## 🧱 Architecture

User
│
▼
Frontend (port 5001) → Backend (port 5002) → Reviews (port 5003)

yaml
Copy
Edit

- **Frontend**: Renders HTML UI and fetches data from backend  
- **Backend**: Communicates with `reviews` service and aggregates data  
- **Reviews**: Returns mock review JSON data

---

## 🚀 Getting Started – Local (Docker Compose)

### 1. Clone the repo

git clone https://github.com/sadesh123/meshapp.git
cd meshapp

shell
Copy
Edit

### 2. Build & Run the Services

docker-compose up --build


### 3. Access the App

Open in your browser:
http://localhost:5001

You’ll see a simple UI displaying review data.

---

## 🐳 Project Structure

microservice-MeshApp/
├── frontend/
│ └── app.py
├── backend/
│ └── app.py
├── reviews/
│ └── app.py
├── requirements.txt
├── docker-compose.yml
└── README.md


Each service is built using:
- Python Flask
- `requests` for HTTP calls

---

## 🚢 Deploying to Kubernetes + Istio

### 1. Start Minikube

minikube start --driver=docker


### 2. Install Istio and Enable Sidecar Injection

istioctl install --set profile=demo -y
kubectl label namespace default istio-injection=enabled --overwrite


### 3. Build Images into Minikube’s Docker

eval $(minikube docker-env)

docker build -t microservice-meshapp-backend:latest ./backend
docker build -t microservice-meshapp-frontend-v1:latest ./frontend-v1
docker build -t microservice-meshapp-frontend-v2:latest ./frontend-v2
docker build -t microservice-meshapp-reviews:latest ./reviews

minikube image load microservice-meshapp-backend:latest
minikube image load microservice-meshapp-frontend-v1:latest
minikube image load microservice-meshapp-frontend-v2:latest
minikube image load microservice-meshapp-reviews:latest


### 4. Deploy Microservices

kubectl apply -f k8s/backend.yaml
kubectl apply -f k8s/frontend-v1.yaml
kubectl apply -f k8s/frontend-v2.yaml
kubectl apply -f k8s/reviews.yaml

### 5. Apply Istio Routing

kubectl apply -f k8s/frontend-gateway.yaml
kubectl apply -f k8s/frontend-destinationrule.yaml
kubectl apply -f k8s/frontend-virtualservice.yaml

---

## 🌐 Accessing the App (Minikube)

### Option 1: Tunnel

minikube tunnel

Then visit:

http://127.0.0.1


Or check port using:

kubectl -n istio-system get svc istio-ingressgateway


If NodePort is exposed:

http://<minikube-ip>:<nodePort>


### Option 2: Port-Forward

kubectl -n istio-system port-forward svc/istio-ingressgateway 8080:80


Visit:
http://localhost:8080


---

## 🧪 Canary Routing

Traffic to `/` is split:
- 90% → `frontend-v1`
- 10% → `frontend-v2`

Customize this logic in `frontend-virtualservice.yaml` using:
- HTTP headers
- User-Agent
- Cookie
- Source IP

---

## 📦 Requirements

- Docker & Docker Compose
- Python 3.9+
- Minikube (or Kind, EKS, etc.)
- Istio CLI

---

## 📜 License

MIT

---

> Built for learning Istio, observability, and progressive delivery patterns.