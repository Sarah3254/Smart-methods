from openai import OpenAI
client = OpenAI()

def send_message(message_log):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=message_log  
    )

    # If no response with text is found, return the first response's content (which may be empty)
    return completion.choices[0].message.content

# Main function that runs the chatbot
def main():
    # Initialize the conversation history with a message from the chatbot
    message_log = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("AI assistant: Goodbye!")
            break
        
        # Add the user's input to the message log
        message_log.append({"role": "user", "content": user_input})
        
        # Get the assistant's response
        response = send_message(message_log)
        
        # Add the assistant's response to the message log
        message_log.append({"role": "assistant", "content": response})
        
        # Print the assistant's response
        print(f"AI assistant: {response}")

if __name__ == "__main__":
    main()
