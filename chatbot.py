responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm doing great! Thanks for asking.",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "help": "I can respond to simple predefined questions.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a nice day!"
    }
print("Rule-Based AI Chatbot")
print("Type 'exit' to end the conversation.")
while True:
    user_input = input("You: ")
    clean_input = user_input.lower().strip()

    if clean_input == "exit":
        print("Bot: Goodbye!")
        break

    reply = responses.get(
        clean_input,
        "I'm sorry, I don't understand that."
    )

    print("Bot:", reply)

    