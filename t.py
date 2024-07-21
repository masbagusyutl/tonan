import time
import json
import requests
from urllib.parse import unquote

def read_accounts(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def extract_username(init_data):
    decoded_data = unquote(init_data)
    start = decoded_data.find('"username":"') + len('"username":"')
    end = decoded_data.find('"', start)
    return decoded_data[start:end]

def perform_task(init_data):
    url = "https://b7zj6wf7falelnlhlz2r5y6r5e0zibdi.lambda-url.us-east-1.on.aws/"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "445",
        "Content-Type": "application/json",
        "Host": "b7zj6wf7falelnlhlz2r5y6r5e0zibdi.lambda-url.us-east-1.on.aws",
        "Origin": "https://twa.photo-cdn.net",
        "Pragma": "no-cache",
        "Referer": "https://twa.photo-cdn.net/",
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0"
    }
    payload = {
        "action": "wallet.save.balance",
        "initData": init_data
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code

def countdown(seconds):
    while seconds:
        hrs, secs = divmod(seconds, 3600)
        mins, secs = divmod(secs, 60)
        time_format = f"{hrs:02}:{mins:02}:{secs:02}"
        print(f"Countdown: {time_format}", end="\r")
        time.sleep(1)
        seconds -= 1

def main():
    accounts = read_accounts('data.txt')
    total_accounts = len(accounts)
    
    for i, account in enumerate(accounts):
        username = extract_username(account.strip())
        print(f"Processing account {i + 1}/{total_accounts}: {username}")
        status_code = perform_task(account.strip())
        print(f"Task completed for {username} with status code: {status_code}")
        time.sleep(5)  # Delay before switching to the next account
    
    print("All accounts processed. Starting 10800 seconds countdown.")
    countdown(10800)
    print("Restarting script...")
    main()

if __name__ == "__main__":
    main()
