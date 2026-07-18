# 🩺 AI Health Report Analyzer
![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![React](https://img.shields.io/badge/React-19-blue)
![AWS](https://img.shields.io/badge/AWS-Deployed-orange)

## Overview

AI Health Report Analyzer is an AI-powered healthcare platform that enables users to upload medical reports, extract clinical information, generate AI-driven summaries, analyze health trends, and retrieve medicine information through an intelligent assistant.

The application combines OCR, NLP, LLMs, and modern web technologies to simplify medical report interpretation for both patients and healthcare professionals.
---

## 🚀 Features

### 🔐 Authentication & Authorization

* JWT-based authentication
* Role-based access control
* Patient and Doctor roles
* Secure API access using Bearer Tokens

### 📄 Medical Report Upload

* Upload PDF and image reports
* File validation and storage
* Report metadata management

### 🔍 Medical Report Extraction

* OCR-based text extraction
* PDF processing using PyMuPDF
* Image processing using Pytesseract

### 🧠 AI-Powered Report Analysis

* Medical entity extraction
* Patient-friendly summaries
* Doctor-oriented clinical summaries
* Abnormal value detection
* Health recommendations

### 📚 Report History

* Store processed reports
* Access previous analyses
* Retrieve historical medical information

### 📈 Health Trend Analysis

* Compare multiple reports
* Track health changes over time
* Visualize trends using charts

### 💬 AI Health Assistant

* Report-based question answering
* General health queries
* Interactive healthcare chatbot

### 💊 Medicine Lookup Service

* Local SQLite medicine database
* Cache-first medicine retrieval
* FastMCP-based Wikipedia integration
* Drug uses, side effects, interactions, and warnings

### 🔔 Notification Service

* Analysis notifications
* Health alerts
* Read/unread notification tracking

---

# 🏗️ System Architecture

```text
Frontend (React + Tailwind CSS)
                    ↓
               FastAPI Backend
                    ↓
 ┌──────────────────────────────────────┐
 │                                      │
 ▼                                      ▼
Authentication Service          Upload Service
                                        │
                                        ▼
                              Extraction Service
                                        │
                                        ▼
                                  NLP Service
                                        │
                                        ▼
                               Summary Service
                                        │
                                        ▼
                                History Service
                                        │
                                        ▼
                              Trend Analysis
                                        │
                                        ▼
                               Chat Service
                                        │
                                        ▼
                          Medicine Lookup Service
                                        │
                      ┌─────────────────┴─────────────────┐
                      ▼                                   ▼
                SQLite Database                   Wikipedia MCP
                                                        │
                                                        ▼
                                                  Groq LLM
```

---

# 🛠️ Backend Technology Stack

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| FastAPI       | Backend Framework            |
| Python        | Programming Language         |
| SQLite        | Database                     |
| JWT           | Authentication               |
| PyMuPDF       | PDF Processing               |
| Pytesseract   | OCR                          |
| Groq LLM      | AI Processing                |
| FastMCP       | MCP Framework                |
| Wikipedia MCP | External Knowledge Retrieval |
| Uvicorn       | ASGI Server                  |
| Swagger UI    | API Testing                  |

---

# 🎨 Frontend Technology Stack

| Technology   | Purpose            |
| ------------ | ------------------ |
| React.js 19  | Frontend Framework |
| Vite         | Build Tool         |
| Tailwind CSS | Styling            |
| Axios        | API Communication  |
| Recharts     | Data Visualization |
| Lucide React | Icons              |

---

# 🗄️ Database Tables

* Users
* Uploads
* Report History
* Chat History
* Medicines
* Notifications

---

# 👥 User Roles

## Patient

* Upload medical reports
* View report summaries
* Track health trends
* Use AI Health Assistant
* Search medicine information

## Doctor

* Review patient reports
* Access clinical summaries
* Analyze abnormal values
* View historical records

---

# 🤖 FastMCP Integration

The Medicine Lookup Service follows a cache-first architecture:

```text
User Search
     ↓
SQLite Database
     ↓ Found
Return Result

     ↓ Not Found
Wikipedia MCP Server
     ↓
Wikipedia Knowledge
     ↓
Groq LLM Processing
     ↓
Save to SQLite
     ↓
Return Structured Response
```

This approach improves performance by caching medicine information locally after the first retrieval.

---

# 📁 Project Structure

```text
medlens-ai/
│
├── backend/
│   ├── backendservices/
│   │   ├── auth_service/
│   │   ├── upload_service/
│   │   ├── extraction_service/
│   │   ├── nlp_service/
│   │   ├── summary_service/
│   │   ├── history_service/
│   │   ├── trend_service/
│   │   ├── chat_service/
│   │   ├── medicine_service/
│   │   └── notification_service/
│   ├── database.py
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── assets/
│
└── README.md
```

---

#  Testing Tools

* Swagger UI
* Postman
* Browser-based Testing
* End-to-End Integration Testing

# Deployment

MedLens AI is deployed on Amazon Web Services (AWS) using an Amazon EC2 Ubuntu instance. The application follows a client-server architecture where the React frontend is served through Nginx and communicates with the FastAPI backend via REST APIs.

Deployment Architecture Users │ ▼ Nginx (Web Server) │ ▼ React Frontend (Production Build) │ ▼ REST APIs │ ▼ FastAPI + Uvicorn │ ├── SQLite Database ├── PyMuPDF & Tesseract OCR ├── Groq LLM ├── FastMCP (Wikipedia MCP) └── Medical Report Uploads

AWS Services Used

Amazon EC2 (Ubuntu) – Hosts the FastAPI backend and React frontend. Nginx – Serves the React production build and forwards API requests. Uvicorn – ASGI server used to run the FastAPI application. CloudWatch – Used for application monitoring and log management. Terraform – Used during infrastructure setup and provisioning.

Deployment Workflow

Build the React frontend using npm run build. Copy the production build to the EC2 server. Configure Nginx to serve the frontend. Run the FastAPI backend using Uvicorn. Configure Security Groups to allow HTTP traffic. Access the application through the EC2 public IP.

Live Application

Frontend: http://98.93.68.141

Backend API (Swagger): http://98.93.68.141:8000/docs

## Installation

### Clone the repository

git clone https://github.com/kavyashankarskkc0625/AI-Health-Report-Analyzer.git

cd AI-Health-Report-Analyzer

cd backend
pip install -r requirements.txt
uvicorn main:app --reload

cd frontend
npm install
npm run dev

## Future Enhancements

- Multi-language medical report analysis
- Doctor appointment integration
- Medical image analysis
- Prescription reminders
- Mobile application

## Author

**Kavya S**

- GitHub: https://github.com/kavyashankarskkc0625

## License

This project is licensed under the MIT License.

