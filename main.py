from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"cleanhire backend is running"}
@app.post("/analyze")
def analyze(response: dict):
    text = response["text"]
    text_lower = text.lower()

    filler_words = ["um", "uh", "like", "you know", "basically", "literally"]
    found_fillers = [word for word in filler_words if word in text_lower]

    hedging_words = ["i think", "i believe", "maybe", "perhaps", "i guess", "probably", "not sure", "i feel like"]
    found_hedging = [word for word in hedging_words if word in text_lower]
    total_signals = len(found_fillers) + len(found_hedging)
    confidence_score = max(0, 100 - (total_signals * 10))
    return {
        "received": text,
        "length": len(text),
        "filler_words_found": found_fillers,
        "filler_count": len(found_fillers),
        "hedging_words_found": found_hedging,
        "hedging_count": len(found_hedging),
        "confidence_score": confidence_score
    }