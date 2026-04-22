# RAG Customer Support Bot

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system using LangChain, ChromaDB, and LangGraph.

## Features
- PDF-based knowledge retrieval
- Embedding storage using ChromaDB
- Context-aware answer generation
- Graph-based workflow using LangGraph
- Intent-based routing (FAQ vs Escalation)
- Human-in-the-Loop support

## Workflow
User Query → Intent Detection → (RAG OR Human Escalation) → Response

## Tech Stack
- Python
- LangChain
- LangGraph
- ChromaDB
- OpenAI

## Run Instructions
```bash
pip install -r requirements.txt
python app.py
