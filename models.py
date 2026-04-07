from pydantic import BaseModel
from typing import List, Optional


class Asset(BaseModel):
    title: str
    description: str
    claims: List[str]
    target_audience: Optional[str]


class Review(BaseModel):
    decision: str
    required_changes: List[str]
    recommendations: List[str]


class FinalSummary(BaseModel):
    overall_decision: str
    marketing: Review
    brand: Review
    compliance: Review
