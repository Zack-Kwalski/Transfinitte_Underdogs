import openai
import speech_recognition as sr
import pyttsx3
r = sr.Recognizer()

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text

print("DogGPT: Hello! How can I assist you today? (Type 'exit' to end the conversation)")
name=input("Greetings from DogGPT!! Enter your name")
while True:
    print("enter 1 for text input or 2 for voice input")
    choice=int(input())
    if choice==1:
        user_input = input(f"{name}: ")

        if user_input.lower() == "exit":
            break

        prompt = f"{name}: {user_input}\nDogGPT:"
        response = chat_with_gpt(prompt)
        print(f"DogGPT: {response}")
    
    elif choice==2:
        try:
		
		# use the microphone as source for input.
            with sr.Microphone() as source2:
                
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level 
                r.adjust_for_ambient_noise(source2, duration=0.2)
                
                #listens for the user's input 
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                #print("Did you say ",MyText)
                prompt = f"{name}: {MyText}\nDogGPT:"
                response = chat_with_gpt(prompt)
                print(f"DogGPT: {response}")
                SpeakText(response)
			
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occurred")
    else:
        print("invalid input")

