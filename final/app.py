from flask import Flask, request, jsonify, send_file
from openai import OpenAI
import pyttsx3
import os

app = Flask(__name__)
client = OpenAI()
audio_file = 'output.mp3'

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def send_message(message_log):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=message_log
    )
    return completion.choices[0].message.content

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history
    user_message = request.json['message']
    conversation_history.append({"role": "user", "content": user_message})
    response = send_message(conversation_history)
    conversation_history.append({"role": "assistant", "content": response})
    return jsonify({"response": response})

@app.route('/convert', methods=['POST'])
def convert():
    text = request.json['text']
    engine = pyttsx3.init()
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    return send_file(audio_file, as_attachment=False, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(debug=True)
