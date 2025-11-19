def extract_sections(text):
    sections = {}

    keywords = {
        "objective": ["objective", "project objective"],
        "budget": ["budget", "financials", "cost estimate"],
        "timeline": ["timeline", "duration"],
        "impact": ["environmental impact", "impact"],
        "justification": ["justification", "need"],
    }

    for section, keys in keywords.items():
        for k in keys:
            if k.lower() in text.lower():
                sections[section] = f"Found section: {section}"
                break
        else:
            sections[section] = "Missing"

    return sections