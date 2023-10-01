# Cold Crafter - Cold Email Writer

## Brief Explanation of Project

Cold Crafter is a tool designed to assist college students in generating cold emails for job applications at startups. Users can create personalized cold emails by simply uploading their resume and providing the name of the company to which they want to apply.

## How it's Built

### Tech Stack

- Python
- Streamlit (for the frontend)
- OpenAI API
- Metaphor API

### Workflow

1. **User Input**: The user starts by providing their email address. If the user hasn't previously uploaded their resume, the system prompts them to do so, and the resume text is saved.

2. **Company Name**: The user enters the name of the company they want to apply to.

3. **Metaphor API**: The Metaphor API is used to perform a keyword search to obtain the website link associated with the provided company name and to extract the HTML content of the company's website.

4. **Company Information Extraction**: The HTML content is passed to the GPT-3.5 model to extract clean and relevant company information.

5. **Email Generation**: The system combines the extracted company information with the user's resume details. Using the OpenAI API, it generates a well-crafted cold email tailored for the specific company.

6. **Frontend**: The frontend of the application is developed using Streamlit, providing an intuitive user interface for the entire process.

Copyright [2023] [Ayush Yadav]

All rights reserved.
