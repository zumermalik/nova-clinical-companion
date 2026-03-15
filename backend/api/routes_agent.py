from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.services.agent_logic import process_clinical_note_with_nova

router = APIRouter()

# Data models to validate incoming and outgoing requests
class NoteRequest(BaseModel):
    text: str

class NoteResponse(BaseModel):
    structured_data: str

@router.post("/process-note", response_model=NoteResponse)
async def process_note(request: NoteRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Note text cannot be empty.")
    
    result = process_clinical_note_with_nova(request.text)
    
    if result.startswith("Error") or result.startswith("Failed"):
        raise HTTPException(status_code=500, detail=result)
        
    return NoteResponse(structured_data=result)