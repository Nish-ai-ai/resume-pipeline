# This is the raw extracted data (like extraction step of ETL)
resume_data = {
    'name': 'Nishanth Sety',
    'email': 'komirisetynishanth@gmail.com',
    'phone': '+1 (816)-462-8751',
    'summary': 'Experienced Data Engineer with 4+ years in large-scale data processing.',
    'experience': [
        {

            'company': 'HCA, Nashville, TN',
            'role': 'Data Engineer',
            'duration': 'Jan 2023 - Present',
            'responsibilities': [
                'Managed ETL pipelines using Spark and Azure Data Factory',
                'Created interactive Power BI dashboards for real-time insights'
            ]
        },
        {
            'company': 'Mastercard, St. Louis, MO',
            'role': 'Data Engineer',
            'duration': 'Jul 2022 - Dec 2022',
            'responsibilities': [
                'Developed data pipelines using AWS stack (EMR, S3, Redshift)',
                'Integrated data from multiple sources to optimize reporting'
            ]
        }
    ],
    'education': [
        {
            'degree': "Master's Degree in Computer Science",
            'university': "University of Central Missouri",
            'year': '2021-2022'
        }
    ],
    'skills': [
        'Hadoop, Spark, Kafka, Azure Data Factory, Power BI, Snowflake'
    ]
}

def extract_resume():
    return resume_data
