# ClearHire — AI Interview Integrity Analyzer

An AI-powered backend API that analyzes interview responses for behavioral signals of deception.

## Features
- Filler word detection
- Hedging language detection
- Contradiction detection
- Response length scoring
- Confidence score (0-100)
- Deception likelihood score
- Risk level — Low / Medium / High

## Tech Stack
- Python 3.13
- FastAPI
- Pydantic

## How to Run
1. Clone the repo
2. Create virtual environment: `python -m venv venv`
3. Activate it on Windows: `venv\\Scripts\\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the development server: `uvicorn main:app --reload`
6. Open the interactive API docs: `http://127.0.0.1:8000/docs`

## API Endpoints
- `GET /` — Health check
- `POST /analyze` — Analyze an interview response

## Example API Request

Use the interactive Swagger UI at `/docs` to inspect the exact request schema for `POST /analyze` and try a request with your own sample response.

## Interpreting Results

The API reports behavioral language signals such as filler words, hedging, contradictions, response length, and risk-related scores. These are indicators for further review—not proof that a person is deceptive. Results should be interpreted with context and should not be used as the sole basis for hiring decisions.

## Live API
https://clearhire-v1-production.up.railway.app/docs
