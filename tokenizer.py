import re

def tokenizer(query):
    # Split query into tokens using regular expressions
    tokens = re.split('\s+(?=(?:[^"]*"[^"]*")*[^"]*$)', query)
    return tokens
