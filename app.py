import openai
import json

# Set your OpenAI API key here
openai.api_key = 'sk-proj-aI6E6U2A1TYvz6KW2UK7T3BlbkFJOw46rFoVUJ8dSX6VJfFJ'

def parse_resume_to_json(resume_content):
    prompt = f"""
    Please parse the following resume content into JSON format. The JSON should include sections such as "Personal Information", "Education", "Work Experience", "Skills", and "Certifications". Each section should contain relevant details extracted from the resume text.

    Resume:
    {resume_content}
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in resume parsing."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message['content'].strip()

# Example usage
resume_text = """
John Doe
Software Engineer
ABC Corp
2018 - 2022
Skills: Python, JavaScript, SQL
Email: john.doe@example.com
Phone: +1 123-456-7890
"""

parsed_resume_json = parse_resume_to_json(resume_text)
parsed_resume_dict = json.loads(parsed_resume_json)

print(json.dumps(parsed_resume_dict, indent=4))

