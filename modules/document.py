class Document():
    def __init__(self, tokens_frequency, vocabulary=[]):
        self.tokens_frequency = tokens_frequency
        self.tokens = set(tokens_frequency.keys())
        self.unique_tokens_frequency = {}
        self.unique_tokens = set()
        self.common_tokens_frequency = {}
        self.common_tokens = set()
        
        self.tokens_proportion = {}
        tokens_count = sum(list(tokens_frequency.values()))
        for key, value in tokens_frequency.items():
            self.tokens_proportion[key] = value/tokens_count
            
        self.vocabulary = vocabulary
        self.vocab_frequency = {}
        
    def fit_unique_tokens(self, *args):
        self.unique_tokens = self.tokens
        self.common_tokens = self.tokens
        
        for document in args:
            if(self == document):
                continue
            assert document.tokens_frequency
            self.unique_tokens = self.unique_tokens.difference(document.tokens)
            self.common_tokens = self.common_tokens.intersection(document.tokens)
        
        self.unique_tokens_frequency = {k: v for k, v in self.tokens_frequency.items() if k in self.unique_tokens}
        self.common_tokens_frequency = {k: v for k, v in self.tokens_frequency.items() if k in self.common_tokens}
    
    def fit_vocabulary(self):
        for key, value in self.tokens_frequency.items():
            if(key in self.vocabulary):
                self.vocab_frequency[key] = value
        
        return sum(list(self.vocab_frequency.values())) / sum(list(self.tokens_frequency.values()))
