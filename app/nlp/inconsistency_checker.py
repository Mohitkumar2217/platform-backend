def find_inconsistencies(text, sections):
    issues = []

    if sections.get("budget") == "Missing":
        issues.append("Budget section missing")

    if "years" in text.lower() and "5" not in text:
        issues.append("Timeline may be unrealistic")

    return issues
