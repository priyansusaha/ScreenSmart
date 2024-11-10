import spacy
import PyPDF2
import openai
from pathlib import Path
import re
from typing import Dict, List, Tuple


class ResumeParser:
    def __init__(self):
        # Load SpaCy's English model with pre-trained pipeline
        self.nlp = spacy.load("en_core_web_lg")

        # Custom labels for entity recognition
        self.SKILLS_PATTERN = [
            "python", "java", "javascript", "react", "node.js", "sql",
            "machine learning", "data analysis", "nlp", "aws", "docker"
        ]

        # Add skill patterns to pipeline
        ruler = self.nlp.add_pipe("entity_ruler", before="ner")
        patterns = [{"label": "SKILL", "pattern": skill} for skill in self.SKILLS_PATTERN]
        ruler.add_patterns(patterns)

    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text content from PDF file."""
        text = ""
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text

    def clean_text(self, text: str) -> str:
        """Clean and preprocess extracted text."""
        # Remove extra whitespace and special characters
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s@.]', ' ', text)
        return text.strip()

    def extract_entities(self, text: str) -> Dict[str, List[str]]:
        """Extract relevant entities from text using SpaCy NER."""
        doc = self.nlp(text)

        entities = {
            'skills': [],
            'organizations': [],
            'dates': [],
            'emails': [],
        }

        # Extract skills
        for ent in doc.ents:
            if ent.label_ == "SKILL":
                entities['skills'].append(ent.text)
            elif ent.label_ == "ORG":
                entities['organizations'].append(ent.text)
            elif ent.label_ == "DATE":
                entities['dates'].append(ent.text)

        # Extract email using regex
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        if emails:
            entities['emails'].extend(emails)

        # Remove duplicates and sort
        for key in entities:
            entities[key] = sorted(list(set(entities[key])))

        return entities


class ResumeScorer:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_score_and_feedback(self, resume_entities: Dict[str, List[str]], job_description: str) -> Tuple[
        float, str]:
        """Generate score and feedback using OpenAI's GPT."""
        # Create a prompt for GPT
        prompt = f"""
        Analyze the following resume details against the job description and provide:
        1. A score out of 100
        2. Detailed feedback including strengths and areas for improvement

        Resume Details:
        Skills: {', '.join(resume_entities['skills'])}
        Organizations: {', '.join(resume_entities['organizations'])}
        Experience Timeline: {', '.join(resume_entities['dates'])}

        Job Description:
        {job_description}

        Provide the response in the following format:
        Score: <number>
        Feedback: <detailed feedback>
        """

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert HR professional analyzing resumes."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        # Parse response
        response_text = response.choices[0].message.content

        # Extract score and feedback
        score_match = re.search(r'Score:\s*(\d+)', response_text)
        score = float(score_match.group(1)) if score_match else 0.0

        feedback_match = re.search(r'Feedback:(.*)', response_text, re.DOTALL)
        feedback = feedback_match.group(1).strip() if feedback_match else "No feedback provided."

        return score, feedback


def main(pdf_path: str, job_description: str, openai_api_key: str) -> Dict:
    """Main function to process resume and generate score/feedback."""
    # Initialize parser and scorer
    parser = ResumeParser()
    scorer = ResumeScorer(openai_api_key)

    # Process resume
    try:
        # Extract and clean text from PDF
        raw_text = parser.extract_text_from_pdf(pdf_path)
        cleaned_text = parser.clean_text(raw_text)

        # Extract entities
        entities = parser.extract_entities(cleaned_text)

        # Generate score and feedback
        score, feedback = scorer.generate_score_and_feedback(entities, job_description)

        return {
            'success': True,
            'entities': entities,
            'score': score,
            'feedback': feedback
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }


# Example usage
if __name__ == "__main__":
    # Configuration
    PDF_PATH = "path/to/resume.pdf"
    JOB_DESCRIPTION = """
    We are seeking a Python developer with strong experience in machine learning and NLP.
    Required skills:
    - Python programming
    - Machine learning algorithms
    - Natural Language Processing
    - SQL databases
    - Git version control
    """
    OPENAI_API_KEY = "your-api-key-here"

    # Process resume
    result = main(PDF_PATH, JOB_DESCRIPTION, OPENAI_API_KEY)

    # Print results
    if result['success']:
        print(f"Extracted Entities:")
        for entity_type, entities in result['entities'].items():
            print(f"{entity_type.capitalize()}: {', '.join(entities)}")
        print(f"\nScore: {result['score']}/100")
        print(f"Feedback: {result['feedback']}")
    else:
        print(f"Error: {result['error']}")