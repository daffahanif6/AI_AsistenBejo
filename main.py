import speech_recognition as sr
import re
import webbrowser
import datetime

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >=0 and currentH <12:
        print("Selamat Pagi Daff")
    if currentH >=12 and currentH <18:
        print("Selamat Siang Daff")
    if currentH >=18 and currentH <0:
        print("Selamat Malam Daff")

greetMe()

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('Daffa : ' + command + '\n')

    except sr.UnknownValueError:
        print('Bejo : Yang keras, gue gak denger bro!')
        command = myCommand();

    return command

def assistant(command):
    "if statements for executing commands"

    if 'hello bro' in command:
        print('Bejo : Hello Daff, Ada apa nich?')

    elif 'open google' in command:
        reg_ex = re.search('google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'where am i' in command:
        reg_ex = re.search('where (.*)', command)
        url = 'https://www.google.com/maps/@-7.7598868,110.4090196,21z'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        
    elif 'open waskita amikom' in command:
        reg_ex = re.search('web (.*)', command)
        url = 'https://waskita.amikom.ac.id/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain + '.com'
            webbrowser.open(url)
            print('Done!')
        else:
            pass
          
    elif 'thank you' in command:
            print('Bejo : Bye Daffa. Happy to help you. Have a good day.')
            exit()
while True:
    assistant(myCommand())
    