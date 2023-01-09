import requests
import tqdm

# Set the API endpoint URL
url = ""

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

        # Send the request
        response = requests.post(url, headers=headers, data=data)

        # Write the response to the text file
        out_file.write(response.text)

print("Requests complete!")