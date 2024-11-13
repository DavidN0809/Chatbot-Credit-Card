# backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import torch

# Initialize FastAPI
app = FastAPI()

# Load your fine-tuned model once when the server starts
MODEL_PATH = "./model/llama3.pt"  # Adjust path as needed
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.7

@app.post("/generate/")
async def generate_text(request: PromptRequest):
    inputs = tokenizer.encode(request.prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=request.max_length,
        temperature=request.temperature,
        pad_token_id=tokenizer.eos_token_id
    )
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"response": result}