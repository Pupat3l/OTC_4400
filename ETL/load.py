import boto3
import psycopg2
 
# AWS credentials and other details
aws_access_key_id = 'xyz'
aws_secret_access_key = 'xyz'
bucket_name = 'bucket-name'
s3_file_path = 'path/to/s3/file'
redshift_role_arn = 'a'
 
# Redshift Serverless connection details
endpoint = 'redshift/enpoint/url'
port = '5439'  # default Redshift port
database = 'dev'
user = 'admin'
password = 'password'
 
# Setting the connection timeout (in seconds)
timeout = 60  # for example, 60 seconds
 
# Connection string with timeout
conn_string = f"dbname='{database}' user='{user}' host='{endpoint}' password='{password}' port='{port}' connect_timeout={timeout}"
 
# Connect to Redshift
conn = psycopg2.connect(conn_string)
 
# Create a cursor object using the connection
cur = conn.cursor()
 
# SQL COPY command to load data from S3 to Redshift under the 'OTC market' schema, do it for all individual files
copy_cmd = f"""
COPY ____
FROM 's3://{bucket_name}/{s3_file_path}'
CREDENTIALS 'aws_access_key_id={aws_access_key_id};aws_secret_access_key={aws_secret_access_key}'
FORMAT AS CSV;
"""
 
# Assuming you already have a connection and cursor (conn and cur) established
cur.execute(copy_cmd)
conn.commit()
 
 
# Close the cursor and connection
cur.close()
conn.close()