# Day 3 · Lab — A2A & Enterprise Integration

## Prerequisites

Same as Day 1 & 2 — `(base)` conda env, Postgres running, `~/agentic-lab/.env` with `OPENROUTER_API_KEY`.

Additional packages Day 3 needs (Step 1 auto-installs if missing):

```bash
pip install --user httpx tenacity
python -c "import httpx, tenacity; print('OK')"
```

## Files

| File | Purpose |
|---|---|
| `lab1_saas_mcp.ipynb` | Mock OAuth2 + TokenCache + MCP tool wrapping SaaS |
| `lab2_circuit_breaker.ipynb` | Tenacity retry + CircuitBreaker state machine + combined pattern |

## Run order

1. Deploy to `~/agentic-lab/day3/`
2. Open Lab 1, run Step 1, confirm ✓
3. Continue through Lab 1
4. Open Lab 2 (same kernel), run

## What each lab teaches

**Lab 1**: The TokenCache class is the pattern for every OAuth2 integration. Fetch once, cache, refresh 5 min before expiry. Never fetch per-request.

**Lab 2**: Retry rides ON TOP of the breaker. Breaker guards against sustained failure. Together, they turn a flaky SaaS into a stable dependency from your agent's perspective.

## Common issues

| Symptom | Fix |
|---|---|
| Token fetched every call | `TokenCache` instance not at module scope — recreated per call |
| Retry runs forever | Missing `stop_after_attempt` — always cap it |
| Breaker stuck OPEN | `on_success()` not resetting `failures` counter |
| Recovery test never runs | Cooldown check needs `time.time() - opened_at > cooldown_sec` |
