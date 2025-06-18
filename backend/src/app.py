from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Did you hear about the mathematician who's afraid of negative numbers?",
    "Why did the chicken go to the séance? To talk to the other side.",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "What do you call fake spaghetti? An impasta.",
    "I would tell you a construction pun, but I'm still working on it.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "I'm on a seafood diet. I see food and I eat it.",
    "What did one wall say to the other? 'I'll meet you at the corner.'",
    "Why can't your nose be 12 inches long? Because then it would be a foot.",
    "Why did the bicycle fall over? It was two tired.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why was the math book sad? It had too many problems.",
    "I used to play piano by ear, but now I use my hands.",
    "What’s orange and sounds like a parrot? A carrot.",
    "How does a penguin build its house? Igloos it together.",
    "Why don’t programmers like nature? It has too many bugs."
]

@app.route('/joke')
def joke():
    return jsonify({"joke": random.choice(jokes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)