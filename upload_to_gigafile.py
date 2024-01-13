import sys
from gfile import GFile

def upload_file(file_path):
    # Gigafileにファイルをアップロードし、URLを取得
    uploaded_file = GFile(file_path)
    upload_response = uploaded_file.upload()
    download_url = upload_response.get_download_page()

    return download_url

if __name__ == "__main__":
    # コマンドライン引数から複数のファイルパスを取得
    for file_path in sys.argv[1:]:
        download_url = upload_file(file_path)
        print(f"Uploaded file URL for {file_path}: {download_url}")
