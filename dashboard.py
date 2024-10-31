import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Sample skills data
skills_data = {
    "Skill": ["Hadoop", "Spark", "Kafka", "Azure Data Factory", "Power BI", "Snowflake"],
    "Proficiency": [4, 4, 3, 4, 5, 3]  # Proficiency scale 1-5
}

# Streamlit dashboard
st.title("Skills Proficiency Dashboard")

# Section: Education from Markdown
st.header("Nishanth_Resume")

# Load and display the education data from the .md file
with open('load/resume.md', 'r' ) as file:
    education_markdown = file.read()

# Display the markdown content
st.markdown(education_markdown)

# Create a DataFrame for skills
skills_df = pd.DataFrame(skills_data)



# Display the skills table
st.header("Skills Proficiency")
st.dataframe(skills_df)

# Plot the skills proficiency
st.subheader("Skills Proficiency Chart")
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size here
ax.bar(skills_df["Skill"], skills_df["Proficiency"], color='green', width=0.6)  # Adjust bar width

# Adjust x-axis label size and rotation
plt.xticks(rotation=45, fontsize=12)  # Rotate labels and change font size
plt.yticks(fontsize=12)  # Adjust y-axis font size

# Add labels
ax.set_ylabel('Proficiency (1-5)', fontsize=12)
ax.set_xlabel('Skills', fontsize=12)
ax.set_title('Skills Proficiency', fontsize=14)

# Display the plot in Streamlit
st.pyplot(fig)
