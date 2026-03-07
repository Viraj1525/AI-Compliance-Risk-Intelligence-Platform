from fastapi import APIRouter
from services.analysis_service import run_analysis
from services.report_service import generate_report

router = APIRouter()


@router.post("/generate-report")
def generate_compliance_report():

    query = "Analyze this document for compliance risks"

    result = run_analysis(query)

    report_path = generate_report(
        result["analysis"],
        result["compliance_score"]
    )

    return {
        "message": "Report generated successfully",
        "report_path": report_path
    }