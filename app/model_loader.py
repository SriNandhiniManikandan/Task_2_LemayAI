from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

class ModelLoader:
    def __init__(self, model_name: str = "google/flan-t5-large"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(self.device)

    def generate_response(self, prompt: str, max_length: int = 100) -> str:
        with torch.no_grad():  # Save memory and speed up inference
            inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
            outputs = self.model.generate(
                inputs.input_ids,
                max_length=max_length,
                num_return_sequences=1,
                do_sample=False
            )
            return self.tokenizer.decode(outputs[0], skip_special_tokens=True)