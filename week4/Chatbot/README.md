
# Chatbot Project

This project is a simple chatbot implementation using OpenAI's GPT-4 model. The project includes both a command-line interface (CLI) chatbot and a web-based chatbot.

## Project Structure

```
Chatbot/
├── app.py              # Python code to create a web page for the chatbot
├── test.py             # Python code to run the chatbot on the command line
├── .env                # Environment variables (e.g., OpenAI API key)
├── .gitignore          # Git ignore file
├── templates/
│   └── index.html      # HTML template for the web-based chatbot
└── images
    └── cmd chatbot.png    # Images of the chatbot running in the command line
    └── webpage chatbot.png # Images of the chatbot running in the web page
```

## Installation and Setup

### Account setup

1. **Create an OpenAI account** or sign in. Next, navigate to the API key page and "Create new secret key", optionally naming the key. Make sure to save this somewhere safe and do not share it with anyone.

### Quickstart language selection

Python is a popular programming language that is commonly used for data applications, web development, and many other programming tasks due to its ease of use. OpenAI provides a custom Python library which makes working with the OpenAI API in Python simple and efficient.

### Step 1: Setting up Python

1. **Install Python**

   To use the OpenAI Python library, you will need to ensure you have Python installed. Some computers come with Python pre-installed while others require that you set it up yourself. To test if you have Python installed, you can navigate to your Terminal or Command line:

   - **MacOS**: Open Terminal: You can find it in the Applications folder or search for it using Spotlight (Command + Space).
   - **Windows**: Open Command Prompt: You can find it by searching "cmd" in the start menu.

   Next, enter the word `python` and then press return/enter. If you enter into the Python interpreter, then you have Python installed on your computer already and you can go to the next step. If you get an error message that says something like "Error: command python not found", you likely need to install Python and make it available in your terminal/command line.

   To download Python, head to the official Python website and download the latest version. To use the OpenAI Python library, you need at least Python 3.7.1 or newer. If you are installing Python for the first time, you can follow the official Python installation guide for beginners.

### Step 2: Set up a virtual environment (optional)

Once you have Python installed, it is a good practice to create a virtual python environment to install the OpenAI Python library. Virtual environments provide a clean working space for your Python packages to be installed so that you do not have conflicts with other libraries you install for other projects. You are not required to use a virtual environment, so skip to step 3 if you do not want to set one up.

To create a virtual environment, Python supplies a built-in `venv` module which provides the basic functionality needed for the virtual environment. Running the command below will create a virtual environment named "openai-env" inside the current folder you have selected in your terminal/command line:

```bash
python -m venv openai-env
```

Once you’ve created the virtual environment, you need to activate it. On Windows, run:

```bash
openai-env\Scripts\activate
```

On Unix or MacOS, run:

```bash
source openai-env/bin/activate
```

You should see the terminal/command line interface change slightly after you activate the virtual environment, it should now show "openai-env" to the left of the cursor input section. For more details on working with virtual environments, please refer to the official Python documentation.

### Step 3: Install the OpenAI Python library

Once you have Python 3.7.1 or newer installed and (optionally) set up a virtual environment, the OpenAI Python library can be installed. From the terminal/command line, run:

```bash
pip install --upgrade openai
```

Once this completes, running `pip list` will show you the Python libraries you have installed in your current environment, which should confirm that the OpenAI Python library was successfully installed.

### Step 4: Set up your API key

To set up your API key for a single project, you can create a local `.env` file which contains the API key and then explicitly use that API key with the Python code shown in the steps to come.

Start by going to the project folder you want to create the `.env` file in.

In order for your `.env` file to be ignored by version control, create a `.gitignore` file in the root of your project directory. Add a line with `.env` on it which will make sure your API key or other secrets are not accidentally shared via version control.

Once you create the `.gitignore` and `.env` files using the terminal or an integrated development environment (IDE), copy your secret API key and set it as the `OPENAI_API_KEY` in your `.env` file. If you haven't created a secret key yet, you can do so on the API key page.

The `.env` file should look like the following:

```plaintext
# Once you add your API key below, make sure to not share it with anyone! The API key should remain private.

OPENAI_API_KEY=abc123
```

The API key can be imported by running the code below:

```python
from openai import OpenAI

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )
```

## Running the Command-Line Chatbot

1. **Run the chatbot on the command line:**
   ```bash
   python test.py
   ```

2. **Usage:**
   - Enter your message and press Enter.
   - The chatbot will respond to your message.

## Running the Web-Based Chatbot

1. **Run the Flask application:**
   ```bash
   python app.py
   ```

2. **Open your browser and navigate to:**
   ```
   http://127.0.0.1:5000
   ```

3. **Usage:**
   - Type your message in the text area and click the "Send" button.
   - The chatbot will respond to your message, and the conversation will be displayed in the chatbox.

## Screenshots

### Command-Line Chatbot
![Command-Line Chatbot](https://github.com/Sarah3254/Smart-methods/blob/main/week4/Chatbot/images/cmd%20chatbot.png)

### Web-Based Chatbot
![Web-Based Chatbot](https://github.com/Sarah3254/Smart-methods/blob/main/week4/Chatbot/images/web%20chatbot.png)
