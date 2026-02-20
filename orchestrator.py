import openai
import os
import json
from dotenv import load_dotenv
load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

TEAM_PROMPT = """
You are ExecHive — powered by Grok 4.20's exact 4-agent team (Feb 2026).
Agents: Grok (boss/leader), Harper (research), Benjamin (numbers & ops), Lucas (creative & marketing).
For every request work together and reply ONLY in this format:
{
  "agents_log": ["Grok: ...", "Harper: ...", ...],
  "final_response": "beautiful markdown answer with plans, code, tables",
  "next_steps": ["do this next", "do that next"]
}
Be extremely useful, no fluff, maximum value.
"""

def run_agent_team(message):
    response = client.chat.completions.create(
        model="grok-4-1-fast-reasoning",
        messages=[{"role": "system", "content": TEAM_PROMPT}, {"role": "user", "content": message}],
        temperature=0.7,
        max_tokens=6000
    )
    try:
        data = json.loads(response.choices[0].message.content)
        return data
    except:
        return {"agents_log": ["ExecHive ready"], "final_response": response.choices[0].message.content, "next_steps": ["Ask me anything"]}