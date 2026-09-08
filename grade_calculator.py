"""
UK University Degree Classification & Module Weighting Utility
Compliant with QAA Frameworks for Higher Education Qualifications (FHEQ)
Developed for educational demonstration and academic planning.
"""

def calculate_uk_classification(modules):
    """
    Computes weighted average percentage and returns the UK degree classification.
    
    Expected format:
    modules = [
        {"name": "Research Methodology", "credits": 20, "mark": 68},
        {"name": "Dissertation", "credits": 60, "mark": 72}
    ]
    """
    total_credits = sum(m["credits"] for m in modules)
    if total_credits == 0:
        return 0, "No credits provided"
        
    weighted_total = sum(m["credits"] * m["mark"] for m in modules)
    overall_mark = round(weighted_total / total_credits, 2)
    
    # Standard UK Higher Education Classification Boundaries
    if overall_mark >= 70.0:
        classification = "First-Class Honours (1st) / Distinction (Level 7)"
    elif overall_mark >= 60.0:
        classification = "Upper Second-Class Honours (2:1) / Merit (Level 7)"
    elif overall_mark >= 50.0:
        classification = "Lower Second-Class Honours (2:2) / Pass (Level 7)"
    elif overall_mark >= 40.0:
        classification = "Third-Class Honours (3rd) / Pass (Undergraduate Level 4-6)"
    else:
        classification = "Fail / Referral Required"
        
    return overall_mark, classification

if __name__ == "__main__":
    sample_modules = [
        {"name": "Advanced Legal Methodologies", "credits": 30, "mark": 67},
        {"name": "Independent Research Project", "credits": 60, "mark": 74},
        {"name": "Critical Literature Synthesis", "credits": 30, "mark": 62}
    ]
    mark, boundary = calculate_uk_classification(sample_modules)
    print(f"Overall Weighted Average: {mark}%")
    print(f"Projected Outcome: {boundary}")
