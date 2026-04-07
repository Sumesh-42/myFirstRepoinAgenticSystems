import requests
import pandas as pd


def fetch_and_process_data():
    url = "https://jsonplaceholder.typicode.com/posts"

    # Fetch data
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"API request failed with status {response.status_code}")

    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Cleaning
    df.rename(columns={"userId": "user_id"}, inplace=True)
    df.drop(columns=["id"], inplace=True)

    # Feature engineering
    df["post_length"] = df["body"].apply(len)

    return df