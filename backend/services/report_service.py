import os

from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import simpleSplit
from reportlab.pdfgen import canvas


def generate_report(analysis, score):

    os.makedirs("reports", exist_ok=True)

    file_path = "reports/compliance_report.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)

    c.setTitle("AI Compliance Audit Report")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(72, 750, "AI Compliance Audit Report")

    c.setFont("Helvetica", 11)
    c.drawString(72, 730, f"Compliance Score: {score}/100")

    y = 700

    lines = analysis.split("\n") if analysis else ["No findings generated."]

    for line in lines:
        text_line = line.strip() or " "
        wrapped_lines = simpleSplit(text_line, "Helvetica", 10, 460)

        for wrapped in wrapped_lines:
            if y < 60:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = 750

            c.setFont("Helvetica", 10)
            c.drawString(72, y, wrapped)
            y -= 16

    c.save()

    return file_path
