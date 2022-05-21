
from typing import Text
import speech_recognition as sr
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard
from pygame import mixer


name = "guideon"
listener = sr.Recognizer()
engine = pyttsx3.init()
 
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate', 145)

def talk(text):
    engine.say(text)
    engine.runAndWait()
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="en")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')

    except:
        pass
    return rec       

def run_guideon():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        print("Reproducing" + music)
        talk("Reproducing" + music)
        pywhatkit.playonyt(music)


if __name__ == '__main__':
    run_guideon()

while True:
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce','')
        print = ("Reproducing " + music)
        talk =("Reproducing" + music)
        pywhatkit.playonyt(music)
    elif 'search' in rec:
        search = rec.replace('search','')
        wikipedia.set_lang("en")
        wiki = wikipedia.summary(search, 2)
        print(search +": " + wiki)
        talk(wiki)


