import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_slack_message(channel, message):
    slack_token = os.getenv('SLACK_BOT_TOKEN')
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Slack API Error: {e.response['error']}")

if __name__ == "__main__":
    slack_channel = os.getenv('SLACK_CHANNEL')
    download_urls = os.getenv('DOWNLOAD_URLS').split(';')

    for url in download_urls:
        message = f"Download URL: {url}"
        send_slack_message(slack_channel, message)
