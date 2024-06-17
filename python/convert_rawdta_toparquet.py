"""
This script converts raw DTA files to Parquet format and uploads the converted files to an AWS S3 bucket.

The script reads DTA files from a specified local directory (`../data/raw/`), converts each file to Parquet format,
and then uploads these Parquet files to a specified S3 bucket (`s3://dataverse-files-parquet/parquet/`).

Requirements:
- pandas: For reading DTA files and converting them to Parquet.
- boto3: For interacting with AWS S3 to upload the converted files.

Usage:
Ensure AWS credentials are configured properly, either through environment variables, AWS credentials file,
or AWS CLI. Then, run the script in an environment where pandas and boto3 are installed.

Note:
This script assumes that the AWS S3 bucket and the local directory with DTA files are correctly set up and accessible.
"""
import os
import pandas as pd
import boto3
from botocore.exceptions import NoCredentialsError

def convert_dta_to_parquet(dta_path, parquet_path):
    """
    Convert DTA files to Parquet and upload to S3.
    """
    # Ensure the output directory exists
    if not os.path.exists(parquet_path):
        os.makedirs(parquet_path)

    # AWS S3 setup
    s3_client = boto3.client('s3')
    bucket_name = 'dataverse-files-parquet'

    # Convert each DTA file in the directory
    for filename in os.listdir(dta_path):
        if filename.endswith('.dta'):
            file_path = os.path.join(dta_path, filename)
            df = pd.read_stata(file_path)
            print(df.head())
            # Convert to Parquet
            parquet_filename = filename.replace('.dta', '.parquet')
            local_parquet_path = os.path.join(parquet_path, parquet_filename)
            df.to_parquet(local_parquet_path)
            
            # Upload to S3
            try:
                s3_client.upload_file(local_parquet_path, bucket_name, f'parquet/{parquet_filename}')
                print(f'Successfully uploaded {parquet_filename} to S3.')
            except NoCredentialsError:
                print('Credentials not available for AWS S3.')
                break

if __name__ == '__main__':
    dta_path = '../data/raw/'
    parquet_path = './parquet_files'
    convert_dta_to_parquet(dta_path, parquet_path)