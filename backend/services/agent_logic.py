from backend.core.aws_client import nova_client

def process_clinical_note_with_nova(clinical_text: str) -> str:
    """
    Sends unstructured clinical notes to Amazon Nova 2 Lite to extract structured data.
    """
    if not nova_client:
        return "Error: Bedrock client not initialized. Check AWS credentials."
    
    # The Nova 2 Lite model ID 
    # Note: Depending on the AWS region you are assigned, you may need a prefix 
    # like 'us.amazon.nova-2-lite-v1:0' or 'global.amazon.nova-2-lite-v1:0'
    model_id = "amazon.nova-2-lite-v1:0" 
    
    # The system prompt acts as the bounds for the agent's behavior
    system_prompt = (
        "You are an expert clinical reasoning assistant. Extract key medical entities "
        "(symptoms, medications, dosages, and patient history) from the following note. "
        "Format the output as a clear, structured clinical summary ready for EHR entry."
    )
    
    try:
        response = nova_client.converse(
            modelId=model_id,
            messages=[
                {
                    "role": "user",
                    "content": [{"text": f"<note>{clinical_text}</note>"}]
                }
            ],
            system=[{"text": system_prompt}],
            inferenceConfig={
                "maxTokens": 1000,
                "temperature": 0.1 # Low temperature for highly factual medical data
            }
        )
        return response['output']['message']['content'][0]['text']
    
    except Exception as e:
        print(f"🔥 Error calling Nova 2 Lite: {e}")
        return f"Failed to process text: {str(e)}"