import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha


engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
# print(voices[1].id)
engin.setProperty('voice', voices[0].id)


def speak(audio):  # function to speak
    engin.say(audio)
    engin.runAndWait()


def wishMe():  # fun to wish as per time
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")

    speak("I am ALBERT, your Artificial Intelligence based virtual assistant. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Please wait, sir. I am Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        speak("Not getting your query, please say that again sir")
        return "None"
    return query

def sendEmail(to, content):
    with open('pass.txt') as f:
        password = f.read()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sohamndrdstd2207@gmail.com', password)
    server.sendmail('sohamndrdstd2207@gmail.com', to, content)
    server.close()


def wolframe():
    try:
        app_id = 'RA5QGK-9W95QA2LXR'
        client = wolframalpha.Client(app_id)
        res = client.query(query)
        answer = next(res.results).text
        print(answer)
        speak(answer)
    except Exception as e:
        speak("Not getting your query, please say that again sir")
        return "None"


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        # all task assigned to EDITH

        if 'wikipedia' in query:
            speak("Seraching on wikipedia... Please wait")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia, ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening youtube for you sir")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening google for you sir")
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("Opening stackoverflow for you sir")
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:
            speak("Opening git hub for you sir")
            webbrowser.open("github.com")

        elif 'play music' in query:

            my_music = 'F:\\Songs\\My Fev'
            songs = os.listdir(my_music)
            # print(songs)
            speak("Playing music for you sir")
            os.startfile(os.path.join(my_music, songs[0]))

        elif 'the time' in query:
            curTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(curTime)
            speak(f"Sir, The time is {curTime}")


        elif 'open vs code' in query:
            vsPath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening VS Code for you sir")
            os.startfile(vsPath)


        elif 'open android studio' in query:
            andPath = "F:\\IMP Applications\\Android Studio\\bin\\studio64.exe"
            speak("Opening Android Studio for you sir")
            os.startfile(andPath)


        elif 'open ms word' in query:
            msPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("Opening MS Word for you sir")
            os.startfile(msPath)

        elif 'open whatsapp' in query:
            waPath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            speak("Opening WhatsApp for you sir")
            os.startfile(waPath)



        elif 'email to tejas' in query:
            try:
                speak("What should I say to Tejas?")
                content = takeCommand()
                to = "tejastpatil230@gmail.com"
                sendEmail(to, content)
                speak("Email has be successfully sent to Tejas")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am unable to send email to Tejas")

        elif 'email to tanvi' in query:
            try:
                speak("What should I say to Tanvi?")
                content = takeCommand()
                to = "tanviruge@gmail.com"
                sendEmail(to, content)
                speak("Email has be successfully sent to Tanvi")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am unable to send email to Tanvi")

        elif 'email to vinayak sir' in query:
            try:
                speak("What should I say to vinayak sir?")
                content = takeCommand()
                to = "vinayak.malavde@sanjayghodawatuniversity.ac.in"
                sendEmail(to, content)
                speak("Email has be successfully sent to vinayak sir")
            except Exception as e:
                print(e)
                speak("Sorry sir, I am unable to send email to vinayak sir")

        elif 'wish me' in query:
            wishMe()



        elif 'shut down yourself' in query:
            print("Ok sir, good bye")
            speak("Ok sir, good bye")
            exit()

        else:
            wolframe()
