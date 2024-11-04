# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import torch

# Initialize FastAPI
app = FastAPI()

# Load your fine-tuned model once when the server starts
MODEL_PATH = "./model/llama3.pt"  # Adjust path as needed
model = torch.load(MODEL_PATH)     # Adjust loading method as per model requirements

# Define input format
class Prompt(BaseModel):
    text: str

# Endpoint to generate responses
@app.post("/generate")
async def generate(prompt: Prompt):
    # Generate a response using your model
    response = model.generate(prompt.text)  # Adjust as per your model's generation method
    return {"response": response}

# Run using: uvicorn main:app --reload
