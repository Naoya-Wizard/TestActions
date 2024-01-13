import sys
from gfile import GFile
import os

def upload_file(file_path):
    # Gigafileにファイルをアップロードし、URLを取得
    uploaded_file = GFile(file_path)
    upload_response = uploaded_file.upload()
    download_url = upload_response.get_download_page()

    return download_url

if __name__ == "__main__":
    download_info = []

    # コマンドライン引数から複数のファイルパスを取得
    print(sys.argv[1:])
    for file_path in sys.argv[1:]:
        download_url = upload_file(file_path)
        print(f"Uploaded file URL for {file_path}: {download_url}")
        download_info.append(f"{file_path}:{download_url}")

    # ファイル名とURLのペアをセミコロンで区切った文字列として環境変数に追加
    github_env = os.environ['GITHUB_ENV']
    with open(github_env, 'a') as file:
        file.write(f"DOWNLOAD_INFO={';'.join(download_info)}\n")
