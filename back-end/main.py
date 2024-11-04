from fastapi import FastAPI
from pydantic import BaseModel
import torch

app = FastAPI()

class Prompt(BaseModel):
    text: str

@app.post("/generate")
async def generate(prompt: Prompt):
    # Load your fine-tuned Llama 3 model
    model = torch.load("path_to_finetuned_model")
    output = model.generate(prompt.text)  # Example
    return {"response": output}
