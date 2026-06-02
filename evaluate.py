from src.analysis import analyze_text
from src.emotion import analyze_emotion
from src.deception import analyze_deception
from src.drift import analyze_drift

def evaluate(text):
    return {
        "emotion": analyze_emotion(text),
        "deception": analyze_deception(text),
        "drift": analyze_drift(text)
    }

if __name__ == "__main__":
    sample = "This is a sample text for evaluation."
    result = evaluate(sample)
    print(result)

