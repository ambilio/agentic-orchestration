"""Day 1 reference agent — LangGraph Studio loads this via langgraph.json.

From a terminal:
    cd ~/agentic-lab/day1
    langgraph dev
    # Open: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
"""
from __future__ import annotations

import json
import os
from typing import Annotated, TypedDict
import operator

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END

# Load env from the sandbox .env; keep shell values (OPENROUTER_API_KEY)
load_dotenv(os.path.expanduser("~/agentic-lab/.env"), override=False)
for k in ("ANTHROPIC_API_KEY","OPENAI_API_KEY","LANGSMITH_API_KEY"):
    if os.environ.get(k) == "":
        del os.environ[k]


class LoanState(TypedDict):
    application_id: str
    applicant_name: str
    loan_amount: float
    monthly_income: float
    messages: Annotated[list, operator.add]
    eligibility_score: float
    bureau_score: int
    decision: str
    human_feedback: dict


_llm = ChatOpenAI(
    model="anthropic/claude-sonnet-4.5",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
    temperature=0,
)


def check_eligibility(state: LoanState) -> dict:
    income = state["monthly_income"]
    amount = state["loan_amount"]
    if amount <= 0:
        return {"eligibility_score": 0.0, "messages": ["eligibility: invalid amount"]}
    score = min(100.0, (income * 12 / amount) * 25)
    return {"eligibility_score": score, "messages": [f"eligibility_check: score={score:.1f}"]}


def route_by_score(state: LoanState) -> str:
    s = state["eligibility_score"]
    if s >= 80:
        return "high"
    if s >= 50:
        return "review"
    return "low"


def bureau_lookup(state: LoanState) -> dict:
    prompt = (
        f"Given an applicant with monthly income {state['monthly_income']:.0f} "
        f"and loan amount {state['loan_amount']:.0f}, return a plausible credit bureau "
        f"response as JSON with keys 'score' (int 300-850) and 'tier' (low/medium/high). "
        f"Respond ONLY with the JSON object, no prose."
    )
    text = _llm.invoke(prompt).content.strip()
    if text.startswith("```"):
        text = text.strip("`").split("\n", 1)[-1].rsplit("```", 1)[0].strip()
        if text.startswith("json"):
            text = text[4:].strip()
    try:
        score = int(json.loads(text)["score"])
    except Exception:
        score = 700
    return {"bureau_score": score, "messages": [f"bureau_lookup: score={score}"]}


def human_review(state: LoanState) -> dict:
    return {"messages": [f"human_review: feedback={state.get('human_feedback', {})}"]}


def make_decision(state: LoanState) -> dict:
    bureau = state.get("bureau_score", 0)
    human = state.get("human_feedback", {})
    if human.get("approved") is True:
        decision = "approved"
    elif human.get("approved") is False:
        decision = "rejected"
    elif bureau >= 700:
        decision = "approved"
    elif bureau >= 600:
        decision = "review"
    else:
        decision = "rejected"
    return {"decision": decision, "messages": [f"decision: {decision}"]}


def _build():
    b = StateGraph(LoanState)
    b.add_node("eligibility", check_eligibility)
    b.add_node("bureau", bureau_lookup)
    b.add_node("human_review", human_review)
    b.add_node("decision", make_decision)

    b.add_edge(START, "eligibility")
    b.add_conditional_edges(
        "eligibility",
        route_by_score,
        {"high": "bureau", "review": "human_review", "low": END},
    )
    b.add_edge("bureau", "decision")
    b.add_edge("human_review", "decision")
    b.add_edge("decision", END)
    return b


# LangGraph Studio picks up `graph` from this module.
# Studio manages the checkpointer itself.
graph = _build().compile(interrupt_before=["human_review"])
