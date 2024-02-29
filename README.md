# Nexus: A Conversational AI with File Upload Functionality

## Table of Contents
1. [Project Overview](https://github.com/GitCoder052023/Nexus?tab=readme-ov-file#project-overview)
2. [Features](https://github.com/GitCoder052023/Nexus?tab=readme-ov-file#features)
3. [Requirements](https://github.com/GitCoder052023/Nexus?tab=readme-ov-file#requirements)
4. [Installation](https://github.com/GitCoder052023/Nexus?tab=readme-ov-file#installation)
5. [Usage](https://github.com/GitCoder052023/Nexus?tab=readme-ov-file#usage)
    - [Running the Application](https://github.com/GitCoder052023/Nexus?tab=readme-ov-file#running-the-application)
    - [Chat Interaction](https://github.com/GitCoder052023/Nexus?tab=readme-ov-file#chat-interaction)

# Project Overview

Nexus is a user-friendly conversational AI application that empowers users to engage in natural language interactions and process information from uploaded files. It leverages the capabilities of the GoogleGenerativeAI model to deliver intelligent and informative responses.

# Features

- Conversational interface: Interact with Nexus through a text-based chat interface, asking questions and receiving comprehensive answers.
- File upload and processing: Upload text, CSV, or PDF documents to provide additional context or information for Nexus to analyze and incorporate into its responses.
- Customizable theme: The GUI offers a dark theme for a visually appealing experience.

# Requirements 

- **Python 3.7+ :** (or compatible version)
- **customtkinter:** ```pip install customtkinter```
- **PyPDF2:** ```pip install PyPDF2```
- **langchain:** ```pip install langchain```
- **Google Gemini API key:** Get your Gemini API key from [this link](https://aistudio.google.com/app/apikey)
- **replace with your own in key variable:** Replace ```key``` variable's value from your original API key **(In Nexus.py)**

# Installation

1. Make sure you have Python and the required libraries installed (see **Requirements**)
2. Clone or download the repository.
3. Install the necessary dependencies within the project directory:

```bash
pip install -r requirements.txt
```

# Usage

## Running the Application

1. Open a terminal or command prompt and navigate to the project directory.
2. Run the application using the following command:

```bash
python Nexus.py
```

## Chat Interaction

1. Click the "Upload Document" button.
2. In the file selection dialog, choose the desired file (text, CSV, or PDF).
3. Once the application launches anf file uploaded, type your questions or prompts in the "Ask question here" entry field.
4. Press the "Ask" button or press Enter to send your query.
5. Nexus will process your question and respond in the chat window above.
