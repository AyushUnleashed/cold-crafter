# Get Company description from a link
import os
from api.gpt_api import set_system_prompt, fetch_openai_response
from api.gemini_api import fetch_gemini_response
from api.prompts import CLEAN_COMPANY_DESCRIPTION_PROMPT
from metaphor.metaphor_company_description import get_extract_from_metaphor

def prepare_llm_prompt(company_dump: str) -> str:
    # Prepare the prompt for LLM.
    set_system_prompt(CLEAN_COMPANY_DESCRIPTION_PROMPT)
    llm_prompt = f"\n ---"
    llm_prompt += f"\nCompany's Website Dump:\n{company_dump}"
    return llm_prompt


def clean_company_info_with_llm(llm_prompt):
    # Fetch llm response

    #gpt_response_text = fetch_openai_response(llm_prompt)
    gpt_response_text = fetch_gemini_response(llm_prompt)

    if gpt_response_text:

        cleaned_company_info = gpt_response_text
        return cleaned_company_info
    else:
        print("Failed to generate the email.")
        return ""


def get_company_info_from_name(company_name):
    text_content = get_extract_from_metaphor(company_name)
    return get_cleaned_info_from_scrapped_webpage(text_content)

def get_cleaned_info_from_scrapped_webpage(text_content):
    llm_prompt = prepare_llm_prompt(text_content)
    cleaned_company_info = clean_company_info_with_llm(llm_prompt)

    # Generate a filename based on the URL
    filename = os.path.join("generations", 'company_cleaned_info.txt')

    # Save the extracted text to the specified text file
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(cleaned_company_info)

    print(f'Text content saved to "{filename}"')
    return cleaned_company_info


if __name__ == '__main__':
    company_name = "metaphor systems"
    get_company_info_from_name(company_name)
