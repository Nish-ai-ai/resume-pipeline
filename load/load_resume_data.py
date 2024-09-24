from transform.transform_resume_data import transform_resume_data, extract_resume

def load_resume_to_markdown(transformed_data):
    with open("resume.md", "w") as f:
        f.write(f"# {transformed_data['name']}\n\n")
        f.write(f"**Summary**\n\n{transformed_data['summary']}\n\n")
        f.write("## Experience\n")
        for job in transformed_data['experience']:
            f.write(f"**{job['role']}** at {job['company']} ({job['duration']})\n\n")
            f.write(f"{job['responsibilities']}\n\n")
        f.write("## Education\n")
        for edu in transformed_data['education']:
            f.write(f"**{edu['degree']}** - {edu['university']} ({edu['year']})\n\n")
        f.write("## Skills\n")
        f.write(f"{transformed_data['skills']}\n")

if __name__ == "__main__":
    resume_data = extract_resume()
    transformed_data = transform_resume_data(resume_data)
    load_resume_to_markdown(transformed_data)
