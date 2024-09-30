from extract.extract_resume_data import extract_resume

def transform_resume_data(resume_data):
    # Example transformation: converting responsibilities to bullet points
    transformed_Experience = []
    for job in resume_data['Experience']:
        formatted_Responsibilities = '\n'.join(f"- {resp}" for resp in job['Responsibilities'])
        transformed_Experience.append({
            'Company': job['Company'],
            'Role': job['Role'],
            'Duration': job['Duration'],
            'Responsibilities': formatted_Responsibilities
        })
    # Returning the transformed data as structured text (can also return HTML or Markdown)
    return {
        'Name': resume_data['Name'],
        'Summary': resume_data['Summary'],
        'Experience': transformed_Experience,
        'Education': resume_data['Education'],
        'Skills': ', '.join(resume_data['Skills'])
    }

if __name__ == "__main__":
    resume_data = extract_resume()
    transformed_data = transform_resume_data(resume_data)
    print(transformed_data)
