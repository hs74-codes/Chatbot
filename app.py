from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Chatbot logic
def get_chatbot_response(user_input):
    user_input = user_input.strip().lower()

    if user_input in ["exit", "quit"]:
        return "Chat session ended. Bye! 👋"
    elif user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "what are you doing":
        return "Texting you."
    elif user_input == "kaise ho":
        return "Main theek hoon, aap kaise ho?"
    elif user_input == "who are you":
        return "I am ChatBot."
    elif "weather" in user_input:
        return "I can't check the weather right now, but it's always sunny in the code world! ☀️"
    elif "help" in user_input:
        return "You can ask me things like 'how are you', 'who are you', or say 'bye'."
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day! 👋"
    else:
        return "Sorry, I don't understand that."

# Home page route
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint for chatbot
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    bot_response = get_chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
