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


## 📋 Requirements

- Python 3.8+
- SpaCy 3.0+
- PyPDF2
- OpenAI Python package
- Internet connection for GPT API access


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
