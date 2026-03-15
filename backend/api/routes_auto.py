from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio

router = APIRouter()

class SyncRequest(BaseModel):
    patient_data: dict

@router.post("/sync-ehr")
async def sync_to_ehr(request: SyncRequest):
    """
    Triggers a Nova Act UI Automation agent to fill out the mock EHR system.
    """
    if not request.patient_data:
        raise HTTPException(status_code=400, detail="Patient data is required.")
        
    try:
        # Here is where the Nova Act fleet service is invoked to navigate the web portal
        
        # Simulating the headless browser automation delay
        await asyncio.sleep(2)
        
        return {
            "status": "success",
            "message": "Nova Act successfully navigated the EHR portal and injected the patient data.",
            "synced_records": request.patient_data
        }
    except Exception as e:
        print(f"🔥 Nova Act Automation error: {e}")
        raise HTTPException(status_code=500, detail=str(e))