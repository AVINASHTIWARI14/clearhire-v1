from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"cleanhire backend is running"}
@app.post("/analyze")
def analyze(response: dict):
    text = response["text"]
    
    filler_words = ["um", "uh", "like", "you know", "basically", "literally"]
    found_fillers = [word for word in filler_words if word in text.lower()]
    
    return {
        "received": text,
        "length": len(text),
        "filler_words_found": found_fillers,
        "filler_count": len(found_fillers)
    }