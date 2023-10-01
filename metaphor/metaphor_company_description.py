import os
from dotenv import load_dotenv
import requests
import json
import streamlit as st
# Load environment variables from the .env file
load_dotenv()

# Retrieve the Metaphor API key from the environment variables
METAPHOR_API_KEY = os.getenv("METAPHOR_API_KEY") or st.secrets["METAPHOR_API_KEY"]

def search_metaphor(company_name: str):
    url = "https://api.metaphor.systems/search"

    query = {
        "query": company_name,
        "type": "keyword",
        "useAutoprompt": True,
        "numResults": 1
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": METAPHOR_API_KEY
    }

    try:
        response = requests.post(url, data=json.dumps(query), headers=headers)
        response_data = response.json()
        print(response_data)

        if "results" in response_data:
            results = response_data["results"]
            if results:
                metaphor_id = results[0]["id"]
                return metaphor_id
    except Exception as e:
        print("Error during Metaphor search:", str(e))

    return None

def get_extract_from_metaphor(company_name: str):
    metaphor_id = search_metaphor(company_name)

    if metaphor_id:
        url = f"https://api.metaphor.systems/contents?ids={metaphor_id}"

        headers = {
            "accept": "application/json",
            "x-api-key": METAPHOR_API_KEY
        }

        try:
            response = requests.get(url, headers=headers)
            response_data = response.json()
            print(response_data)

            if "contents" in response_data:
                contents = response_data["contents"]
                if contents:
                    extract = contents[0]["extract"]
                    return extract
        except Exception as e:
            print("Error while fetching metaphor content:", str(e))

    return None

def main():
    company_name = "Appstractor"  # Replace with the company name you want to search
    # print(search_metaphor(company_name))
    extract = get_extract_from_metaphor(company_name)

    if extract:
        # print("Extract for the company:")
        print(extract)
    else:
        print("Metaphor data not found for the company.")

if __name__ == "__main__":
    main()