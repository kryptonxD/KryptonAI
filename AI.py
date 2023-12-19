import pyttsx3                          # pip install pyttsx3
import datetime                         # for date and time
import speech_recognition as sr         # for speech recoginition
import wikipedia                        #for searching over world
import smtplib                          #for sending emails
import webbrowser as wb                 # for web chrome
import os                               # for logout, shut down the system
import pyautogui                        #for screenshot, use command pip install pyautogui
import psutil                           #for CPU battery update, use comm pip install psutil
import pyjokes                          #for jokes
import pyaudio
engine = pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# speak("This is Krypton AI Assistant")


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

# time()

def date():
    year= int(datetime.datetime.now().year)
    month= int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's date is")
    speak(date)
    speak(month)
    speak(year)
# date()

def wishme():
    speak("Welcome back Sir!")
    
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")
    elif hour >=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("You are in the middle of the night sir!")
    speak("Krypton.AI at your service sir, please tell me how can I help you today ?")

# wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizning...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"
    return query

# takeCommand()
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)  #since gmail use 587 port
    server.ehlo()
    server.starttls()
    server.login('kryptonmemer@gmail.com', 'CaptainAmerica')
    server.sendmail('kryptonmemer@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\RITESH KUMAR\\OneDrive\\Desktop\\Programmings\\Udemy Courses\\Python AI Assistant\\AI Assitant\\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' +usage)
    battery = psutil.sensors_battery()
    speak("The battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        

        # these are the particular words which the system hear to run accordingly. Like- "time, Date, wikipedia"
        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching sir!")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = 'dsgamingislive@gmail.com'
                # sendEmail(to,content)
                speak(content)
                # speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to  send the mail")

# for searching in chrome
        elif 'search in chrome' in query:
            speak("What should I search ?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s' #check for the path of chrome in different systems
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')

# for logout, restartm shutdown the system
        elif 'logout' in query:
            os.system("shutdown -l")

        elif 'shutdown' in query:
            os.system("shutdown /s /t l")

        elif 'restart' in query:
            os.system("shutdown /r /t l") 

# for playing songs in local album, to run this code in different system you need to set the music path directory
        elif 'play songs' in query:
            songs_dir = 'D:\\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0])) 


#for keeping the interation data with the AI, just say simply, Krypton Remember that ? then the Ai will ask what should I remember and then you need to say the data which will be stored in data.txt file

        elif 'remember that' in query:  
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that " +data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        
        elif 'do you know anything' in query:
            remember =open('data.txt', 'r')
            speak("you said me to remember that" +remember.read())      #it will let the AI to speak waht the user said 

# for taking a screenshot 
        elif 'screenshot' in query:         #simply say take a screenshot
            screenshot()
            speak("I've taken a screenshot, please check it in ss.png folder")

# for battery and CPU performance
        elif 'cpu' in query:
            cpu()

# for jokes
        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            quit()
  
