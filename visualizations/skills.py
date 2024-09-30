import matplotlib.pyplot as plt

# Example skills data
skills = ['AWS', 'Azure', 'Python', 'Scala', 'Java', 'Redshift', 'Hive', 'Jenkins', 'Docker', 'SQL_Server', 'MongoDB', 'HBase', 'Hadoop', 'Spark', 'Kafka', 'Azure_Data_Factory', 'Power_BI',
           'Snownflake']

proficiency = [4, 4, 4, 4, 5, 3, 4, 4, 4, 4, 3, 3, 5, 4, 4, 5, 4, 4]  # Proficiency scale 1-5

# Create a bar chart
fig, ax = plt.subplots(figsize=(10, 10))
ax.bar(skills, proficiency, color='green', width= 0.1 )

# Add labels
ax.set_ylabel('Proficiency (1-5)')
ax.set_title('Skills Proficiency')

plt.xticks(ticks=range(len(skills)), labels=skills, rotation=45, ha='right', fontsize=10)

# Save the visualization
plt.savefig(r'C:/Users/Program/resume-pipeline/visualizations/skills_proficiency.png')
plt.show()

