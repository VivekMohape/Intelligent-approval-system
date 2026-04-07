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
