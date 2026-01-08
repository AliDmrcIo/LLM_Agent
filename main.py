# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
from agent import run_agent
from fastapi.responses import FileResponse

app = FastAPI()

# Tarayıcıdan erişim izni (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    """
    Frontend'den mesajı al, Agent'a ver, cevabı dön.
    """
    user_input = req.message
    print(f"\n[API] Gelen İstek: {user_input}")
    
    try:
        # Agent çalıştır
        response = run_agent(user_input)
        
        # Cevabı frontend'e gönder
        return {"reply": response}
    except Exception as e:
        return {"reply": f"Sistem Hatası: {str(e)}"}
    
@app.get("/")
def read_root():
    return FileResponse("index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)