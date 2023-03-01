import datetime
import sys
import os
import wikipedia
import pyttsx3
import webbrowser
#import datetime
import speech_recognition as sr
import wikipedia
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Moring AD")
    elif hour>=12 and hour<18:
        speak("Good Afternoon AD")
    else:
        speak("Good Evening")
    speak("Ongalukaga   Naa enna pannalam ")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("wait for few min")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
    except Exception as e :
        print(e)
        speak("say that again please")
    return query


    

if __name__=="__main__":
    wishme()
    while True:


        query=takecommand().lower()

        if "wikipedia" in query:
            speak("Searching in wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open code" in query:
            codepath= "C:\\Users\\Adhokshajan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif "open chrome" in query:
            codepath1= "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codepath1)
        elif "the time" in query:
            time=datetime.datetime.now().strftime("%H:%M:%S")
            speak(time)
        elif "down" in query:
            speak("ok sir ")
            os.system("shutdown  /s /t 06")
            speak("iam going to shutdown the computer sir")
            speak("bye sir , have a good time ")
            sys.exit()

        elif "quit" in query :
            speak("quiting sir ")
            break
        elif "exit" in query :
            exit()



