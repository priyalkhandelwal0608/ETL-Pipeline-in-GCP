import requests

def call_ollama(prompt, model="llama3", timeout=5):
    """Communicates with the local Ollama server."""
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
        return response.json().get("response", "No response")
    except Exception:
        return "AI Offline"

def clean_csv_value(text):
    """Ensures text doesn't break CSV formatting."""
    if not text: return "N/A"
    # Replace commas with semicolons so the CSV doesn't split columns incorrectly
    return str(text).replace("\n", " ").replace(",", ";").replace('"', "'").strip()