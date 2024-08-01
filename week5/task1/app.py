from flask import Flask, request, render_template_string, send_file
import pyttsx3
import os

app = Flask(__name__)
audio_file = 'output.mp3'

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    engine = pyttsx3.init()
    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    return render_template_string(open('index.html').read())

@app.route('/audio')
def audio():
    return send_file(audio_file, as_attachment=False)

if __name__ == '__main__':
    app.run(debug=True)
