import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import psutil
import platform

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")    

    else:
        speak("Good Evening!")  

    speak("I am your Personal Assistant. Please tell me how may I help you") 

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

# Function to open apps
def open_app(app_name):
    try:
        if app_name == "notepad":
            os.system("notepad.exe")
        elif app_name == "calculator":
            os.system("calc.exe")
        elif app_name == "paint":
            os.system("mspaint.exe")
        else:
            speak(f"Sorry, I cannot open {app_name}")
    except Exception as e:
        speak(f"Sorry, I couldn't open {app_name}. {str(e)}")

# Function to get system information
def system_info():
    system = platform.system()
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    storage = psutil.disk_usage('/').percent
    speak(f"Your system is running on {system}. CPU usage is {cpu}%, memory usage is {memory}%, and disk usage is {storage}%.")

# Function to search the web
def search_web(query):
    search_query = query.replace("search", "")
    webbrowser.open(f"https://www.google.com/search?q={search_query}")


if __name__=="__main__" :
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"the time is {strTime}")
        elif 'open' in query:
            app_name = query.replace("open", "").strip()
            open_app(app_name)
        elif 'system info' in query:
            system_info()
        elif 'search' in query:
            search_web(query)
        elif 'quit' in query:
            exit()