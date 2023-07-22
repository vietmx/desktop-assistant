import speech_recognition as sr
from gtts import gTTS
import playsound
import os

# talk function for audio input
def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        input.pause_threshold = 0.7
        audio=input.listen(source)
        data = ""
        try:
            data=input.recognize_google(audio, language='en-in')
            print("Your question is, " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
        return data  


# respond function for assistant response
def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    playsound.playsound(file, True)
    os.remove(file)
