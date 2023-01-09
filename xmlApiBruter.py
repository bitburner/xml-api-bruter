import boto3
import requests
import tqdm

# Set the API endpoint URL
url = ""

# Create an AWS session
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY'
)

# Create an AWS STS client
sts_client = session.client('sts')

# Get temporary AWS credentials
credentials = sts_client.get_session_token()

# Extract the access key, secret key, and session token
access_key = credentials['Credentials']['AccessKeyId']
secret_key = credentials['Credentials']['SecretAccessKey']
session_token = credentials['Credentials']['SessionToken']

# Open the text file containing the POST data
with open('post_data.txt', 'r') as f:
    # Read the lines of the file into a list
    lines = f.readlines()

# Open a text file for writing the responses
with open('responses.txt', 'w') as out_file:
    # Iterate through the list of POST data
    for data in tqdm.tqdm(lines):
        # Set the SOAP action
        headers = {'SOAPAction': 'urn:exampleAction'}

        # Set the AWS authentication headers
        headers['x-amz-security-token'] = session_token
        headers['x-amz-access-key'] = access_key
        headers['x-amz-secret-key'] = secret_key

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Write the response to the text file
        out_file.write(response.text)

print("Requests complete!")
