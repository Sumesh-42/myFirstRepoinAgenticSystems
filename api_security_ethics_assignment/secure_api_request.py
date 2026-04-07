from dotenv import load_dotenv
import os
import requests


def fetch_secure_data():
    # Load environment variables
    load_dotenv()

    # Get API key
    api_key = os.getenv("API_KEY")

    if not api_key:
        print("Error: API_KEY not found in environment variables.")
        return

    # Use a real working API (for testing)
    url = "https://jsonplaceholder.typicode.com/posts"

    # Headers (Authorization included as per assignment)
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        # Handle status codes
        if response.status_code == 200:
            print("✅ Success! Data received:\n")
            data = response.json()

            # Print only first 3 records for readability
            for item in data[:3]:
                print(item)

        elif response.status_code == 429:
            print("⚠️ Rate limit reached. Try again later.")

        else:
            print(f"❌ Request failed. Status code: {response.status_code}")

    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Check your internet or API URL.")

    except requests.exceptions.Timeout:
        print("⏳ Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"🚨 Unexpected error: {e}")


# Run script
if __name__ == "__main__":
    fetch_secure_data()