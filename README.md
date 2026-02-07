# Applied AI Backend Service

A production-style backend service built with FastAPI that accepts raw text, performs sentiment analysis using a pretrained NLP model, and stores all requests and results in PostgreSQL.

This project is designed to demonstrate backend engineering skills with AI as a component, not as a research experiment.

---

## Problem Statement

Many AI demos focus on model accuracy or notebooks but ignore system concerns like persistence, observability, and API design.

This service focuses on the **end-to-end backend workflow**:
- Accept input via an HTTP API
- Perform AI inference
- Return structured output
- Persist results reliably
- Provide basic observability for debugging

---

## Architecture Overview

````
Client
|
| POST /analyze
v
FastAPI API Layer
|
|-- Input validation (Pydantic)
|-- Request ID middleware
|
v
Inference Service
|
|-- Pretrained sentiment model
|
v
PostgreSQL Database
|
|-- Stores input, output, metadata
````


Key design principle: **AI is treated as a replaceable component**, not the core system.

---

## Tech Stack

- **Language:** Python
- **API Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **AI Model:** Pretrained Hugging Face sentiment model
- **Environment Config:** dotenv
- **Observability:** Structured logging + request IDs

---

## API Usage

### Endpoint

`POST /analyze`

### Request Body

```json
{
  "text": "The app crashes and support never replies"
}
```

### Response

```json
{
  "sentiment": "negative",
  "confidence": 0.98
}
```
Each response includes an X-Request-ID header for tracing.

## Data Model

`analyses` Table

```
| Field      | Purpose                |
| ---------- | ---------------------- |
| id         | Primary key            |
| input_text | Original user input    |
| sentiment  | Model prediction       |
| confidence | Model confidence score |
| model_name | AI model identifier    |
| created_at | Timestamp              |

```
All requests are persisted to support auditing, debugging, and future analytics.

##

### AI Integration

1. Uses a pretrained sentiment analysis model

2. Model is loaded once at application startup

3. Inference is isolated in a dedicated service module

### Notes on Confidence

The confidence score reflects the model’s internal probability, not ground truth correctness. Results may vary on domain-specific or ambiguous inputs.

##

### Observability

1. Each request is assigned a unique request ID

2. Request IDs are:

    1. logged at request entry

    2. logged after inference

    3. returned in response headers

This enables request-level tracing and debugging in distributed systems.

##

### Known Limitations

1. Single-process inference (no background workers)

2. Cold-start latency due to model loading

3. No rate limiting or authentication

4. No database migrations (manual table creation)

These tradeoffs were made intentionally to keep the system focused and understandable.

##

### Future Improvements

1. Alembic migrations for schema evolution

2. Background inference workers

3. Rate limiting and authentication

4. Model versioning and A/B testing

5. Caching frequent requests

##

### Summary

This project demonstrates how to build a real backend service that integrates AI responsibly, with attention to architecture, persistence, and operational concerns.
