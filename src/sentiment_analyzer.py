# sentiment_analyzer.py

from transformers import BertTokenizer, BertForSequenceClassification
import torch

class BERTSentimentAnalyzer:
    def __init__(self, model_name='nlptown/bert-base-multilingual-uncased-sentiment'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertForSequenceClassification.from_pretrained(model_name)
        self.model.to(self.device)

    def analyze(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', max_length=512, truncation=True)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        sentiment = torch.argmax(logits, dim=1).item()

        # Sentiment mapping (0 = very negative, 4 = very positive)
        if sentiment == 0 or sentiment == 1:
            return 'negative'
        elif sentiment == 2:
            return 'neutral'
        else:
            return 'positive'
