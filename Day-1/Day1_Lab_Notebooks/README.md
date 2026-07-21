# Day 1 · Lab — Single-Agent Mastery

## Prerequisites (already true in your sandbox)

- `(base)` conda env active, `/opt/miniconda/bin/python`
- All packages preinstalled: `langgraph`, `langchain_openai`, `pydantic_ai`, `claude_agent_sdk`, `agents`, `mcp`
- `~/agentic-lab/.env` contains `DATABASE_URL` and `LANGSMITH_TRACING=true`
- `OPENROUTER_API_KEY` set at shell level
- `agentic-postgres` docker container running

## Optional (for LangSmith traces)

Paste your LangSmith key into `~/agentic-lab/.env`:

```bash
# Replace <your-langsmith-key> with an actual key from smith.langchain.com/settings
sed -i "s|^LANGSMITH_API_KEY=$|LANGSMITH_API_KEY=<your-langsmith-key>|" ~/agentic-lab/.env
grep -q "^LANGSMITH_PROJECT" ~/agentic-lab/.env || echo "LANGSMITH_PROJECT=agentic-lab" >> ~/agentic-lab/.env
```

Without a key, Step 1 auto-flips `LANGSMITH_TRACING` to `false` to silence noise. Lab still runs.

## Deploy this bundle to the sandbox

```bash
mkdir -p ~/agentic-lab/day1
# Copy all files in this bundle to ~/agentic-lab/day1/
# (via VS Code drag-drop, scp, or however your workflow does file transfer)
```

## Run Lab 1

1. Open `~/agentic-lab/day1/lab1_loan_agent.ipynb` in VS Code
2. `Ctrl+Shift+P` → `Python: Select Interpreter` → `/opt/miniconda/bin/python`
3. Run cells top-to-bottom
4. Step 1 diagnoses environment — fix any ✗ before proceeding

## Run LangGraph Studio

Separate terminal:

```bash
cd ~/agentic-lab/day1
langgraph dev
```

Open: <https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024>

## Files

| File | Purpose |
|---|---|
| `lab1_loan_agent.ipynb` | Main lab — LangGraph + PostgreSQL + HITL |
| `lab2_sdk_comparison.ipynb` | Stretch — Claude Agent SDK + OpenAI Agents SDK |
| `agent.py` | LangGraph Studio reference agent |
| `langgraph.json` | Studio config |

## Troubleshooting

| Symptom | Fix |
|---|---|
| `.env not loaded` | `pip install python-dotenv`, re-run Step 1 |
| `DATABASE_URL missing` | Confirmed present in your `.env`; just re-run Step 1 |
| `agentic-postgres not running` | `cd ~/agentic-lab && docker compose up -d` |
| `401 Unauthorized` from OpenRouter | Model ID missing provider prefix; `base_url` should end in `/api/v1` |
| `interrupt_before` doesn't pause | It's on `compile()`, not `add_node()` |
| Trace not in LangSmith | Wait 30s. Confirm `LANGSMITH_API_KEY` in `.env`, re-run Step 1 |
| `langgraph dev` won't start | Check `langgraph.json` and `agent.py:graph` path |
