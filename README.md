# Flask ML API for Predicting Kubernetes Cluster Failures

This project is an AI-powered Flask API that predicts and helps remediate Kubernetes cluster failures. It leverages a trained TensorFlow ML model to provide predictions based on input cluster metrics, ensuring optimal performance and minimal downtime.

---

## Features

- REST API for ML-based predictions.
- Dockerized for seamless deployment.
- Compatible with Kubernetes (`kind`) clusters for testing.

---

## Installation

1. Clone the repository:
   git clone https://github.com/sharmishta173/kubernetes_failures.devtrails.git
   cd flask_project
2. Install dependencies:
pip install -r requirements.txt
Add the trained ML model file (model.h5) to the project directory.
3. Usage
Run Locally
Start the Flask API server:

python app.py
Send a prediction request to the API:

curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{"data": [0.5, 0.7, 1.2, 0.3]}'
Run with Docker
Build the Docker image:

docker build -t flask-ml-api .
Run the Docker container:

docker run -p 5000:5000 flask-ml-api
File Structure
.
├── app.py                 # Flask API logic
├── model.h5               # Pre-trained TensorFlow model
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker configuration
├── kind-config.yaml       # KIND cluster configuration
└── README.md              # Project documentation
Future Improvements
Add Kubernetes remediation capabilities.

Extend the ML model for more complex predictions.

Real-time metrics monitoring for Kubernetes clusters.

Contributing
Contributions are welcome! Fork this repository, make your changes, and submit a pull request.

License
This project is licensed under the MIT License. See LICENSE for details.

Contact
GitHub: sharmishta173
Email: thamminenisharmishta21@gmail.com
