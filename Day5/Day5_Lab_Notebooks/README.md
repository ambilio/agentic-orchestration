# Day 5 · Lab — Data Understanding & Text-to-SQL

## Prerequisites

- Track 3.A complete (`(base)` conda env, `~/agentic-lab/.env`, Postgres container)
- Additional: `sqlglot` (Lab 1 Step 1 auto-installs)

## Files

| File | Purpose |
|---|---|
| `lab1_text_to_sql.ipynb` | Load ba_sales DB, profile schema, build text-to-SQL agent |
| `lab2_guardrails.ipynb` | Add sqlglot guardrails, HITL for ambiguity, verification |

## Run order

1. Deploy to `~/agentic-lab/day5/`
2. Open Lab 1, run cells top-to-bottom (creates the ba_sales database)
3. Open Lab 2 (same kernel; assumes ba_sales exists)

## What each lab teaches

**Lab 1**: Schema grounding is the technique. Feed the model actual columns + sample values + row counts. Prompt engineering alone doesn't fix text-to-SQL.

**Lab 2**: Guardrails at the SQL layer (sqlglot AST), HITL for ambiguity, verification with reasoning trace. Same LangGraph patterns from Day 1, new application.

## Common issues

| Symptom | Fix |
|---|---|
| `ba_sales database does not exist` | Run Lab 1 Step 2 |
| `sqlglot` ImportError | `pip install --user sqlglot`, restart kernel |
| SQL wrapped in markdown fences | Lab strips them; if fails, check fence pattern |
| Ambiguity detected on every question | Word matcher too aggressive — tune |
| HITL doesn't pause | Missing `interrupt_before` in `compile()` (Day 1 trap) |
