# 🩺 Nova Clinical Companion

**An autonomous, multimodal AI assistant for modern healthcare workflows.**
*Built for the 2026 Amazon Nova AI Hackathon.*

## 📖 Overview
The Nova Clinical Companion is a modular, agentic web application designed to eliminate administrative friction for clinicians and lab technicians. By bridging the gap between raw medical observations and structured data entry, this system allows healthcare professionals to focus entirely on their work while the AI handles the administrative overhead.

Built entirely on AWS utilizing the Amazon Nova foundation models, this application integrates four core capabilities:

* **🗣️ Voice AI (Nova 2 Sonic):** A real-time, hands-free conversational interface for dictating clinical notes and querying patient history without breaking sterility.
* **🧠 Agentic Reasoning (Nova 2 Lite):** The central orchestration layer. It processes unstructured dictations, cross-references medical guidelines, and structures the data.
* **👁️ Multimodal Understanding (Nova Embeddings):** A vector database that ingests dense clinical trial PDFs and medical imagery, allowing operators to semantically search complex literature on the fly.
* **⚙️ UI Automation (Nova Act):** A headless browser agent that takes the structured data from the Nova Lite agent and automatically navigates and fills out mock Electronic Health Record (EHR) web portals.

## 🛠️ Tech Stack
* **Frontend:** Next.js / React (TailwindCSS)
* **Backend:** FastAPI (Python), LangChain / Strands Agents
* **Infrastructure & AI:** AWS SDK (Boto3), Amazon Nova (2 Lite, 2 Sonic, Multimodal Embeddings, Act)
