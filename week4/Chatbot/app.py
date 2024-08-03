from flask import Flask, request, jsonify, render_template
from openai import OpenAI

client = OpenAI()

app = Flask(__name__)

# Store conversation history in a global variable
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
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    global conversation_history

    user_message = request.json['message']
    conversation_history.append({"role": "user", "content": user_message})

    response = send_message(conversation_history)
    conversation_history.append({"role": "assistant", "content": response})

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
