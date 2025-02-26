import requests
import time


def initiate_auth(game_uuid, device_id):
    url = "https://app.playmanity.net/api/games/auth/initiate"
    payload = {"game_uuid": game_uuid, "device_id": device_id}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["auth_id"], data["auth_url"]
    else:
        print("Error initiating authentication:", response.json())
        return None, None


def check_auth_status(auth_id):
    url = f"https://app.playmanity.net/api/games/auth/status/{auth_id}"

    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "valid":
                return data.get("token")
            elif data.get("status") == "denied":
                print("Authentication denied.")
                return None
        elif response.status_code == 404:
            print("Invalid auth_id.")
            return None

        print("Waiting for authorization...")
        time.sleep(5)  # Polling every 5 seconds


def main():
    game_uuid = "32bde2de-d225-448f-8c6a-263275d93ef2"
    device_id = "d63d00da-ed78-4eba-b531-0f556e64cd4e"

    auth_id, auth_url = initiate_auth(game_uuid, device_id)

    if auth_id and auth_url:
        print("Authorize the game here:", auth_url)
        token = check_auth_status(auth_id)
        if token:
            print("Authentication successful! Token:", token)
        else:
            print("Failed to authenticate.")


if __name__ == "__main__":
    main()