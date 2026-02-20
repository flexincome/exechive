from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from orchestrator import run_agent_team
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="ExecHive - Your Grok 4.20 AI Executive Team")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

class Query(BaseModel):
    message: str

@app.post("/ask")
async def ask(query: Query):
    result = run_agent_team(query.message)
    return result

@app.get("/")
def home():
    return {"message": "🚀 ExecHive is running! Open http://localhost:8000/docs to test your AI team"}

if __name__ == "__main__":
    print("🚀 Starting ExecHive... open browser to http://localhost:8000/docs")
    uvicorn.run(app, host="0.0.0.0", port=8000)