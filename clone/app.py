from flask import Flask, render_template, request
import openai
import pyttsx3
import speech_recognition as sr

app = Flask(__name__)

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

r = sr.Recognizer()

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

@app.route("/", methods=["GET", "POST"])
def home():
    response = None

    if request.method == "POST":
        user_input = request.form["userinput"]
        name = "User"  # You can customize this if you want to capture the user's name
        prompt = f"{name}: {user_input}\nDogGPT:"
        response = chat_with_gpt(prompt)
        SpeakText(response)

    return render_template("index.html", response=response)


if __name__ == "__main__":
    app.run(debug=True)
