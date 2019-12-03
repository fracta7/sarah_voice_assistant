import speech_recognition as sr
import playsound  # to play saved mp3 file
from gtts import gTTS  # google text to speech
import os  # to save/open files
import wolframalpha  # to calculate strings into formula
from selenium import webdriver  # to control browser operations
import tkinter  # gui libraries
import tkinter.messagebox  # gui libraries
from PIL import Image as im
from PIL import ImageTk

from tkinter import *

top = tkinter.Tk()

top.geometry('500x480')
top.iconbitmap('ico.ico')
top.title('Sarah')
canvas = tkinter.Canvas(top, width=500, height=400)
canvas.pack()


def info_lib():
    tkinter.messagebox.showinfo("Information",
                                "Used open-source libraries:\n\nspeech_recognition - for speech recognition\nplaysound - for giving audio feedback\ngTTS - for casting text to speech\nselenium - for web drivers\n\n\nMade purely in python 3.6\n\n2019-2020")


def info_dev():
    tkinter.messagebox.showinfo("About developers",
                                "My creator is NO 'NAME' team.\nTeam members are:\n\nJavokhir Matnazarov(201912231)\nIskandar Gulyamov(201912141)\nShokhjakhon Zaynutdinov(201912220)\n\n\ne-Mail addresses:\n\nfracta7@gmail.com\nchikkenramen@gmail.com\nkhan_0220@gmail.com\n\nWoosong University\nEndicott College of International Studies\nTechnology Studies department\n\n2019-2020")


num = 1


def assistant_speaks(output):
    global num

    # num to rename every audio file
    # with different name to remove ambiguity
    num += 1
    print("Sarah : ", output)

    toSpeak = gTTS(text=output, lang='en', slow=False)
    # saving the audio file given by google text to speech
    file = str(num) + ".mp3"
    toSpeak.save(file)

    # playsound package is used to play the same file.
    playsound.playsound(file, True)
    os.remove(file)


def get_audio():
    rObject = sr.Recognizer()
    audio = ''

    with sr.Microphone() as source:
        print("Speak...")

        # recording the audio using speech recognition
        audio = rObject.listen(source, phrase_time_limit=5)
    print("Stop.")  # limit 5 secs

    try:

        text = rObject.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text

    except:

        assistant_speaks("Could not understand your request, PLease try again !")
        return 0


def process_text(input):
    try:
        if 'search' in input or 'play' in input:
            # a basic web crawler using selenium
            search_web(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Sarah. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks such as calculating sums or opening applications etcetra'''
            assistant_speaks(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "My creator is 'NO NAME' team"
            assistant_speaks(speak)
            return

        elif "can you tell a joke" in input:  # just
            speak = """i will tell a joke when you start speaking english"""
            assistant_speaks(speak)
            return

        elif "calculate" in input.lower():

            # write your wolframalpha app_id here
            app_id = "WOLFRAMALPHA_APP_ID"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return

        elif 'open' in input:

            # another function to open
            # different application availaible
            open_application(input.lower())
            return

        else:

            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search_web(input)
            else:
                return
    except:

        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            search_web(input)


# Driver Code
def start_app():
    assistant_speaks("hello how are you?")
    name = 'Human'
    name = get_audio()
    assistant_speaks("Honestly I'm a computer so I don't care ")

    while (1):

        assistant_speaks("What can i do for you?")
        text = get_audio().lower()

        if text == 0:
            continue

        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye I'm quitting " + '.')
            break

        # calling process text to process the query
        process_text(text)


def search_web(input):
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)
    driver.maximize_window()

    if 'youtube' in input.lower():

        assistant_speaks("Opening in youtube")
        indx = input.lower().split().index('youtube')
        query = input.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
        return

    elif 'wikipedia' in input.lower():

        assistant_speaks("Opening Wikipedia")
        indx = input.lower().split().index('wikipedia')
        query = input.split()[indx + 1:]
        driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
        return

    else:

        if 'google' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        elif 'search' in input:

            indx = input.lower().split().index('google')
            query = input.split()[indx + 1:]
            driver.get("https://www.google.com/search?q =" + '+'.join(query))

        else:

            driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

        return


# function used to open application
# present inside the system.
def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return

    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return

    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return

    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return

    else:

        assistant_speaks("Application not available")
        return


def faq():
    tkinter.messagebox.showinfo("Information",
                                "Frequently asked questions\n\nApp is not responding?\nTry saying command 'exit'\n\nWhat commands are available?\nOpening :\n   Chrome\n   Mozilla\n   Microsoft Office apps like Word and Excel\n\nSearching online from:\n   Youtube\n   Google\n   Wikipedia\nAlso you can ask some questions like 'Who made you?' or 'Can you tell a joke? and listen what it says)))\n\n\nIf You have any question You can email us, contact options are available on 'About Developers' section")


img_start = im.open("start_button.png")
ph_image_start = ImageTk.PhotoImage(img_start)

img_info = im.open("info.png")
ph_image_info = ImageTk.PhotoImage(img_info)

img_dev = im.open("dev_info.png")
ph_image_dev = ImageTk.PhotoImage(img_dev)

img_faq = im.open("faq.png")
ph_image_faq = ImageTk.PhotoImage(img_faq)

img_ico = im.open("icon.png").resize((100, 100))
ph_image_icon = ImageTk.PhotoImage(img_ico)

ICO = tkinter.Button(canvas, text=" ", image=ph_image_icon, pady=20, highlightthickness=0,
                     bd=0)

B = tkinter.Button(canvas, text=" ", command=start_app, pady=100, padx=200, image=ph_image_start, highlightthickness=0,
                   bd=0)
B1 = tkinter.Button(canvas, text=" ", command=info_lib, pady=20, padx=150, image=ph_image_info, highlightthickness=0,
                    bd=0)
B2 = tkinter.Button(canvas, text=" ", command=info_dev, pady=20, padx=150, image=ph_image_dev, highlightthickness=0,
                    bd=0)
B3 = tkinter.Button(canvas, text=" ", command=faq, pady=20, padx=150, image=ph_image_faq, highlightthickness=0, bd=0)
ICO.pack()
B.pack()
B1.pack()
B2.pack()
B3.pack()
top.mainloop()
