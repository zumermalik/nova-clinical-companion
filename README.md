# Nova Clinical Companion

A generative AI application built on AWS utilizing the Amazon Nova foundation model portfolio. This project serves as a proof-of-concept for automating clinical administrative workflows, including voice dictation, agentic data structuring, and Electronic Health Record (EHR) synchronization.

`Built for the 2026 Amazon Nova AI Hackathon.`

## System Architecture

The application implements a microservices architecture, separating a Next.js frontend client from a FastAPI backend that handles AWS Bedrock orchestration. The system leverages four distinct Amazon Nova capabilities:

* **`Voice Interface (Nova 2 Sonic):`** Processes real-time clinical dictation, converting raw audio input into clinical text.
* **`Agentic Reasoning (Nova 2 Lite):`** Acts as the core orchestration layer. It parses unstructured clinical narratives and extracts key medical entities (patient demographics, symptoms, dosages) into structured JSON formats.
* **`Multimodal Analysis (Nova Vision / Embeddings):`** Facilitates the ingestion and semantic analysis of medical literature (PDFs) and clinical imagery.
* **`UI Automation (Nova Act):`** Orchestrates headless browser agents to automatically map and push structured data payloads into target EHR web portals.

## Technology Stack

* **`Frontend:`** Next.js (React), Tailwind CSS, Axios
* **`Backend:`** FastAPI (Python), Uvicorn, Pydantic
* **`Cloud Infrastructure:`** AWS SDK (Boto3), Amazon Bedrock

## Prerequisites

* Node.js (v18 or higher)
* Python (v3.10 or higher)
* AWS Account with programmatic access and Bedrock model access granted for the Amazon Nova suite.

## Installation & Deployment

### 1. Repository Setup
Clone the repository and navigate to the project root:
```bash
git clone https://github.com/zumermalik/nova-clinical-companion.git
cd nova-clinical-companion
```

### 2. Environment Configuration
Create a `.env` file in the root directory to store your AWS credentials. Do not commit this file to version control.
```env
AWS_ACCESS_KEY_ID="your_aws_access_key"
AWS_SECRET_ACCESS_KEY="your_aws_secret_key"
AWS_REGION="us-east-1" 
```
*(Note: Ensure your selected AWS region supports the required Nova models via Amazon Bedrock).*

### 3. Backend Initialization
Initialize the Python environment and start the FastAPI server:
```bash
pip install -r backend/requirements.txt
uvicorn backend.main:app --reload --port 8000
```
The backend API documentation (Swagger UI) will be accessible at `http://localhost:8000/docs`.

### 4. Frontend Initialization
In a separate terminal session, initialize the Next.js application:
```bash
cd frontend
npm install
npm run dev
```
The application interface will be accessible at `http://localhost:3000`.

## Project Status & Testing
This project includes a simulated API mode for demonstration purposes in environments where active AWS Bedrock connections are restricted or rate-limited. To toggle between live inference and simulation mode, adjust the routing logic within `frontend/src/app/page.tsx`.
