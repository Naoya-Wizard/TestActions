import sys
from gfile import GFile
import os

def upload_file(file_path):
    # Gigafileにファイルをアップロードし、URLを取得
    uploaded_file = GFile(file_path)
    upload_response = uploaded_file.upload()
    download_url = upload_response.get_download_page()

    return download_url

def append_to_github_env(key, value):
    # GitHub Actionsの環境ファイルへのパスを取得
    github_env = os.environ['GITHUB_ENV']

    # 環境ファイルに新しい環境変数を追加
    with open(github_env, 'a') as file:
        file.write(f"{key}={value}\n")

if __name__ == "__main__":
    # コマンドライン引数から複数のファイルパスを取得
    for file_path in sys.argv[1:]:
        download_url = upload_file(file_path)
        print(f"Uploaded file URL for {file_path}: {download_url}")

        # GitHub Actionsの環境変数としてダウンロードURLを保存
        append_to_github_env(f"DOWNLOAD_URL_{file_path}", download_url)
