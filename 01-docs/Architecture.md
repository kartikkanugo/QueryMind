# QueryMind Architecture

QueryMind is structured as a modular system where the Rust server orchestrates reasoning and delegates computation to specialized components.

## System Overview

```
User Interface
      │
      ▼
Rust Server (Axum)
      │
Context Engineering
      │
LLM Provider Layer
      │
Tool Execution Layer
      │
TCP Communication
      │
Python Worker
      │
Dataset Analysis
```

## Components

### 1. User Interface

The UI provides a simple interface for:

- asking questions
- uploading datasets
- viewing results and plots

The UI communicates with the Rust server over HTTP.

### 2. Rust Server

The Rust server acts as the **central orchestration layer**.

Responsibilities:

- API routing
- conversation management
- prompt construction
- model interaction
- tool execution coordination

### 3. LLM Provider Layer

QueryMind supports multiple model providers.

Examples:

- local models (LLaMA)
- cloud models (GPT APIs)

The interface abstracts model interaction so that the same context can be used across providers.

### 4. Tool Execution Layer

When the LLM determines that computation is required, it can invoke a tool.

Example tools:

- Python dataset execution
- plotting
- statistics

### 5. Python Worker

The Python worker is responsible for executing data operations.

Capabilities include:

- loading datasets
- executing generated Python code
- generating visualizations
- returning structured results

Libraries expected to be used:

- pandas
- numpy
- matplotlib

### 6. TCP Communication

The Rust server communicates with the Python worker through TCP messages.

Example request:

```
execute_python:
    code: df.groupby("region").sum()
```

Example response:

```
status: ok
result: {...}
```

## Execution Loop

Typical flow:

1. User asks a question.
2. Rust server builds context.
3. LLM generates a response or tool request.
4. Tool request triggers Python execution.
5. Result returned to LLM.
6. LLM generates final explanation.

## Design Principles

- local-first architecture
- modular components
- language-agnostic tool execution
- clear separation of orchestration and computation
