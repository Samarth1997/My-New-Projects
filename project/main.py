import ctypes
import smtplib
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import json
import openai
import time
import requests
import win32com.client as wincl
import datetime
from ecapture import ecapture as ec
import sys
import pyjokes
import os
import winshell
import wikipedia


recognizer= sr.Recognizer()
engine=pyttsx3.init()
newsapi="468e6980fb174f7f98904019f4011cff"



def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time_by_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Please say the number of seconds for the timer.")
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=10)
            spoken_text = recognizer.recognize_google(audio)
            print(f"You said: {spoken_text}")
            return int(spoken_text)  # Convert spoken input to integer
        except sr.UnknownValueError:
            speak("I couldn't understand that. Could you repeat?")
            return None
        except sr.RequestError:
            speak("Sorry, there was an issue with the speech recognition service.")
            return None
        except ValueError:
            speak("Please say a valid number.")
            return None

def email(to,content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("samarthkumardineshbhaipatel@gmail.com","9327956319")
    server.sendmail("samarthkumardineshbhaipatel@gmail.com",to,content)
    server.close()
    
        
    
def process(c):

        if("open google" in c.lower()):
            speak("Here you go to google\n")
            webbrowser.open("www.google.com")    
        elif 'how are you' in c.lower():
            speak("I am fine Thank you")
            speak("How are you Sir")

        elif  "good" in c.lower() or "fine" in c.lower():
            print("You are in good spirits")
            speak("It's good to know that you're fine")  
            print(f"Debugging: c = {c}")

        elif("open google" in c.lower()):
            speak("Here you go to google\n")
            webbrowser.open("www.google.com")
        elif("open facebook" in c.lower()):
            speak("Here you go to facebook\n")
            webbrowser.open("www.facebook.com")
        elif("open youtube" in c.lower()):   
            speak("Here you go to Youtube\n")
            webbrowser.open("www.youtube.com")
        elif("open linked in" in c.lower()):
            speak("Here you go to Linkedin\n")
            webbrowser.open("www.linkedin.com")
        
        
        elif 'open stack overflow' in c.lower():
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com") 

        elif("timer" in c.lower()):
            t=None
            
            while t is None:
                t=get_time_by_speech()
            while t:
                mins, sec=divmod(t,60)
                timer= '{:02d}:{:02d}'.format(mins,sec)
                print(timer,end="\r")
                time.sleep(1)
                t-=1

            speak("Wake up this is your Alaram: ")
            # sys.exit()
        
        elif"send email" in c.lower():
            try:
                speak("what should i say")
                recognizer.adjust_for_ambient_noise(source)
                recognizer.pause_threshold = 1
                    # audio = r.listen(source)
                audio = recognizer.listen(source)
                content = recognizer.recognize_google(audio)
                print(f"Message to send: {content}")  
                speak("whom should i send:")
                to=input("enter email of recipent:")
                print(to)
                email(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("something went wrong")

        elif("fun fact" in c.lower()):
            st=''
            url = "https://uselessfacts.jsph.pl/random.json?language=en"
            
            resonse = requests.get(url)
            if resonse.status_code == 200:
                data= json.loads(resonse.text)

                useless_fact= data['text']
        
                print(useless_fact)
                speak("funfact is:")
                speak(useless_fact)

            else:
                print("failed to fetch fun facts:")
                speak("failed to fetch fun facts:") 
        
        elif "get jokes" in c.lower():
            joke=pyjokes.get_joke()
            speak("joke is:")

            speak(joke)        
            print(joke)
        elif "search" in c.lower():
            c = c.replace("search", "").strip()
            if not c.startswith("http://") and not c.startswith("https://"):
                c = "https://" + c+ ".com"
            try:
                response = requests.get(c)
                if response.status_code == 200:
                    webbrowser.open(c)
                else:
                    print("Error: Unable to reach the website.")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")
        
   
        elif c.lower().startswith("play"):
            song = c.lower().split(" ", 1)[1]
            if song in musicLibrary.music:
                link = musicLibrary.music[song]
                webbrowser.open(link)
            else:
                print(f"Song '{song}' not found in the music library.")
                speak(f"Sorry, I couldn't find the song '{song}' in the music library.")
        
        elif("weather report" in c.lower()):
            
            speak("for which city do you need weather report:")
  
            audio = recognizer.listen(source, timeout=10)
            city = recognizer.recognize_google(audio)
            print(f"Your city is: {city}")
            url1 = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key=39ZBS8KDEW7MPP7J26Z6XQMWT"
            r1=requests.get(url1)

            if r1.status_code ==200:
                data=r1.json()

                current_temp = data['currentConditions']['temp']
                city= data['resolvedAddress']
                conditions = data['currentConditions']['conditions']
                time1= data['currentConditions']['datetime']
                maxi_temp=data['days'][0]['tempmax']
                mini_temp=data['days'][0]['tempmin']
                report = f"The current temperature of {city} is {current_temp}°F with {conditions} at time{time1}. The maximum temperature of the day is {maxi_temp}°F and minimum temperature of the day is {mini_temp}"
                
                print(report)
                speak(report)

            else:
                print("failed to fetch report:")

        elif "read news" in c.lower():

            r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapi}")
            if r.status_code == 200:
                data = r.json()
            
        
            articles=data['articles']

            for article in articles:
                print(article)
                speak("news is: ")
                speak(article['title'])
            else:

                print("Failed to fetch the news articles.")        
        elif "make a note" in c.lower():

            speak("what should I write?")
            try:
                recognizer.adjust_for_ambient_noise(source)
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source)
                note = recognizer.recognize_google(audio)  
                
                with open("jarvis.txt", 'w') as f:
                    speak("Should I include the date and time?")
                    audio = recognizer.listen(source)
                    include_time = recognizer.recognize_google(audio).lower()

                    if "yes" in include_time or "sure" in include_time:
                        strTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(strTime + " - " + note + "\n")
                    else:
                        f.write(note + "\n")
                
                speak("Note saved successfully.")
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Please try again.")
            except sr.RequestError:
                speak("There seems to be an issue with the speech recognition service.")

        elif "read note" in c.lower():
            print("program is in save ")
            speak("showing notes")
            file=open("jarvis.txt","r+")
            content=file.read()
            print(content)
            speak(content)

        elif 'wikipedia' in c.lower():
            speak("searching wikipedia.....")
            c= c.replace('wikipedia',"")
            result=wikipedia.summary(c, sentences=3)
            speak("According to wikipedia..")
            print(result)
            speak(result)

        elif 'lock window' in c.lower():
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        
        elif 'delete' in c.lower():
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'time jarvis' in c.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif "camera" in c.lower() or "take a photo" in c.lower():
            speak("Say cheeez")
            ec.capture(0, "Jarvis Camera ", "img.jpg")

        elif "exit" in c.lower() or "stop" in c.lower():
            speak("Jarvis is Deactivated")
            sys.exit()
        else:
            speak("I didn't understand that command. I am taking you to Chat Gpt you can search There")
            print("I didn't understand that command. I am taking you to Chat Gpt you can search There")
            webbrowser.open("https://chat.chatbotapp.ai/auth?utm_source=GoogleAds&utm_medium=cpc&utm_campaign={campaign}&utm_id=21151825605&utm_term=160968040295&utm_content=731497268312&gad_source=1&gclid=CjwKCAiAzba9BhBhEiwA7glbajlsbQc3gVcdqV8Bsfy2ziFTwoVeg7qeI_4apcnKOcTYbfpi7A7R0xoCprAQAvD_BwE"+c)
            openai.api_key = "sk-82fcf7aadf0e4764be99225ea03f0535"



if __name__== "__main__":
    
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir !")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir !")   
  
    else:
        speak("Good Evening Sir !")  
  
    print("Hii this is Jarvis.......")
    speak("Hii this is Jarvis.......")
    print("Jarvis is Active now:")     
    speak("Jarvis is Active now:")   
    
    while (True):
        
        r=sr.Recognizer()
            
        print("Recognizing....")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
    
                print("Hii I am Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)
                # audio = r.listen(source,timeout=1,phrase_time_limit=2)
                word=r.recognize_google(audio, language ='en-in')
                print(word)

                if(word.lower() == "jarvis"):
        
                    speak("Yes how can i help you.....")
                    with sr.Microphone() as source:
                        r.pause_threshold = 1

                        audio = r.listen(source)
                        command=r.recognize_google(audio, language ='en-in')
                        
                        
                        print(f"Recognized command: {command}")
                        process(command)

                elif "no" in word.lower() or "exit" in word.lower() or "stop" in word.lower():
                
                    speak("Jarvis is Deactivated")
                    print("Jarvis is Deactivated")
                    sys.exit()
        except Exception as e:
            print("error; {0}".format(e))
