from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


def generate_report(analysis, score):

    os.makedirs("reports", exist_ok=True)

    file_path = "reports/compliance_report.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)

    c.drawString(100, 750, "AI Compliance Audit Report")
    c.drawString(100, 720, f"Compliance Score: {score}/100")

    y = 680

    lines = analysis.split("\n")

    for line in lines:
        c.drawString(100, y, line)
        y -= 20

    c.save()

    return file_path