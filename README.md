# SummaLyzer: Advanced NLP-Powered Text Summarization Engine

## Project Overview
SummaLyzer is an end-to-end text summarization tool that leverages the power of advanced NLP techniques. Utilizing the Google Pegasus model, this Python-based solution is designed for efficient summarization of extensive texts, ensuring high accuracy and contextual relevance.

## Key Features
- **NLP-Driven Text Summarization**: Incorporates Google Pegasus for state-of-the-art summarization.
- **Full-Stack Development**: Comprehensive Python-based solution with a focus on modularity and scalability.
- **Data Pipeline Management**: Robust handling of data ingestion, validation, and transformation.
- **RESTful API**: FastAPI implementation for seamless interaction with the model.
- **CI/CD**: Integrated Continuous Integration and Deployment using GitHub Actions.
- **Containerization and Cloud Deployment**: Utilizes Docker and AWS services (EC2, ECR) for scalable and efficient deployment.

## Technologies Used
- **Languages**: Python
- **Machine Learning**: Google Pegasus
- **API**: FastAPI
- **Containerization**: Docker
- **Cloud**: AWS (EC2, ECR)
- **CI/CD**: GitHub Actions
- **Version Control**: Git, GitHub

## Getting Started
To get this project up and running on your local machine, follow these steps:

### Prerequisites
- Python 3.8
- Docker
- An AWS account

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/YourUsername/SummaLyzer.git
   ```
2. Navigate to the project directory:
   ```
   cd SummaLyzer
   ```
3. Create and activate a virtual environment:
   ```
   conda create -n summary python=3.8 -y
   conda activate summary
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Usage
Run the application:
```
python app.py
```
Access the API at `http://localhost:8080`.

## AWS CI/CD Deployment with GitHub Actions

### Initial AWS Setup
- **Accessing AWS**: Begin by logging into the AWS console.
- **IAM User Creation**: Set up a new IAM user designated for deployment processes.

### Access Privileges
- **EC2 Access**: Assign access to EC2, which serves as a virtual machine.
- **ECR Access**: Grant permissions to interact with Elastic Container Registry (ECR), crucial for storing Docker images.

### Deployment Steps
- **Image Creation**: Start by constructing a Docker image from your source code.
- **ECR Upload**: Next, upload this Docker image to your ECR.
- **EC2 Instance**: Proceed to initiate an EC2 instance.
- **ECR to EC2**: Retrieve your Docker image from ECR onto your EC2 instance.
- **Docker Launch**: Finally, launch the Docker image within the EC2 environment.

### Required Policies
- **AmazonEC2ContainerRegistryFullAccess**: Essential for comprehensive ECR interactions.
- **AmazonEC2FullAccess**: Provides unrestricted access to EC2 functionalities.

### Additional Setup Steps
- **ECR Repository**: Establish an ECR repository to house your Docker images, noting down the URI: 
- **EC2 Configuration**: Create an EC2 instance, preferably Ubuntu-based.

### Installing Docker on EC2
- **Optional Updates**: Run `sudo apt-get update -y` and `sudo apt-get upgrade`.
- **Essential Installations**:
   - Obtain Docker: `curl -fsSL https://get.docker.com -o get-docker.sh`.
   - Install Docker: `sudo sh get-docker.sh`.
   - Configure Docker permissions: `sudo usermod -aG docker ubuntu` and `newgrp docker`.

### EC2 as Self-Hosted Runner
- In GitHub, navigate through `Settings > Actions > Runners > New self-hosted runner` and follow the instructions for your OS.

### Setting Up GitHub Secrets
Configure the following secrets in your GitHub repository for seamless integration:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION` (e.g., us-east-1)
- `AWS_ECR_LOGIN_URI` (e.g., `566373416292.dkr.ecr.ap-south-1.amazonaws.com`)
- `ECR_REPOSITORY_NAME` (e.g., simple-app)

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/vbabua/Text-Summarization/blob/main/LICENSE) file for details.