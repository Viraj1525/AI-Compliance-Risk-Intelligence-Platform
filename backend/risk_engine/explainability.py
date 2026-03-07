def generate_explanation(risk_output):

    explanation = f"""
Compliance Risk Analysis Explanation

The AI system identified the following issues:

{risk_output}

These issues may violate data protection
or security compliance requirements.
"""

    return explanation