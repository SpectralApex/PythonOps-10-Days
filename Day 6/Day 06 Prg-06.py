# Simple Chatbot
def respond(msg):
    if "hello" in msg.lower(): return "Hi there, operator!"
    elif "bye" in msg.lower(): return "Mission complete. Logging out."
    else: return "Processing..."

while True:
    user = input("You: ")
    if user.lower() == "exit": break
    print("Bot:", respond(user))
