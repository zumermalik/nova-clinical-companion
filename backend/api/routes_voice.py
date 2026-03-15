from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.core.aws_client import nova_client

router = APIRouter()

@router.post("/transcribe")
async def process_voice_dictation(file: UploadFile = File(...)):
    """
    Accepts an audio file and processes it using Nova 2 Sonic.
    """
    if not file.filename.endswith(('.wav', '.mp3', '.m4a')):
        raise HTTPException(status_code=400, detail="Invalid audio format. Use WAV, MP3, or M4A.")
    
    if not nova_client:
        raise HTTPException(status_code=500, detail="AWS Bedrock client not initialized.")

    try:
        audio_bytes = await file.read()
        
        # NOTE: AWS Bedrock payload structure for Nova 2 Sonic.
        # Uncomment and configure model_id once your AWS region has full Sonic access.
        
        # model_id = "amazon.nova-2-sonic-v1:0" 
        # response = nova_client.converse(
        #     modelId=model_id,
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": [
        #                 {"text": "Transcribe this clinical dictation and summarize the main points."},
        #                 {
        #                     "document": {
        #                         "name": "dictation",
        #                         "format": file.filename.split('.')[-1],
        #                         "source": {"bytes": audio_bytes}
        #                     }
        #                 }
        #             ]
        #         }
        #     ]
        # )
        
        # Mock response for local testing
        transcription = "Patient presents with mild hypertension. Prescribed 10mg Lisinopril."
        
        return {
            "status": "success",
            "filename": file.filename,
            "transcription": transcription
        }
        
    except Exception as e:
        print(f"🔥 Voice processing error: {e}")
        raise HTTPException(status_code=500, detail=str(e))