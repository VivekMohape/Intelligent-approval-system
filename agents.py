from llm import call_llm
from utils import safe_json_parse
from models import Asset, Review, FinalSummary


async def marketing_coordinator(state):
    prompt = f"""
    Extract JSON:
    {state['raw_input']}
    """
    res = await call_llm(prompt)
    return {"asset": Asset(**safe_json_parse(res))}


async def marketing_review(state):
    res = await call_llm(f"Marketing review:\n{state['asset'].json()}")
    return {"marketing": Review(**safe_json_parse(res))}


async def brand_review(state):
    res = await call_llm(f"Brand review:\n{state['asset'].json()}")
    return {"brand": Review(**safe_json_parse(res))}


async def compliance_review(state):
    res = await call_llm(f"Compliance review:\n{state['asset'].json()}")
    return {"compliance": Review(**safe_json_parse(res))}


async def summary(state):
    overall = "Approved"

    if any([
        state["marketing"].decision == "Changes Required",
        state["brand"].decision == "Changes Required",
        state["compliance"].decision == "Changes Required"
    ]):
        overall = "Changes Required"

    return {
        "final": FinalSummary(
            overall_decision=overall,
            marketing=state["marketing"],
            brand=state["brand"],
            compliance=state["compliance"]
        )
    }
