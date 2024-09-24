# This is the raw extracted data (like extraction step of ETL)
resume_data = {
    'Name': 'Nishanth Sety',
    'Email': 'komirisetynishanth@gmail.com',
    'Phone': '+1 (816)-462-8751',
    'Summary': 'Seasoned Data Engineer with over 4 years of experience in designing and optimizing data pipelines using Big Data technologies like Hadoop, Spark, Kafka, and Hive. Skilled in cloud-native data engineering on AWS and Azure, with expertise in Azure Data Factory, Databricks, Snowflake, and Redis. Strong background in ETL development, data lake/warehouse architectures, and data governance across the full data lifecycle. Proficient in building complex data workflows with Apache Airflow and migrating databases to Snowflake. Experienced in agile methodologies and CI/CD using tools like Git, Jenkins, Docker, and Kubernetes..',
    'Experience': [
        {

            'Company': 'HCA, Nashville, TN',
            'Role': 'Data Engineer',
            'Duration': 'Jan 2023 - Present',
            'Responsibilities': [
                'Designed and automated data ingestion pipelines using Spark, Sqoop, and Oozie, optimizing RDBMS-to-Azure Data Lake workflows.',
                'Developed data integration pipelines connecting MongoDB with Power BI, enabling seamless real-time data visualization and reporting.',
                'Created and managed data models in Azure Synapse, supporting enterprise-level analytics with automated ETL workflows.',
                'Developed large ETL models combining multiple sources using Azure Data Factory and Databricks for incremental data loads.'
            ]
        },
        {
            'Company': 'Mastercard, St. Louis, MO',
            'Role': 'Data Engineer',
            'Duration': 'Jul 2022 - Dec 2022',
            'Responsibilities': [
                'Built scalable data pipelines utilizing AWS services (EMR, EC2, S3, RDS, Redshift) for large-scale data processing and analytics.',
                'Enhanced ETL performance using Spark’s in-memory processing, improving the speed of processing large datasets stored in S3.',
                'Optimized SQL queries for data transformation, ensuring faster data processing and improved system reliability.',
                'Integrated diverse data sources and adhered to data quality standards, following Agile methodologies for efficient project delivery.'
            ]
        },
        {
            'Company': 'HTC GLobal, India',
            'Role': 'Data Engineer',
            'Duration': 'Jul 2019 - Jun 2021',
            'Responsibilities': [
                'Developed healthcare analytics systems using R, Hadoop, and MongoDB, ensuring compliance with data governance protocols.',
                'Built ETL pipelines with Spark, SQL, and Redshift, processing large healthcare datasets to derive valuable business insights.',
                'Implemented CI/CD pipelines using Jenkins and Terraform, automating AWS deployments and reducing operational downtime.',
                'Processed and migrated data using AWS EMR and Glue, streamlining complex healthcare data integration.'
            ]
        }
    ],
    'Education': [
        {
            'Degree': "Master's Degree in Computer Science",
            'University': "University of Central Missouri",
            'Year': '2021-2022'
        }
    ],
    'Skills': [
        'Hadoop, Spark, Kafka, Azure Data Factory, Power BI, Snowflake'
    ]
}

def extract_resume():
    return resume_data
