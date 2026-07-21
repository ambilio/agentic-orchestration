# Day 2 · Lab — Multi-Agent & MCP Authoring

## Prerequisites

Same as Day 1 — `(base)` conda env, Postgres running, `~/agentic-lab/.env` with `OPENROUTER_API_KEY`.

Verify:
```bash
python -c "from mcp.server.fastmcp import FastMCP; print('OK')"
```

## Files

| File | Purpose |
|---|---|
| `lab1_multi_agent.ipynb` | Supervisor + 3 specialists on shared typed state |
| `lab2_fastmcp_server.ipynb` | FastMCP server with auth + rate limit, client integration |

## Run order

1. Deploy files to `~/agentic-lab/day2/`
2. Open Lab 1, run Step 1, confirm ✓
3. Continue through Lab 1
4. Open Lab 2 (same kernel), run

## Common issues

| Symptom | Fix |
|---|---|
| `ModuleNotFoundError: langgraph.checkpoint.postgres` | `pip install --user langgraph-checkpoint-postgres` |
| MCP client hangs | Server crashed silently — check `bureau_mcp_server.py` in Step 3 |
| Rate limit fires early | Kernel state — restart kernel to reset counters |
