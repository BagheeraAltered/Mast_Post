from mastodon import Mastodon

# Set up your Mastodon instance URL and access token
instance_url = 'https://url-token'
access_token = 'token'

# Create an instance of the Mastodon API client
mastodon = Mastodon(
    access_token=access_token,
    api_base_url=instance_url
)

# Prompt the user to enter the status message
status_message = input("Enter your status message: ")

# Post the status message
mastodon.status_post(status_message)
