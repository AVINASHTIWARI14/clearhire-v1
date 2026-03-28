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
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install fastapi uvicorn`
5. Run: `uvicorn main:app --reload`
6. Open: `http://127.0.0.1:8000/docs`

## API Endpoints
- `GET /` — Health check
- `POST /analyze` — Analyze interview response