# Intelligent Approval System (LangGraph Agentic Workflow)

A production-grade **multi-agent AI system** for automating marketing approvals using LangGraph, Groq LLMs, and Streamlit.

---

## Overview

This system simulates a real-world approval pipeline:

- Marketing Review
- Brand Review
- Compliance Review
- Final Decision Aggregation

All powered by **parallel AI agents**.

---

## ⚡ Key Features

### 🤖 Multi-Agent Architecture
- Marketing, Brand, Compliance agents
- Independent decision-making
- Final aggregation logic

### ⚡ Async Execution (LangGraph)
- Parallel agent execution
- Faster response times

###  LLM Stack (Groq)
- `openai/oss-120b` → Primary reasoning model  
- `llama3-8b-8192` → Fast fallback model  

### 🔁 Reliability
- Retry mechanism (Tenacity)
- Automatic fallback between models

### 💾 Memory (SQLite)
- Stores past approvals
- Tracks decisions over time

### 📊 Analytics Dashboard
- Decision distribution
- Historical trends
- Recent approvals

### 🧑 Human-in-the-Loop
- Manual override capability in UI

### 🎨 UI
- Built with Streamlit
- dashboard + metrics + tables

---

## 🏗️ Architecture
User Input
↓
Coordinator Agent
↓
Parallel Execution
├── Marketing Agent
├── Brand Agent
├── Compliance Agent
↓
Summary Agent
↓
Memory Store (SQLite)
↓
Analytics Dashboard



---

## 📂 Project Structure

approval-system/
│
├── app.py # Streamlit UI + Analytics
├── graph.py # LangGraph async workflow
├── agents.py # Agent logic
├── models.py # Pydantic schemas
├── llm.py # Groq LLM wrapper
├── memory.py # SQLite memory layer
├── utils.py # Helpers + pandas
├── config.py # API config
├── requirements.txt
└── README.md

🧑‍💻 How to Use the App
🚀 Step 1: Open the App
Run locally or open deployed Streamlit link
✍️ Step 2: Enter Marketing Content

Paste any marketing text, for example:

Our AI guarantees faster approvals and ensures compliance across all teams.
⚡ Step 3: Click "Run"
The system will:
Extract structured information
Run 3 AI agents in parallel
Generate review decisions
📊 Step 4: View Results

You will see:

✅ Overall Decision
Approved / Changes Required
📋 Detailed Table
Marketing Review
Brand Review
Compliance Review
🔍 Recommendations
Suggested improvements
Required changes
🧑 Step 5: Human Override
You can manually override the final decision:
Approved
Changes Required
💾 Step 6: Automatic Storage

Every run is saved in the system:

Input text
AI output
Final decision
Timestamp
📊 Step 7: View Analytics Tab

Switch to Analytics tab to see:

📈 Decision distribution
🧾 Historical approvals
🕒 Recent activity
🔥 Example
Input
Our AI guarantees 100% compliance and faster approvals.
Output
Overall Decision: Changes Required

Compliance Issues:
- Remove "guarantees"
- Add disclaimer for AI claims
