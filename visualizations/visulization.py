import matplotlib.pyplot as plt

# Example experience data
experience = [
    {'company': 'HCA Nashville, TN', 'role': 'Data Engineer', 'start_year': 2023, 'end_year': 2024},
    {'company': 'Mastercard St. Louis, MO', 'role': 'Data Engineer', 'start_year': 2022, 'end_year': 2022},
    {'company':'HTC Global India','role':'Data Engineer','start_year':2019,'end_year':2021}
]

# Extract data for plotting
companies = [exp['company'] for exp in experience]
start_years = [exp['start_year'] for exp in experience]
end_years = [(exp['end_year'] - exp['start_year']) + 1 for exp in experience]

colors = ['red', 'green', 'blue']
# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 5))

# Horizontal bar chart
ax.barh(companies ,end_years, left=start_years,  color=colors)

# Add labels
ax.set_xlabel('Years')
ax.set_ylabel('Companies')
ax.set_title('Experience Timeline')

ax.set_xlabel('Years')
ax.set_ylabel('Companies')
ax.set_title('Experience Timeline')
# Save the visualization
plt.savefig(r"C:\Users\Program\resume-pipeline\visualizations\experience_timeline.png")
plt.show()

