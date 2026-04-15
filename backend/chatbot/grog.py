from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
print("KEY LOADED:", os.getenv("GROQ_API_KEY"))
 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
 
 
class ChatRequest(BaseModel):
    message: str
 
 
class ChatResponse(BaseModel):
    reply: str
 
 
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
 
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Answer questions clearly and concisely.",
                },
                {"role": "user", "content": request.message},
            ],
            max_tokens=1024,
            temperature=0.7,
        )
 
        reply = completion.choices[0].message.content
        return ChatResponse(reply=reply)
 
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Groq API error: {str(e)}")
 
 
@app.get("/health")
async def health():
    return {"status": "ok"}
 
