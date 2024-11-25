from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, BitsAndBytesConfig, AutoModelForCausalLM
from peft import PeftModel, PeftConfig
import torch

# Initialize FastAPI
app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins; restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Paths to the trained model and base model
TRAINED_MODEL_PATH = "/opt/notebooks/Chatbot-Credit-Card/backend/models/llama-3.1-8b-CC/base-final"
BASE_MODEL_PATH = "meta-llama/Llama-3.1-8B"

# BitsAndBytes configuration
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

# Load the tokenizer from the trained model path
tokenizer = AutoTokenizer.from_pretrained(TRAINED_MODEL_PATH, trust_remote_code=True)

# Load the base model with quantization
print("Loading the base model...")
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_PATH,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)

# Load PEFT configuration and PEFT model
print("Loading the PEFT configuration and model...")
peft_config = PeftConfig.from_pretrained(TRAINED_MODEL_PATH)
model = PeftModel.from_pretrained(
    base_model,
    TRAINED_MODEL_PATH,
    device_map="auto",
    torch_dtype=torch.float16,
)

# Ensure tokenizer and model are aligned
print(f"Tokenizer vocabulary size: {len(tokenizer)}")
print(f"Model's embedding size: {model.get_input_embeddings().weight.shape[0]}")

class PromptRequest(BaseModel):
    prompt: str
    max_length: int = 200
    temperature: float = 0.7

@app.post("/generate/")
async def generate_text(request: PromptRequest):
    # Encode the input prompt
    inputs = tokenizer.encode(request.prompt, return_tensors="pt").to("cuda")  # Ensure tensor is moved to GPU if available
    
    # Generate text based on the input prompt
    outputs = model.generate(
        inputs,
        max_length=request.max_length,
        temperature=request.temperature,
        pad_token_id=tokenizer.eos_token_id
        # early_stopping=True  # Stop generation when a logical end is reached
    )

    
    # Decode the generated tokens into text
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Return the result
    return {"response": result}