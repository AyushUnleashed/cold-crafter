import google.generativeai as genai
import os
import requests
from dotenv import find_dotenv, load_dotenv
import streamlit as st
# Load environment variables from the root .env file
root_env_path = find_dotenv()
load_dotenv(root_env_path)

gemini_api_key = os.getenv('GEMINI_API_KEY') or st.secrets['GEMINI_API_KEY']
def fetch_gemini_response(user_prompt: str):
    try:
        # Configure the Google Generative AI API client
        genai.configure(api_key=gemini_api_key)

        # Create a Gemini model object
        model = genai.GenerativeModel('gemini-pro')

        # Generate a response from the model
        response = model.generate_content(user_prompt)

        # Return the generated response
        return response.text
    except Exception as e:
        print("Exception occurred while fetching response from Gemini", e)
        st.error("Oh!! , looks like LLM lost it's weights, refresh the page")
        # Handle the exception and return a 500 status code
        error_message = f"An error occurred: {str(e)}"
        return error_message


# import requests

# def fetch_gemini_response(user_prompt: str):
#     """
#     Fetches a response from the Gemini API.
#
#     Args:
#         user_prompt: The user's prompt to the AI.
#
#     Returns:
#         The AI's response to the user's prompt.
#     """
#     # Configure the request headers
#     headers = {
#         'Content-Type': 'application/json',
#     }
#
#     # Configure the request body
#     data = {
#         'prompt': {
#             'text': user_prompt,
#         },
#     }
#
#     try:
#         # Send the request to the Gemini API
#         response = requests.post(
#             'https://generativelanguage.googleapis.com/v1beta3/models/text-bison-001:generateText',
#             headers=headers,
#             json=data,
#             params={'key': os.environ['GEMINI_API_KEY']},
#         )
#
#         # Handle the response
#         if response.status_code == 200:
#             # Return the AI's response
#             return response.json()['candidates'][0]['content']
#         else:
#             # Handle the error
#             error_message = f"An error occurred: {response.text}"
#             raise Exception(error_message)
#
#     except Exception as e:
#         # Handle the exception and return a 500 status code
#         error_message = f"An error occurred: {str(e)}"
#         st.error("Oh!! , looks like LLM lost it's weights, refresh the page")
#         return error_message


if __name__ == "__main__":
    # Fetch the response from the Gemini API
    response = fetch_gemini_response("Hello maadlee")
    print(response)