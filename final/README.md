
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

## Installation

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set Up Environment Variables:**

   Create a `.env` file in the `final/` directory with the following content:

   ```ini
   OPENAI_API_KEY=your_openai_api_key
   ```

   Replace `your_openai_api_key` with your actual OpenAI API key.

## Running the Application

1. **Start the Flask Server:**

   ```bash
   python app.py
   ```

2. **Access the Application:**

   Open your web browser and go to `http://127.0.0.1:5000/` to interact with the Voice Interaction Assistant.

## Usage

- **Start Recording:** Click the "Start Recording" button to begin capturing voice input. The application will transcribe the spoken text, send it to the AI assistant, and display the response.
- **Voice Feedback:** The AI assistant's response will be played back as audio through the browser's audio player.

## Troubleshooting

- **API Key Issues:** Ensure your OpenAI API key is correctly set in the `.env` file.
- **Dependency Errors:** Verify that all dependencies are installed and the virtual environment is activated.
