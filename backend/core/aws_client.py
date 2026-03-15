import boto3
from botocore.exceptions import ClientError
from backend.core.config import settings

def get_bedrock_client():
    """
    Initializes and returns a Boto3 client for Amazon Bedrock Runtime.
    This is the gateway to all Amazon Nova models (Lite, Sonic, Embeddings).
    """
    try:
        # We explicitly pass the credentials from our config to ensure
        # it works perfectly inside the GitHub Codespace environment.
        client = boto3.client(
            service_name='bedrock-runtime',
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )
        print("✅ AWS Bedrock Runtime client initialized.")
        return client
    except Exception as e:
        print(f"🔥 Critical Error initializing Bedrock client: {e}")
        return None

# Create a singleton instance to be imported into our API routes
nova_client = get_bedrock_client()