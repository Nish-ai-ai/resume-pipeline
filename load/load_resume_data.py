from transform.transform_resume_data import transform_resume_data, extract_resume

def load_resume_to_markdown(transformed_data):
    with open("resume.md", "w") as f:
        f.write(f"# {transformed_data['Name']}\n\n")
        f.write(f"**Summary**\n\n{transformed_data['Summary']}\n\n")
        f.write("## Experience\n")
        for job in transformed_data['Experience']:
            f.write(f"**{job['Role']}** at {job['Company']} ({job['Duration']})\n\n")
            f.write(f"{job['Responsibilities']}\n\n")
        f.write("## Education\n")
        for edu in transformed_data['Education']:
            f.write(f"**{edu['Degree']}** - {edu['University']} ({edu['Year']})\n\n")
        f.write("## Skills\n")
        f.write(f"{transformed_data['Skills']}\n")

if __name__ == "__main__":
    resume_data = extract_resume()
    transformed_data = transform_resume_data(resume_data)
    load_resume_to_markdown(transformed_data)
