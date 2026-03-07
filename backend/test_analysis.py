from risk_engine.compliance_checker import analyze_compliance

sample_text = """
User data is stored indefinitely.
No retention policy is defined.
Encryption requirements are not specified.
"""

result = analyze_compliance(sample_text)

print(result)