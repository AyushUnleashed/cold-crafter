def fetch_user_info_from_email(email):
    # Construct the filename based on the email address
    filename = f"generations/{email}_resume.txt"

    try:
        # Open the file and read its contents
        with open(filename, 'r',encoding='utf-8') as file:
            content = file.read()

        # Split the content into words
        words = content.split()

        # Take only the first 400 words
        selected_words = ' '.join(words[:400])

        print(selected_words)
        return selected_words
    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Resume file for {email} not found.")
        return f"Resume file for {email} not found."
    except Exception as e:
        # Handle other exceptions if they occur
        error = f"An error occurred: {str(e)}"
        print(error)
        return error


if __name__ == "__main__":
    fetch_user_info_from_email("yashrajshukla48@gmail.com")