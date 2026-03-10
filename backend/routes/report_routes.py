from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from services.analysis_service import run_analysis
from services.report_service import generate_report

router = APIRouter()


class ReportRequest(BaseModel):
    query: Optional[str] = None


@router.post("/generate-report")
def generate_compliance_report(request: Optional[ReportRequest] = None):

    query = "Analyze this document for compliance risks"

    if request and request.query and request.query.strip():
        query = request.query.strip()

    result = run_analysis(query)

    report_path = generate_report(
        result["analysis"],
        result["compliance_score"]
    )

    return {
        "message": "Report generated successfully",
        "analysis": result["analysis"],
        "compliance_score": result["compliance_score"],
        "report_path": report_path,
        "download_url": f"/{report_path.replace('\\', '/')}"
    }
