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
    download_info = os.getenv('DOWNLOAD_URLS').split(';')

    for info in download_info:
        file_path, download_url = info.split(':', 1)
        file_name = os.path.basename(file_path)
        message = f"【GigaFile（ギガファイル）便】\nURL：{download_url}\nファイル名：{file_name}"
        send_slack_message(slack_channel, message)
