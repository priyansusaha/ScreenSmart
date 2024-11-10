# ScreenSmart: AI-Driven Resume Parser and Scorer

ScreenSmart is an intelligent resume screening tool that combines the power of SpaCy's Named Entity Recognition (NER) with OpenAI's GPT to automate and enhance the candidate evaluation process. The system automatically extracts key information from resumes and provides job-specific scoring and detailed feedback.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![SpaCy](https://img.shields.io/badge/spaCy-3.0+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Features

- **Automated Resume Parsing**: Extract key information from PDF resumes using SpaCy NER
  - Skills and technologies
  - Work experience and organizations
  - Dates and timeline
  - Contact information

- **Intelligent Scoring**: Leverage OpenAI's GPT for sophisticated resume evaluation
  - Job-specific scoring (0-100)
  - Detailed feedback on candidate strengths
  - Areas for improvement
  - Match analysis against job requirements

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/priyansusaha/screensmart
cd screensmart
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Download the SpaCy English model:
```bash
python -m spacy download en_core_web_lg
```

5. Set up your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'  # On Windows, use: set OPENAI_API_KEY=your-api-key-here
```

## 📋 Requirements

- Python 3.8+
- SpaCy 3.0+
- PyPDF2
- OpenAI Python package
- Internet connection for GPT API access

## 💻 Usage

```python
from resume_parser import main

# Configure your inputs
pdf_path = "path/to/resume.pdf"
job_description = """
We are seeking a Python developer with strong experience in machine learning and NLP.
Required skills:
- Python programming
- Machine learning algorithms
- Natural Language Processing
- SQL databases
- Git version control
"""
openai_api_key = "your-api-key-here"

# Process the resume
result = main(pdf_path, job_description, openai_api_key)

# Print results
if result['success']:
    print(f"Extracted Entities:")
    for entity_type, entities in result['entities'].items():
        print(f"{entity_type.capitalize()}: {', '.join(entities)}")
    print(f"\nScore: {result['score']}/100")
    print(f"Feedback: {result['feedback']}")
else:
    print(f"Error: {result['error']}")
```

## 🏗️ Project Structure

```
screensmart/
├── resume_parser/
│   ├── __init__.py
│   ├── parser.py      # Resume parsing logic using SpaCy
│   └── scorer.py      # GPT integration for scoring
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   └── test_scorer.py
├── requirements.txt
└── README.md
```

## 🔧 Configuration

The system can be configured through environment variables or direct parameters:

- `OPENAI_API_KEY`: Your OpenAI API key
- `SPACY_MODEL`: SpaCy model to use (default: "en_core_web_lg")
- `GPT_MODEL`: GPT model to use (default: "gpt-4")

## 📊 Sample Output

```json
{
    "success": true,
    "entities": {
        "skills": ["Python", "Machine Learning", "NLP", "SQL"],
        "organizations": ["Tech Corp", "AI Solutions Inc"],
        "dates": ["2020-2022", "2018-2020"],
        "emails": ["candidate@email.com"]
    },
    "score": 85.5,
    "feedback": "Strong technical background in required areas..."
}
```


## 🙏 Acknowledgments

- SpaCy for their excellent NLP toolkit
- OpenAI for their GPT API
- The open-source community for various Python packages used in this project

## 📞 Contact

Your Name - [@priyansusaha](https://twitter.com/priyansusaha)

Project Link: [https://github.com/priyansusaha/screensmart](https://github.com/priyansusaha/screensmart)

## ⚠️ Disclaimer

This tool is designed to assist in the resume screening process but should not be used as the sole decision-maker in hiring processes. Human oversight and review are essential for fair and accurate candidate evaluation.
