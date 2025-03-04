import requests
import time
import sys
import logging
import json

# Налаштування логування
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Константи API
API_BASE_URL = "https://app.playmanity.net/api"
DEFAULT_GAME_UUID = "32bde2de-d225-448f-8c6a-263275d93ef2"
DEFAULT_DEVICE_ID = "d63d00da-ed78-4eba-b531-0f556e64cd4e"

# ---------------------------------> check the SDK for python
def check_sdk():
    try:
        logging.info("PSDK: Trying to access SDK files")
        import PlaymanityAPI.SDK
    except Exception as e:
        logging.error(f"PSDK: Failed to initialize ({e})")
        sys.exit(1)

# ---------------------------------> API functions
def initiate_auth(game_uuid, device_id):
    url = f"{API_BASE_URL}/games/auth/initiate"
    payload = {"game_uuid": game_uuid, "device_id": device_id}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("auth_id"), data.get("auth_url")
    except requests.RequestException as e:
        logging.error(f"Error initiating authentication: {e}")
        return None, None

def check_auth_status(auth_id):
    url = f"{API_BASE_URL}/games/auth/status/{auth_id}"

    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            status = data.get("status")
            if status == "valid":
                return data.get("token")
            elif status == "denied":
                logging.warning("Authentication denied.")
                return None
        except requests.RequestException as e:
            logging.error(f"Error checking auth status: {e}")
            return None

        logging.info("Waiting for authorization...")
        time.sleep(5)

def get_ad(auth_token, game_uuid):
    url = f"{API_BASE_URL}/advertisements"
    payload = {"gameUuid": game_uuid, "authToken": auth_token}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        ad_data = response.json()
        if ad_data and "ad" in ad_data:
            return ad_data["ad"]
        else:
            logging.error("No advertisement data found in response.")
            return None
    except requests.RequestException as e:
        logging.error(f"Error fetching ad: {e}")
        return None

def main(game_uuid=None, device_id=None):
    game_uuid = game_uuid or DEFAULT_GAME_UUID
    device_id = device_id or DEFAULT_DEVICE_ID

    auth_id, auth_url = initiate_auth(game_uuid, device_id)
    if auth_id and auth_url:
        logging.info(f"Authorize the game here: {auth_url}")
        token = check_auth_status(auth_id)
        if token:
            logging.info("Authentication successful!")
            ad = get_ad(token, game_uuid)
            if ad:
                logging.info(f"Advertisement received: {json.dumps(ad, indent=4)}")
            else:
                logging.warning("No ads available.")
        else:
            logging.error("Failed to authenticate.")

if __name__ == "__main__":
    main()
