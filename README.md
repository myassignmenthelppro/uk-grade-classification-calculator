# UK Higher Education Degree Classification & Weighting Calculator

An open-source academic assessment utility designed to calculate weighted averages, module credit allocations, and final degree classifications in accordance with the **Framework for Higher Education Qualifications (FHEQ)** and **Quality Assurance Agency (QAA)** benchmarks.

This tool helps undergraduate and postgraduate students decode their module handbooks, project assessment weightings, and model potential grading outcomes across Level 4, Level 5, Level 6 (Bachelor's), and Level 7 (Master's) programmes.

Developed as an educational resource in collaboration with the academic advisory and editorial mentors at [My Assignment Help Pro](https://myassignmenthelppro.com/).

---

## 1. Classification Benchmarks (UK Standard)

| Band Percentage | Undergraduate Classification (Levels 4–6) | Postgraduate Classification (Level 7) | Core Pedagogical Expectation |
| :--- | :--- | :--- | :--- |
| **70.0% – 100%** | First-Class Honours (1st) | Distinction | Authoritative critical evaluation, flawless methodology, original synthesis |
| **60.0% – 69.9%** | Upper Second-Class Honours (2:1) | Merit | Comprehensive literature synthesis, clear analytical structure, accurate referencing |
| **50.0% – 59.9%** | Lower Second-Class Honours (2:2) | Pass | Descriptive competence, basic argument flow, minor structural limitations |
| **40.0% – 49.9%** | Third-Class Honours (3rd) | Borderline / Compensatable | Limited critique, descriptive narrative, frequent formatting or citation errors |
| **Below 40.0%** | Fail / Resit Required | Fail | Learning outcomes unmet; fundamental methodological or structural gaps |

---

## 2. Algorithmic Implementation & Usage

The core engine computes credit-weighted arithmetic means, standardizing the variance between 15-credit, 30-credit, and 60-credit assessment blocks (such as independent capstone projects).

### Python Execution
```bash
# Clone the repository
git clone [https://github.com/](https://github.com/)[YOUR-GITHUB-USERNAME]/uk-grade-classification-calculator.git

# Navigate to directory
cd uk-grade-classification-calculator

# Run the terminal calculator
python grade_calculator.py
