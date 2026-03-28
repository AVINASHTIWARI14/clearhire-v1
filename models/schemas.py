from pydantic import BaseModel
class InterviewResponse(BaseModel):
    text: str
    candidatename: str = "Anonymous"