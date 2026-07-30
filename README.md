# VectorCraft AI - Enterprise RAG & Intelligent Document Search

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-19.0-61DAFB?logo=react&logoColor=black)](https://react.dev/)
[![Azure AI Search](https://img.shields.io/badge/Azure-AI%20Search-0078D4?logo=microsoftazure&logoColor=white)](https://azure.microsoft.com/products/ai-services/ai-search)
[![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-0078D4?logo=openai&logoColor=white)](https://azure.microsoft.com/products/ai-services/openai-service)

---

### 👑 Project Ownership & Leadership
* **Founder & Lead Architect**: **Vivek Mara**
* **GitHub Repository**: [VivekMara2 / VectorCraft](https://github.com/VivekMara2/VectorCraft)
* **License**: MIT License (`Copyright (c) 2026 Vivek Mara`)

---

## 📌 Project Overview

**VectorCraft AI** is an enterprise-grade Retrieval-Augmented Generation (RAG) platform created by **Vivek Mara**. It provides a modern, ChatGPT-like intelligent interface over custom domain data and enterprise documents by pairing **Azure OpenAI (GPT-4o / GPT models)** with **Azure AI Search** for hybrid vector indexing and retrieval.

---

## 🚀 Key Features

* **💬 Multi-Turn RAG Chat**: Interactive conversational interface with prompt-rewriting and history memory.
* **📚 Citation & Thought Process**: Verifiable inline citations and transparent step-by-step model reasoning.
* **🔍 Hybrid Vector & Keyword Search**: High-relevance document indexing using Azure AI Search integrated vectorization.
* **📄 Multi-Format Ingestion**: Ingest PDF, CSV, Word, HTML, JSON, TXT, and Markdown files.
* **🖼️ Multimodal AI Support**: Analyze image-heavy documents and diagrams using vision-enabled models.
* **🔐 Enterprise Access Control (ACL)**: Document-level security and authentication integrated with Microsoft Entra ID.
* **📊 Evaluation & Telemetry**: Quantitative RAG evaluation toolsets and Application Insights monitoring.

---

## 🛠️ Architecture & Tech Stack

* **Frontend**: React 19, TypeScript, Fluent UI components, Vite, i18next localization.
* **Backend**: Python 3.10+ with Quart (async web framework), Azure OpenAI SDK, Azure Search SDK.
* **Infrastructure & Bicep**: Automated provisioning via Azure Developer CLI (`azd`), Azure Container Apps, Azure Blob Storage.

```
+-------------------+      +-------------------+      +----------------------+
|   React Frontend  | ---> |  Python Backend   | ---> |  Azure OpenAI GPT    |
| (VectorCraft UI)  | <--- |  (Quart RAG API)  | <--- | (Query & Generation) |
+-------------------+      +-------------------+      +----------------------+
                                     |
                                     v
                           +-------------------+
                           |  Azure AI Search  |
                           | (Vector Indexing) |
                           +-------------------+
```

---

## ⚡ Getting Started

### Prerequisites

* [Azure Developer CLI (`azd`)](https://aka.ms/azure-dev/install)
* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js 22+](https://nodejs.org/)
* [PowerShell 7+](https://github.com/powershell/powershell) or Bash

### Local Development Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/VivekMara2/VectorCraft.git
   cd VectorCraft
   ```

2. **Start the application locally**:
   ```bash
   # Windows PowerShell
   $env:PORT = 50505
   ./app/start.ps1

   # Linux / macOS
   PORT=50505 ./app/start.sh
   ```

3. **Open in browser**:
   Navigate to `http://127.0.0.1:50505` to interact with **VectorCraft AI**.

---

## ☁️ Deployment

Deploy both infrastructure and code using the Azure Developer CLI:

```bash
# Login to Azure
azd auth login

# Provision resources and deploy app
azd up
```

For subsequent backend or frontend code changes, deploy instantly with:
```bash
azd deploy
```

---

## 📖 Documentation & Guidelines

* [Developer Guidelines (`AGENTS.md`)](AGENTS.md)
* [Data Ingestion Guide](docs/data_ingestion.md)
* [Local Development Guide](docs/localdev.md)
* [Security & Access Control](docs/login_and_acl.md)

---

## 👤 Author & Maintainer

Developed and maintained by **Vivek Mara**.  
Official Repository: [https://github.com/VivekMara2/VectorCraft](https://github.com/VivekMara2/VectorCraft)  
For inquiries, issues, or contributions, please refer to [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
