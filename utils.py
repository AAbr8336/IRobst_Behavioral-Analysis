# Utility functions for shared operations

def clean_text(text):
    return text.strip() if text else ""

def normalize(text):
    return text.lower() if text else ""
