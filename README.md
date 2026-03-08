# QueryMind

QueryMind is a local-first AI system for reasoning over arbitrary datasets.

The goal of the project is to build an AI assistant that can analyze unknown datasets by combining:

- local language models
- tool execution
- Python-based data analysis
- optional cloud LLM fallback

The system is designed to work **fully offline**, **hybrid**, or **cloud-assisted** depending on configuration.

## Core Idea

A user can provide a dataset and ask questions such as:

- "Which region has the highest revenue?"
- "Plot revenue by month"
- "Find anomalies in this dataset"

QueryMind uses a language model to plan actions and executes Python code on the dataset to compute results.

## High-Level Flow

User Question
→ Context Builder
→ LLM Reasoning
→ Tool Invocation (Python execution)
→ Result Returned
→ Final Explanation

## Project Structure

```
querymind/
├── src-server/      # Rust backend (Axum)
├── src-py-worker/   # Python execution engine
├── src-ui/          # UI
├── 01-docs/
└── 02-examples/
```

## Components

### Rust Server

The Rust server orchestrates the system:

- API endpoints
- context engineering
- LLM interaction
- tool execution
- communication with workers

Built using **Rust** and **Axum**.

### Python Worker

The Python worker performs dataset analysis using:

- pandas
- numpy
- plotting libraries

It receives execution requests from the Rust server.

## Goals

- fully local AI analysis
- support multiple LLM providers
- safe tool execution
- flexible dataset reasoning

## Status

Early development.

Initial focus:

1. Rust server skeleton
2. TCP communication with Python worker
3. basic LLM interaction
4. dataset execution loop
