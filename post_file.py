import time
from mastodon import Mastodon

# Set up your Mastodon instance URL and access token
instance_url = 'https://url.com'
access_token = 'TPKEM'

# Create an instance of the Mastodon API client
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=instance_url
)

# Prompt the user to enter the file path
file_path = input("Enter the path to the file: ")

# Open the file
with open(file_path, 'r') as file:
    # Read the lines from the file
    lines = file.readlines()

    # Iterate over each line
    for line in lines:
        # Strip leading/trailing whitespace and newline characters
        status_message = line.strip()

        # Post the status message
        mastodon.status_post(status_message)

        # Wait for 120 seconds before posting the next line
        time.sleep(120)
