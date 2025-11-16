import re

def extract_budget(text):
    nums = re.findall(r"\b\d{2,12}\b", text)
    return int(nums[0]) if nums else 0

def extract_timeline(text):
    match = re.search(r"(\d+)\s*(months|month|Months|Month)", text)
    return int(match.group(1)) if match else 12

def create_features(text, sections, inconsistencies):
    return {
        "missing_sections": list(sections.values()).count("Missing"),
        "budget": extract_budget(text),
        "timeline_months": extract_timeline(text),
        "inconsistency_score": len(inconsistencies)
    }
