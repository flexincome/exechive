from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from orchestrator import run_agent_team
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="ExecHive - Your Grok 4.20 AI Executive Team")

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# This makes the pretty page show at the root
app.mount("/", StaticFiles(directory=".", html=True), name="static")

class Query(BaseModel):
    message: str

@app.post("/ask")
async def ask(query: Query):
    result = run_agent_team(query.message)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
