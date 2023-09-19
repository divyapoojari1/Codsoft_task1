import re
rules = {
    r'hello|hi|hey': 'Hello there!',
    r'how are you|how are you doing': 'I am just a computer program, but I am functioning well. How can I assist you?',
    r'what is your name|who are you': 'I am a simple chatbot.',
    r'bye|goodbye|exit': 'Goodbye! If you have more questions in the future, feel free to ask.',
    r'(.*)\bhelp\b(.*)': 'I can assist you with general information. Please ask me a question.',
    r'(.*)\bweather\b(.*)': 'I do not have access to real-time data. You can check the weather on a weather website or app.',
    r'(.*)\btime\b(.*)': 'I do not have access to real-time data. You can check the time on your device.',
    r'(.*)\bthanks|thank you\b(.*)': 'You\'re welcome! If you have more questions, feel free to ask.',
}
def chatbot_response(user_input):
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response
    return "I'm sorry, I don't understand that."


print("Hello! I'm your chatbot. You can start a conversation or say 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
