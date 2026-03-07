from fastapi import APIRouter
from services.analysis_service import run_analysis

router = APIRouter()


@router.post("/analyze-risk")
def analyze_risk():

    query = "Analyze this document for compliance and security risks"

    result = run_analysis(query)

    return result