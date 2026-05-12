import os
from openai import OpenAI
from dotenv import load_dotenv

# Load your environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the client exactly as you did in mem.py
client = OpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("Fetching available models for your Free Tier key...\n")

try:
    # Call the list models endpoint
    models = client.models.list()
    
    print("Available Model IDs:")
    print("-" * 30)
    
    # Loop through and print just the ID so you can copy-paste it
    for model in models.data:
        print(f"-> {model.id}")
        
except Exception as e:
    print(f"An error occurred: {e}")