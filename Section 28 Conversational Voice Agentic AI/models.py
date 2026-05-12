import google.generativeai as genai
import os

genai.configure(api_key="GEMINI_API_KEY")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"Model Name: {m.name}")
        print(f"Description: {m.description}\n")