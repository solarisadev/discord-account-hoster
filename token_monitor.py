import requests
import json
import time
import logging

# Load config from config.json
with open('config.json') as f:
    config = json.load(f)

# Set up logging
logging.basicConfig(
    filename=config['log_file'],
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Load tokens from tokens.txt
with open('tokens.txt') as f:
    tokens = [line.strip() for line in f.readlines() if line.strip()]

# Function to check token status
def check_token_status(token):
    headers = {
        'Authorization': token
    }
    try:
        response = requests.get('https://discord.com/api/v10/users/@me', headers=headers)
        if response.status_code == 200:
            return "Valid"
        elif response.status_code == 401:
            return "Invalid"
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"

# Main monitoring loop
def monitor_tokens():
    while True:
        for token in tokens:
            status = check_token_status(token)
            logging.info(f"Token: {token[:10]}... - Status: {status}")
            print(f"Token: {token[:10]}... - Status: {status}")
        time.sleep(config['check_interval'])

# Run the monitor
if __name__ == '__main__':
    monitor_tokens()
