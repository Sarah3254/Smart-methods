
# Voice Interaction Assistant

## Overview

The Voice Interaction Assistant is a web application that combines speech recognition, natural language processing, and text-to-speech functionalities. It allows users to interact with an AI assistant through voice input, receive responses in text, and hear those responses converted into speech.

## Project Structure

```
final/
│
├── app.py
├── .gitignore
├── .env
├── requirements.txt
└── static/
    └── index.html
```

- `app.py`: The main Flask application file containing the server-side logic for chat and text-to-speech functionalities.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `.env`: Configuration file for environment variables (e.g., API keys).
- `requirements.txt`: Lists the Python dependencies required for the project.
- `static/index.html`: The frontend HTML file with integrated JavaScript for voice recording and chat interaction.

## Installation and Setup

1. **Install Python** (if not already installed):

   - **MacOS**: Open Terminal and run `python3 --version`. If Python is not installed, download it from the [official Python website](https://www.python.org/downloads/).
   - **Windows**: Open Command Prompt and run `python --version`. If Python is not installed, download it from the [official Python website](https://www.python.org/downloads/).

2. **Set Up a Virtual Environment** (optional but recommended):

   ```bash
   python -m venv venv
   ```

   - **Activate the Virtual Environment**:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:

   Create a `.env` file in the `final/` directory with the following content:

   ```ini
   OPENAI_API_KEY=your_openai_api_key
   ```

   Replace `your_openai_api_key` with your actual OpenAI API key. Ensure this file is added to `.gitignore` to keep your API key secure.

## Running the Application

1. **Start the Flask Server**:

   ```bash
   python app.py
   ```

2. **Access the Application**:

   Open your web browser and go to `http://127.0.0.1:5000/` to interact with the Voice Interaction Assistant.

## Usage

- **Start Recording:** Click the "Start Recording" button to begin capturing voice input. The application will transcribe the spoken text, send it to the AI assistant, and display the response.
- **Voice Feedback:** The AI assistant's response will be played back as audio through the browser's audio player.

## Troubleshooting

- **API Key Issues:** Ensure your OpenAI API key is correctly set in the `.env` file.
- **Dependency Errors:** Verify that all dependencies are installed.
