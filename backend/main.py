from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize FastAPI
app = FastAPI()

# Path to the model checkpoint folder
MODEL_PATH = "./models/llama-3.2-3b-CC/final-1-epoch/checkpoint-500"

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.7

@app.post("/generate/")
async def generate_text(request: PromptRequest):
    # Encode the input prompt
    inputs = tokenizer.encode(request.prompt, return_tensors="pt")
    
    # Generate text based on the input prompt
    outputs = model.generate(
        inputs,
        max_length=request.max_length,
        temperature=request.temperature,
        pad_token_id=tokenizer.eos_token_id
    )
    
    # Decode the generated tokens into text
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Return the result
    return {"response": result}
