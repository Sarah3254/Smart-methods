
# Text to Speech Converter

## Overview

This project is a simple Text to Speech (TTS) web application that allows users to convert text input into speech and play it directly in the browser. The application is built using Flask for the backend and Python's `pyttsx3` library for text-to-speech conversion. The frontend is created with HTML and JavaScript.

## Features

- Convert text input into speech using Python's `pyttsx3` library.
- Play the converted speech directly in the browser using HTML5 `<audio>` element.
- Simple and intuitive user interface.

## Files

- `index.html`: The frontend HTML file that provides the user interface for text input and displays the converted speech.
- `app.py`: The backend Flask application that handles text-to-speech conversion and serves the audio file.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- pyttsx3


## Installation

1. **Install Dependencies**

   ```bash
   pip install flask pyttsx3
   ```

2. **Run the Flask Application**

   ```bash
   python app.py
   ```

   Access the application at `http://localhost:5000`.

## Code Explanation

- **`index.html`**: Provides the user interface, including a form for text input and an `<audio>` element to play the converted speech.
- **`app.py`**: Contains the Flask application that:
  - Serves the `index.html` file.
  - Handles POST requests to convert text to speech and save it as an audio file.
  - Serves the generated audio file to be played in the browser.

## Libraries and Tools

- [Flask](https://flask.palletsprojects.com/) - Web framework used for the backend.
- [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/) - Python library used for text-to-speech conversion.
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used for creating the frontend interface.
