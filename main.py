from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InterviewResponse(BaseModel):
    text: str
    candidate_name: str = "Anonymous"

@app.get("/")
def home():
    return {"message": "clearhire backend is running"}

@app.post("/analyze")
def analyze(response: InterviewResponse):
    text = response.text
    text_lower = text.lower()

    filler_words = ["um", "uh", "like", "you know", "basically", "literally"]
    found_fillers = [word for word in filler_words if word in text_lower]

    hedging_words = ["i think", "i believe", "maybe", "perhaps", "i guess", "probably", "not sure", "i feel like"]
    found_hedging = [word for word in hedging_words if word in text_lower]

    word_count = len(text.split())
    if word_count < 10:
        length_penalty = 30
    elif word_count < 20:
        length_penalty = 15
    else:
        length_penalty = 0

    total_signals = len(found_fillers) + len(found_hedging)
    confidence_score = max(0, 100 - (total_signals * 10) - length_penalty)

    return {
        "received": text,
        "candidate_name": response.candidate_name,
        "word_count": word_count,
        "filler_words_found": found_fillers,
        "filler_count": len(found_fillers),
        "hedging_words_found": found_hedging,
        "hedging_count": len(found_hedging),
        "confidence_score": confidence_score
    }