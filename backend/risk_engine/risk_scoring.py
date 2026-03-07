def calculate_compliance_score(analysis_text):

    score = 100

    if "High" in analysis_text:
        score -= 30

    if "Medium" in analysis_text:
        score -= 15

    if "Low" in analysis_text:
        score -= 5

    if score < 0:
        score = 0

    return score