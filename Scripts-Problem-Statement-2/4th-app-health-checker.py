import requests
import time
import logging

# Set up logging
logging.basicConfig(filename='app_health_checker.log', level=logging.INFO)

# Define application URL and expected HTTP status code
APP_URL = 'https://example.com'
EXPECTED_STATUS_CODE = 200

def check_app_status():
    try:
        response = requests.get(APP_URL, timeout=5)
        if response.status_code == EXPECTED_STATUS_CODE:
            return 'up'
        else:
            return 'down'
    except requests.exceptions.RequestException as e:
        logging.error(f'Error checking app status: {e}')
        return 'down'

def main():
    while True:
        app_status = check_app_status()
        if app_status == 'up':
            logging.info(f'App is up and running (HTTP {EXPECTED_STATUS_CODE})')
        else:
            logging.error(f'App is down or not responding (HTTP {response.status_code})')
        time.sleep(60)  # Check every 1 minute

if __name__ == '__main__':
    main()