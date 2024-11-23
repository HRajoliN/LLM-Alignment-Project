# LLM Alignment Assistant

## 🌟 Overview

**LLM Alignment Assistant** is an advanced tool designed to assist in aligning large language models (LLMs) with desired human values and objectives. This project offers a full-stack approach to training, fine-tuning, deploying, and monitoring LLMs using **Reinforcement Learning from Human Feedback (RLHF)**. The system also incorporates evaluation metrics to ensure ethical and effective use of language models. The assistant provides a user-friendly interface for exploring the alignment, visualization of training metrics, and deploying the system at scale using cloud-native technologies.

![✨ Architecture Diagram](assets/architecture_diagram.png)

## ✨ Key Features

- **🖥️ User-Friendly Web Interface**: A sleek, intuitive UI for interacting with the LLM and viewing alignment results.
- **📊 Interactive Training**: Train models using RLHF, with dynamic metrics displayed in real-time.
- **🛠️ Data Augmentation & Preprocessing**: Advanced preprocessing scripts, including tokenization, cleaning, and data augmentation using NLP techniques.
- **⚙️ Scalable Deployment**: Easy deployment via Docker and Kubernetes, with horizontal scaling capabilities.
- **🔍 Explainability & Monitoring**: Incorporates SHAP or LIME-based explainability features along with live monitoring dashboards.

## 🗂️ Project Structure

- **📁 app/**: Contains the UI and the backend logic of the web interface.
  - `ui.py`: Manages routes and interactions with the UI.
  - `static/`: Contains styles and JavaScript for an appealing UI.
  - `templates/`: HTML templates for rendering the web pages.
- **📁 data/**: Scripts and datasets for generating, downloading, and processing data.
- **📁 deployment/**: Docker, Kubernetes configurations, and Helm charts to manage deployments.
- **📁 src/**: Core functionality, including training, evaluation, and preprocessing scripts.
- **📁 tests/**: Unit and integration tests to ensure quality across the different components.

## 🛠️ Setup

### 📋 Prerequisites

- Python 3.8+
- Docker & Docker Compose
- Kubernetes (Minikube or any cloud provider)
- Node.js (for front-end enhancements)

### 🔧 Installation

1. **📥 Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/LLM-Alignment-Assistant.git
   cd LLM-Alignment-Assistant
   ```

2. **📦 Set Up the Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **📦 Install Node.js Dependencies** (optional for enhanced UI):
   ```bash
   cd app/static
   npm install
   ```

### 🚀 Running Locally

To run the application locally:

1. **🐳 Build Docker Image**:
   ```bash
   docker-compose up --build
   ```

2. **🌐 Access the UI**:
   Visit `http://localhost:5000` in your web browser.

## 📦 Deployment

### 🚢 Docker and Kubernetes

- **🐳 Docker**: A Dockerfile is provided for containerization.
- **☸️ Kubernetes**: Use the provided `deployment/kubernetes/deployment.yml` and `service.yml` files to deploy the app to a Kubernetes cluster.
- **📜 Helm Charts**: Helm charts are available in the `deployment/helm/` directory for easier reusability and scalability.

### 🔄 CI/CD Pipeline

A GitHub Actions workflow is included to automate building, testing, and deployment:

- **✅ Lint & Test**: Linting and unit tests are run at every pull request.
- **🐋 Docker Build & Push**: Docker images are built and pushed to Docker Hub.
- **☸️ Kubernetes Deployment**: Automatically deploy to the Kubernetes cluster upon merging.

## 🤖 Training and Fine-Tuning

### 💡 Reinforcement Learning from Human Feedback (RLHF)

The training module includes:
- **📊 Fine-Tuning**: Using the `training/fine_tuning.py` script, models can be fine-tuned on specific datasets.
- **🏆 Reward Models**: Implemented in `training/reward_model.py` for evaluating the appropriateness of responses.
- **🌐 Distributed Training**: Support for distributed training using `training/rlhf.py`.

### 🎛️ Hyperparameter Tuning

For hyperparameter tuning, **Optuna** has been integrated to provide automated exploration of the training parameters, ensuring optimal model performance.

## 🔄 Data Pipeline

- **🛠️ Data Augmentation**: Using advanced NLP techniques, including back-translation and embedding-based masking, available in `preprocessing/augmentation.py`.
- **✅ Validation**: Thorough validation scripts (`preprocess_data.py` and `validate_data.py`) to maintain data quality.
- **⚙️ Automation with Apache Airflow**: Data pipeline orchestration using Airflow, ensuring proper data flow between stages.

## 📈 Evaluation and Monitoring

- **📊 Metrics**: The `evaluation/metrics.py` script provides a detailed analysis of model performance, including bias detection and fairness metrics.
- **🛡️ Safety Testing**: Ethical AI assessments using `evaluation/safety_tests.py`.
- **📊 Dashboard**: Real-time monitoring with **Streamlit**, displaying key metrics, including training loss, accuracy, and reward trends.

## 🌐 Web Interface Improvements

- **🎨 Improved UI with TailwindCSS**: We've enhanced the CSS for modern and engaging aesthetics.
- **📈 Interactive Visualizations**: Added **Chart.js** visualizations to present alignment metrics in a clear, graphical format.
- **💬 Chatbot Integration**: A conversational UI element to interact directly with the trained LLM.

## 🧪 Testing

- **✅ Unit Tests**: Located in `tests/`, covering training, preprocessing, and evaluation.
- **🔄 Integration Tests**: End-to-end tests that simulate full pipeline execution.
- **🧪 Mock Testing**: Use of `pytest-mock` to simulate API calls and external integrations.

## 📊 Monitoring and Logging

- **📈 Monitoring**: Kubernetes monitoring using **Prometheus** and **Grafana**, with Horizontal Pod Autoscaling (HPA) for scalability.
- **🔍 Explainability**: SHAP and LIME explainability metrics are added to the evaluation process, providing insights into model behavior.
- **📜 Logging**: Centralized logging using **ELK Stack** (Elasticsearch, Logstash, Kibana).

## 🚀 Cloud Deployment Instructions (AWS)

To deploy the LLM Alignment Assistant on **AWS**, you can utilize **Elastic Kubernetes Service (EKS)** or **AWS Sagemaker** for model training:

1. **AWS Elastic Kubernetes Service (EKS)**:
   - Create an EKS cluster using AWS CLI or the console.
   - Apply the Kubernetes deployment files:
     ```bash
     kubectl apply -f deployment/kubernetes/deployment.yml
     kubectl apply -f deployment/kubernetes/service.yml
     ```
   - Configure the **Horizontal Pod Autoscaler (HPA)** to ensure scalability:
     ```bash
     kubectl apply -f deployment/kubernetes/hpa.yml
     ```

2. **AWS Sagemaker for Model Training**:
   - Modify the `training/fine_tuning.py` to integrate with AWS Sagemaker.
   - Use the Sagemaker Python SDK to launch a training job:
     ```python
     import sagemaker
     from sagemaker.pytorch import PyTorch

     role = "arn:aws:iam::your-account-id:role/service-role/AmazonSageMaker-ExecutionRole-2023"

     pytorch_estimator = PyTorch(
         entry_point='training/fine_tuning.py',
         role=role,
         instance_count=1,
         instance_type='ml.p2.xlarge',
         framework_version='1.8.0',
         py_version='py3'
     )

     pytorch_estimator.fit({'training': 's3://your-bucket-name/training-data'})
     ```
   - Ensure IAM roles and permissions are properly set for accessing **S3** and **Sagemaker**.


## 🚀 Future Work

- **🌍 Multi-Language Support**: Expand the LLM's training to support multiple languages.
- **⚖️ Ethical AI Enhancements**: Further enhance bias detection and mitigation techniques.
- **☁️ Cloud-Native Deployment**: Implement cloud services like **AWS SageMaker** for training at scale.

## 🤝 Getting Involved

Contributions are welcome! Feel free to submit issues, pull requests, or suggestions for new features. 

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## 📬 Contact

- **✉️ Email**: [amirsina.torfi@gmail.com](mailto:amirsina.torfi@gmail.com)
- **🌐 Website**: [Portfolio](https://astorfi.github.io)

---

<p align="center">Made with ❤️ by Amirsina Torfi</p>

