print("=" * 50)
print("🤖 Welcome to the Rule-Based Chatbot")
print("Type 'bye' to exit")
print("=" * 50)

while True:
    user = input("\nYou: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am a Rule-Based Chatbot.")

    elif "course" in user:
        print("Bot: We offer AI, Data Science, and Computer Science courses.")

    elif "fee" in user:
        print("Bot: The fee details are available at the admissions office.")

    elif "admission" in user:
        print("Bot: Admissions are open. You can apply online.")

    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")