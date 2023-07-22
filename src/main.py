from virant_func import respond
from virant_func import talk

import wikipedia
import time
import datetime
import webbrowser
import os

respond("Hi, I am Virant your personal desktop assistant")

# Assistant on continuous loop
while(1):
        respond("How can I help you?")
        text=talk().lower()
        
        if text==0:
            continue
            
        if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
            respond("Bye thank you")
            break
            
        if 'wikipedia' in text:
            respond('Searching Wikipedia')
            text =text.replace("wikipedia", "")
            results = wikipedia.summary(text, sentences=3)
            respond("According to Wikipedia")
            print(results)
            respond(results)
                  
        elif 'time' or 'what is the time' in text:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            respond(f"the time is {strTime}")     
        
        elif 'search'  in text:
            text = text.replace("search", "")
            webbrowser.open_new_tab(text)
            time.sleep(5)

        elif 'open gmail' in text:
            webbrowser.open_new_tab("https://www.gmail.com")
            respond("Gmail is open")
            time.sleep(5)
            
        elif 'open google' in text:
            webbrowser.open("www.google.com")
            respond("Google is open")
            time.sleep(5)

        elif 'open word' in text:
            respond("Opening Microsoft Word")
            os.startfile("location of ms word")

        elif 'tell me about yourself' or 'who are you' or 'what is your name' in text:
            respond("I am Virant. Personal desktop assistant")

        elif 'what can you do' in text:
            respond('I can fetch information for you and open applications')
        
        else:
           respond("Application not available")
