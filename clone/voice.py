import speech_recognition as sr
from gtts import gTTS
from langdetect import detect
import os

def recognize_speech():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Speak in Hindi, Tamil, or English:")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("I could not understand your speech.")
            return ""
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return ""

def speak_response(response_text, target_language):
    if response_text:
        tts = gTTS(text=response_text, lang=target_language)
        tts.save("response.mp3")
        os.system("mpg123 response.mp3")

if __name__ == "__main__":
    while True:
        user_input = recognize_speech()
        response = "I could not understand your speech."

        if user_input:
            # Detect the language of the user's input
            detected_language = detect(user_input)

            # Define responses for each language
            responses = {
                "en": "You spoke in English: " + user_input,
                "hi": "आपने हिंदी में कहा: " + user_input,
                "ta": "நீங்கள் தமிழில் பேசினீர்கள்: " + user_input,
            }

            # Choose the appropriate response based on the detected language
            response = responses.get(detected_language, response)

        speak_response(response, detected_language)
