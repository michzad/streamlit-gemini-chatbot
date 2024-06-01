# Chatbot using Streamlit and Gemini API

This project is a very simple chatbot built using Streamlit as the interface and the Gemini API for generating responses. The chatbot allows users to enter prompts and receive responses, with the conversation history preserved throughout the session much like any chatbot on the market. The only difference is that it feels good doing it yourself :D

#### Last Updated: June 1st, 2024

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Why?](#whyanything)

<a name="introduction"></a>
## Introduction

This project aims to create a user-friendly chatbot interface using Streamlit and the Gemini API. Users can interact with the chatbot by entering prompts, and the chatbot responds using the Gemini API. The conversation history is maintained throughout the session, providing a seamless user experience.

<a name="features"></a>
## Features

- **User-Friendly Interface**: Simple and intuitive interface built with Streamlit.
- **Conversation History**: Preserves the chat history within the session.
- **API Integration**: Uses the Gemini API to generate responses based on user prompts.
- **Real-Time Interaction**: Allows users to interact with the chatbot in real-time.

<a name="installation"></a>
## Installation

Make sure you have [Python](https://www.python.org/downloads/) installed.

Follow these steps to set up the environment and run the application:

1. Clone the Repository:
   ```bash
   git clone https://github.com/Sambonic/streamlit-gemini-chatbot
   ```
   ```bash
   cd streamlit-gemini-chatbot
   ```

2. Create a Python Virtual Environment:
```bash
python -m venv env
```

3. Activate the Virtual Environment:
- On Windows:
  ```
  env\Scripts\activate
  ```

- On macOS and Linux:
  ```
  source env/bin/activate
  ```
4. Ensure Pip is Up-to-Date:
  ```
  python.exe -m pip install --upgrade pip
  ```
5. Install Dependencies:

   ```bash
   pip install .
   ```
<a name="usage"></a>
## Usage
1. Run the Streamlit file app:

   ```bash
   streamlit run streamlit_interface.py
   ```
2. Open the app in your browser (usually at http://localhost:8501).
3. Enter your Gemini API key in the sidebar to establish the connection.
4. Enter prompts in the chat input box to interact with the chatbot.
5. View the conversation history in the app interface.

<a name="whyanything"></a>
## Why?
This feels like a very simple project and completely useless when the wider alternatives exist out there. I took this project as a learning experience to familiarize myself better with gemini's API as well as refresh my memory and update my knowledge on streamlit's latest updates. I hope to use this experience in a bigger project that would involve fine-tuning and a more structured chatbot for specific purposes.