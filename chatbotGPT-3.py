import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to interact with GPT-3 and get responses
def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=150  # Adjust the response length as needed
    )
    return response.choices[0].text.strip()

# Main loop for the chat bot
print("Chat Bot: Hi! How can I assist you today? (Type 'exit' to quit)")

conversation_history = []

while True:
    user_input = input("You: ")

    # Add the user's message to the conversation history
    conversation_history.append(f"You: {user_input}")

    if user_input.lower() == 'exit':
        print("Chat Bot: Goodbye!")
        break

    # Get the chat bot's response based on the conversation history
    chat_prompt = "\n".join(conversation_history)
    chat_bot_response = chat_with_gpt3(chat_prompt)

    # Extract and display the chat bot's response
    bot_response = chat_bot_response[len(chat_prompt):].strip()
    print("Chat Bot:", bot_response)

    # Add the chat bot's response to the conversation history
    conversation_history.append(f"Chat Bot: {bot_response}")
