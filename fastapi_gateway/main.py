from fastapi import FastAPI, Header, HTTPException
import requests, os

app = FastAPI()

API_KEY = os.getenv("API_KEY", "changeme")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")

@app.post("/chat")
def chat(prompt: str, authorization: str = Header(None)):
    if authorization != f"Bearer {API_KEY}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    res = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={"model": "mistral:instruct", "prompt": prompt, "stream": False},
        timeout=600
    )
    return res.json()
