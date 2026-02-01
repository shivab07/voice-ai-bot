from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import os
from groq import Groq

# Load environment variables
load_dotenv()

# Create Flask app FIRST
app = Flask(__name__)

# Create Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question")
    print("QUESTION:", question)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   # ✅ CURRENT WORKING MODEL
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
    )

    answer = response.choices[0].message.content
    print("ANSWER:", answer)

    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
