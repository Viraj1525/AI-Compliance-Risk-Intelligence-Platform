from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from services.analysis_service import run_analysis

router = APIRouter()


class AnalysisRequest(BaseModel):
    query: Optional[str] = None


@router.post("/analyze-risk")
def analyze_risk(request: Optional[AnalysisRequest] = None):

    query = "Analyze this document for compliance and security risks"

    if request and request.query and request.query.strip():
        query = request.query.strip()

    result = run_analysis(query)

    return result
