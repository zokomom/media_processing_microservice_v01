<div align="center">

# 🚀 Distributed Media Processing Microservice

### Asynchronous Media Processing Pipeline built with FastAPI, Celery, RabbitMQ, Redis, AWS S3, Docker & Prometheus

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-Message%20Broker-FF6600?style=for-the-badge&logo=rabbitmq)
![Redis](https://img.shields.io/badge/Redis-Job%20Store-DC382D?style=for-the-badge&logo=redis)
![AWS S3](https://img.shields.io/badge/AWS-S3-569A31?style=for-the-badge&logo=amazonaws)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?style=for-the-badge&logo=prometheus)

</div>

---

# 📌 Overview

This project is an asynchronous media processing microservice developed using **FastAPI** and **Celery**. Instead of processing uploaded media synchronously, incoming tasks are pushed into **RabbitMQ**, processed by Celery workers in the background, and stored securely in **AWS S3**.

The service supports both **image** and **video** processing while exposing REST APIs for uploading media, tracking processing jobs, and downloading processed assets using **pre-signed S3 URLs**.

The project is fully containerized using **Docker Compose** and monitored with **Prometheus**.

---

# ✨ Features

## Image Processing

- Upload JPEG & PNG images
- Automatic center cropping
- Resize images to 500 × 500 pixels
- Watermark processed images
- Store processed images in AWS S3
- Secure download of processed media using AWS S3 Pre-Signed URLs
---

## Video Processing

- Upload MP4 videos
- Compress videos using FFmpeg
- Generate video thumbnails
- Upload compressed videos to AWS S3
- Store thumbnails separately

---

## Background Processing

- Asynchronous task execution
- Celery Worker
- RabbitMQ Message Broker
- Retry mechanism on failures
- Non-blocking API responses

---

## Job Tracking

- Unique Job ID generation
- Processing status stored in Redis
- Job states

```
Queued
Processing
Completed
Failed
```

- Download processed files using Pre-Signed URLs

---

## Monitoring

- Prometheus Metrics
- FastAPI Request Metrics
- RabbitMQ Metrics
- CPU Usage
- Memory Usage
- Request Latency

---

## Deployment

- Dockerized Services
- Docker Compose
- Environment Variables
- AWS S3 Integration

---

# 🏗 Architecture

```mermaid
graph TD

A[Client]

A -->|Upload Media| B(FastAPI)

B -->|Store Original| C[(AWS S3)]

B -->|Create Job| D[(Redis)]

B -->|Publish Task| E[RabbitMQ]

E --> F[Celery Worker]

F --> G[Image Processing]

F --> H[Video Processing]

G --> I[(Processed Images)]

H --> J[(Compressed Videos)]

H --> K[(Video Thumbnails)]

I --> C

J --> C

K --> C

B -->|Check Job| D

B -->|Generate Pre-Signed URL| C

L[Prometheus]

L --> B

L --> E
```

---

# ⚙ Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python 3.10 |
| API Framework | FastAPI |
| Task Queue | Celery |
| Message Broker | RabbitMQ |
| Job Store | Redis |
| Cloud Storage | AWS S3 |
| Image Processing | Pillow |
| Video Processing | FFmpeg |
| Monitoring | Prometheus |
| Containerization | Docker |
| Orchestration | Docker Compose |
| Load Testing | Locust |

---

# 📂 Project Structure

```text
media_processing_microservice_v01
│
├── app
│   ├── routes
│   ├── services
│   ├── utils
│   ├── tasks.py
│   ├── celery_app.py
│   ├── config.py
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── prometheus.yml
├── requirements.txt
├── locustfile.py
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/zokomom/media_processing_microservice_v01.git
```

Go to project directory

```bash
cd media_processing_microservice_v01
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate

Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file

```env
AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY

AWS_REGION=ap-south-1

S3_BUCKET_NAME=atharv-media-storage

REDIS_URL=redis://redis:6379/1

RABBITMQ_URL=amqp://guest:guest@rabbitmq:5672//
```

---

# 🐳 Running with Docker

Build the project

```bash
docker compose build
```

Start all services

```bash
docker compose up
```

Stop services

```bash
docker compose down
```

The following containers will be started

| Service | Port |
|----------|------|
| FastAPI | 8000 |
| RabbitMQ | 15672 |
| Redis | 6379 |
| Prometheus | 9090 |
| Celery Worker | Internal |

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Health Check |
| POST | `/upload` | Upload Image or Video |
| GET | `/jobs/{job_id}` | Get Job Status |
| GET | `/metrics` | Prometheus Metrics |

---

# 🔄 Processing Workflow

```text
Client

   │

Upload Image / Video

   │

FastAPI

   │

Store Original File in AWS S3

   │

Create Job in Redis

   │

Publish Task to RabbitMQ

   │

Celery Worker

   │

Image / Video Processing

   │

Upload Processed Files to AWS S3

   │

Update Redis Job Status

   │

Generate Pre-Signed URL

   │

Client Downloads Processed File
```

---
# 📊 Monitoring

The project includes built-in monitoring using **Prometheus** to observe the health and performance of the microservice.

### Metrics Collected

- HTTP Request Count
- Request Latency
- Response Status Codes
- CPU Usage
- Memory Usage
- FastAPI Metrics
- RabbitMQ Metrics

### Access Prometheus

```
http://localhost:9090
```

### FastAPI Metrics Endpoint

```
http://localhost:8000/metrics
```

---

# ⚡ Load Testing

The application was load tested using **Locust** to validate API responsiveness under concurrent users.

## Configuration

| Parameter | Value |
|-----------|-------|
| Virtual Users | 50 |
| Spawn Rate | 5 users/sec |
| Duration | 5 Minutes |
| Host | http://localhost:8000 |

---

## Results

| Metric | Result |
|---------|---------|
| Total Requests | 9505 |
| Failures | 0 |
| Average Response Time | 6.43 ms |
| Median Response Time | 5 ms |
| 95th Percentile | 12 ms |
| Maximum Response Time | 527 ms |
| Requests per Second | ~34 |

The load test demonstrates that the API remains responsive under concurrent traffic while media processing is handled asynchronously by Celery workers.

---

# 📷 Project Screenshots

## Swagger API Documentation

<img src="images/swagger.png" width="900">

FastAPI automatically generates interactive API documentation using Swagger UI.

---

## Docker Containers

<img src="images/docker.png" width="900">

All project services are containerized using Docker Compose.

Running Containers:

- FastAPI API
- Celery Worker
- RabbitMQ
- Redis
- Prometheus

---

## Prometheus Monitoring

<img src="images/prometheus.png" width="900">

Prometheus continuously scrapes metrics from:

- FastAPI
- RabbitMQ

---

## AWS S3 Storage

<img src="images/s3.png" width="900">

Processed media is organized into separate folders.

```
uploads/
processed/
thumbnails/
```

---

## Locust Load Test

### Statistics

<img src="images/locust_stats.png" width="900">

---

### Charts

<img src="images/locust_charts.png" width="900">

The application handled over **9500 requests** during testing with **0 failures**, demonstrating stable performance under concurrent user load.

---

# 🔐 Security

The application follows several security best practices.

- AWS credentials stored using environment variables
- Sensitive files excluded using `.gitignore`
- Private S3 bucket
- Temporary files removed after processing
- Pre-Signed URLs used for secure downloads
- Docker environment isolation

---

# 🚀 Future Improvements

Some planned enhancements include:

- User Authentication (JWT)
- PostgreSQL Database Integration
- Object Detection using AI
- Image Classification
- Video Streaming Support
- Kubernetes Deployment
- CI/CD Pipeline using GitHub Actions
- Grafana Dashboard
- Email Notifications
- Auto Scaling Workers

---

# 💡 Challenges Faced

During development several real-world backend challenges were encountered and solved.

- Migrating from local file storage to AWS S3
- Handling asynchronous background processing
- Configuring RabbitMQ with Celery
- Managing Redis job states
- Fixing EXIF image rotation
- Docker networking configuration
- Prometheus integration
- Generating secure pre-signed URLs
- Processing large media files efficiently

These challenges provided practical experience with distributed backend systems and production-oriented development.

---

# 📖 Learning Outcomes

Through this project I gained practical experience with:

- Building REST APIs using FastAPI
- Designing asynchronous architectures
- Message Queues with RabbitMQ
- Background Tasks using Celery
- Redis as a Job Store
- AWS S3 Cloud Storage
- Docker Containerization
- Docker Compose
- Prometheus Monitoring
- Performance Testing with Locust
- Secure File Delivery using Pre-Signed URLs
- Distributed System Design

---

# 👨‍💻 Author

**Atharv Kumar**

Bachelor of Computer Applications (BCA)

Backend Developer | Python | FastAPI | AWS | Docker

GitHub

https://github.com/zokomom

---

# 🙏 Acknowledgements

This project was developed as part of an internship assignment to demonstrate the implementation of a distributed media processing system using modern backend technologies.

Special thanks to the open-source community behind:

- FastAPI
- Celery
- RabbitMQ
- Redis
- Docker
- Prometheus
- Pillow
- FFmpeg
- AWS

---

# ⭐ If you found this project useful

Please consider giving the repository a ⭐ on GitHub.

It helps support the project and encourages further improvements.

---

<div align="center">

### Thank you for visiting this repository ❤️

Made with Python, FastAPI, Docker and AWS.

</div>