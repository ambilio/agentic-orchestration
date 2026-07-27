# Day 6 · Lab — Requirements Extraction & Documentation

## Prerequisites

- Track 3.A + Day 5 completed
- `~/agentic-lab/.env` with `OPENROUTER_API_KEY`
- No new sandbox packages required

## Files

| File | Purpose |
|---|---|
| `lab1_extract_requirements.ipynb` | Chunk transcript, extract with Pydantic, verify traceability |
| `lab2_brd_signoff.ipynb` | Render BRD from template, HITL sign-off with audit trail |
| `sample_transcript.txt` | Realistic product planning meeting (also embedded in Lab 1) |

## Run order

1. Deploy to `~/agentic-lab/day6/`
2. Open Lab 1, run cells top-to-bottom (saves requirements to `/tmp/day6_requirements.json`)
3. Open Lab 2 (same kernel; loads requirements from step 2)

## What each lab teaches

**Lab 1**: Staged extraction pipeline beats one-shot. `llm.with_structured_output()` forces schema compliance. Source-utterance traceability is the anti-hallucination check.

**Lab 2**: HITL sign-off uses the Day 1 `interrupt_before` pattern — nothing new to learn about LangGraph mechanics. Template + LLM overview is the document-generation pattern.

## Common issues

| Symptom | Fix |
|---|---|
| Empty extraction | Chunks too small — model has no context. Increase chunk size. |
| Source_utterance paraphrased | Prompt weakness. Add "Copy verbatim" more forcefully. |
| Traceability verification fails | Model added quotes/punctuation. Loosen check with normalization. |
| HITL doesn't pause | Missing `interrupt_before` in `compile()` (Day 1 trap). |
| Revise loop never terminates | Reviewer must eventually approve — not an infinite loop unless mis-configured. |
