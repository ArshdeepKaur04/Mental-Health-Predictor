import ollama 
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load fine-tuned T5 model
model_path = r"C:\Users\hp\Desktop\Arshdeep\College\Internships\Arogo\Fine-Tuning\t5_mental_health_model"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)
model.eval()

# Function to predict condition
def predict_condition(statement):
    inputs = tokenizer(statement, return_tensors="pt", max_length=100, truncation=True)
    with torch.no_grad():
        output = model.generate(**inputs, max_length=50)
    return tokenizer.decode(output[0], skip_special_tokens=True)

# Function to generate explanation
def generate_explanation(condition):
    prompt = f"Explain {condition} and suggest coping mechanisms & potential next steps."
    try:
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}], stream=False)
        if "message" in response and "content" in response["message"]:
            return response["message"]["content"]
        else:
            return "No response received."
    except Exception as e:
        return f"Error generating explanation: {e}"