from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Model ve tokenizer
model_name = "nanelimon/bert-base-turkish-offensive"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

def detect_insult(tweet):
    inputs = tokenizer(tweet, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)

    # Modelin sınıflandırma sonucunu al
    predictions = torch.argmax(outputs.logits, dim=-1)
    
    # Hakaret tespit edildiyse 1, edilmediyse 0 döner
    return predictions.item() == 1
