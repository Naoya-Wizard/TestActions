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

    # 最初のコマンドライン引数を取得（すべてのファイルパスが含まれる）
    all_file_paths = sys.argv[1]

    # 空白で分割して個々のファイルパスを取得
    file_paths = all_file_paths.split(" ")
    print(file_paths)

    for file_path in file_paths:
        print(file_path)
        download_url = upload_file(file_path)
        print(f"Uploaded file URL for {file_path}: {download_url}")
        download_info.append(f"{file_path}:{download_url}")

    # ファイル名とURLのペアをセミコロンで区切った文字列として環境変数に追加
    github_env = os.environ['GITHUB_ENV']
    with open(github_env, 'a') as file:
        file.write(f"DOWNLOAD_URLS={';'.join(download_info)}\n")
