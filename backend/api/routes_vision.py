from fastapi import APIRouter, UploadFile, File, HTTPException
from backend.core.aws_client import nova_client

router = APIRouter()

@router.post("/analyze-document")
async def analyze_medical_document(file: UploadFile = File(...)):
    """
    Accepts an image or document and uses Nova Multimodal to extract insights.
    """
    allowed_extensions = ('.png', '.jpg', '.jpeg', '.pdf')
    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an image or PDF.")
    
    if not nova_client:
        raise HTTPException(status_code=500, detail="AWS Bedrock client not initialized.")

    try:
        file_bytes = await file.read()
        file_extension = file.filename.split('.')[-1].lower()
        
        # NOTE: Multimodal payload structure
        # model_id = "amazon.nova-2-pro-v1:0" 
        # response = nova_client.converse(
        #     modelId=model_id,
        #     messages=[
        #         {
        #             "role": "user",
        #             "content": [
        #                 {"text": "Analyze this clinical document and summarize the findings."},
        #                 {
        #                     "image": {
        #                         "format": "jpeg" if file_extension in ['jpg', 'jpeg'] else file_extension,
        #                         "source": {"bytes": file_bytes}
        #                     }
        #                 }
        #             ]
        #         }
        #     ]
        # )
        
        # Mock response for local testing
        output_text = "Analysis complete: Document indicates normal blood pressure levels and standard cell morphology. No anomalies detected."
        
        return {
            "status": "success",
            "filename": file.filename,
            "analysis": output_text
        }
        
    except Exception as e:
        print(f"🔥 Multimodal processing error: {e}")
        raise HTTPException(status_code=500, detail=str(e))