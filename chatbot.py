from datetime import datetime

def chatbot():
    print("Chatbot: Hello! I'm a simple rule-based chatbot.")
    print("Type 'bye' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower().strip()

        # Rule 1: 
        if user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hi there! How can I assist you today?")
        
        # Rule 2: 
        elif "weather" in user_input:
            print("Chatbot: The weather is sunny and pleasant today!")

        # Rule 3: 
        elif "your name" in user_input:
            print("Chatbot: I'm ChatSimple, your friendly chatbot assistant.")
        
        # Rule 4: 
        elif "time" in user_input:
            now = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {now}.")
        
        # Rule 5: 
        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm doing great!  How about you?")
        
        # Rule 6:
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        # Rule 7:
        else:
            print("Chatbot: I'm not sure how to respond to that. Can you try asking something else?")

# Start the chatbot
if __name__ == "__main__":
    chatbot()

