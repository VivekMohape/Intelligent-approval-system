from langgraph.graph import StateGraph, END
from typing import TypedDict

from agents import *


class State(TypedDict):
    raw_input: str
    asset: dict
    marketing: dict
    brand: dict
    compliance: dict
    final: dict


def build_graph():
    builder = StateGraph(State)

    builder.add_node("coordinator", marketing_coordinator)

    builder.add_node("marketing", marketing_review)
    builder.add_node("brand", brand_review)
    builder.add_node("compliance", compliance_review)

    builder.add_node("summary", summary)

    builder.set_entry_point("coordinator")

    # Parallel fan-out
    builder.add_edge("coordinator", "marketing")
    builder.add_edge("coordinator", "brand")
    builder.add_edge("coordinator", "compliance")

    # Fan-in
    builder.add_edge("marketing", "summary")
    builder.add_edge("brand", "summary")
    builder.add_edge("compliance", "summary")

    builder.add_edge("summary", END)

    return builder.compile()
