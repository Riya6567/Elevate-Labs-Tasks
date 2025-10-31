# Simple Rule-Based Chatbot using if-else

print("🤖 Hello! I am ChatSpark, your friendly chatbot.")
print("Type 'bye' anytime to exit.\n")

while True:
    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("ChatSpark: Hello there! How can I help you today?")
    
    elif "how are you" in user_input:
        print("ChatSpark: I'm just a program, but I'm doing great! What about you?")
    
    elif "your name" in user_input:
        print("ChatSpark: I’m ChatSpark — created using Python if-else logic! 😄")
    
    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"ChatSpark: The current time is {current_time}.")
    
    elif "date" in user_input:
        from datetime import datetime
        current_date = datetime.now().strftime("%B %d, %Y")
        print(f"ChatSpark: Today’s date is {current_date}.")
    
    elif "creator" in user_input or "made you" in user_input:
        print("ChatSpark: I was created by a Python programmer!")
    
    elif "bye" in user_input:
        print("ChatSpark: Goodbye! Have a great day! 👋")
        break
    
    else:
        print("ChatSpark: I'm not sure I understand. Could you please rephrase?")
