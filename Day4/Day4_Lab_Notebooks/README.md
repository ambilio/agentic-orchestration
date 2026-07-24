# Day 4 · Lab — Observability & Security

## Prerequisites

- `(base)` conda env active
- `OPENROUTER_API_KEY` in `~/agentic-lab/.env`
- OTel packages (Step 1 auto-installs if missing)

## Files

| File | Purpose |
|---|---|
| `lab1_langsmith_otel.ipynb` | LangSmith @traceable + OTel spans, coexistence pattern |
| `lab2_injection_defense.ipynb` | Prompt injection: attack, then 3-layer defense, then red team |

## Run order

1. Deploy to `~/agentic-lab/day4/`
2. Open Lab 1, run cells top-to-bottom
3. Open Lab 2 (same kernel)

## What each lab teaches

**Lab 1**: OTel is the last observability decision you'll make. Instrument once, ship anywhere. LangSmith stays for dev productivity.

**Lab 2**: Prompt injection is real. Filter inputs, validate outputs, isolate context. Red-team your own agent before customers do.

## Common issues

| Symptom | Fix |
|---|---|
| OTel spans not appearing | Call `trace.get_tracer_provider().force_flush()` before checking output |
| `@traceable` no-op | `langsmith` package missing, or LANGSMITH_API_KEY not set — both are OK for the lab |
| Regex false-positive on legit input | Add `\b` word boundaries to `BAD_PATTERNS` |
| All attacks slip past filter | Confirm you're calling `secure_loan_decision`, not `naive_loan_decision` |
