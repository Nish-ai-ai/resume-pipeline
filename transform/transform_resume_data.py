from extract.extract_resume_data import extract_resume

def transform_resume_data(resume_data):
    # Example transformation: converting responsibilities to bullet points
    transformed_experience = []
    for job in resume_data['experience']:
        formatted_responsibilities = '\n'.join(f"- {resp}" for resp in job['responsibilities'])
        transformed_experience.append({
            'company': job['company'],
            'role': job['role'],
            'duration': job['duration'],
            'responsibilities': formatted_responsibilities
        })
    # Returning the transformed data as structured text (can also return HTML or Markdown)
    return {
        'name': resume_data['name'],
        'summary': resume_data['summary'],
        'experience': transformed_experience,
        'education': resume_data['education'],
        'skills': ', '.join(resume_data['skills'])
    }

if __name__ == "__main__":
    resume_data = extract_resume()
    transformed_data = transform_resume_data(resume_data)
    print(transformed_data)

