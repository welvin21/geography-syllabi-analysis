import re

class TextPreprocessor():
    def __init__(self):
        pass
    
    def preprocess(self, text: str):
        text = text.replace('\n', '')
        text = text.lower()
        text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
        text = re.sub(r'[^A-Za-z0-9]+', ' ', text)
        text = re.sub(r'[\d.]', '', text)
        text = text.replace('achge', '')
        text = " ".join([w for w in text.split(" ") if len(w) > 1])
        
        return text
