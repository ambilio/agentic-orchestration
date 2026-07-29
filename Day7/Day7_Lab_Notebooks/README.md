# Day 7 · Lab — Insight Synthesis & Reporting

## Prerequisites
- Days 5-6 completed; `~/agentic-lab/.env` with OPENROUTER_API_KEY
- matplotlib (usually pre-installed with conda base)

## Files
| File | Purpose |
|---|---|
| `lab1_insight_synthesis.ipynb` | Extract insights from Q4 data; rank by surprise × confidence |
| `lab2_report_charts.ipynb` | Draft memo, generate matplotlib charts, verify consistency |

## Run order
1. Deploy to `~/agentic-lab/day7/`
2. Lab 1 (writes to `/tmp/day7_insights.json`)
3. Lab 2 (reads from Lab 1's output)

## Common issues
| Symptom | Fix |
|---|---|
| JSON parse fails | Model added markdown fences; Step 4 strips them, verify |
| Chart exec() crashes | LLM used undefined var; check chart_code output for typos |
| Consistency check false positives | prose_numbers pattern too greedy; refine regex |
| All insights are "low" surprise | Prompt didn't emphasize surprise strongly enough; add 'CFO wouldn't expect' |
