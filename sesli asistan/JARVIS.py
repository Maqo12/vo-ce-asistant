from gtts import gTTS                                                                                           
import thingsCanDo as do                                                                                           
import os                                                                                           
import webbrowser as wb                                                                                           
import smtplib                                                                                           
import random                                                                                           
import speech_recognition as sr                                                                                           
import imp                                                                                  
        
def TalkToMe(audio):                                                                                           
    print(audio)                                                                                           
    # tts = gTTS(text = audio, lang = "en")                                                                                           
    # tts.save("audio.mp3")                                                                                           
    # os.system("audio.mp3")                                                                                           
        
def TakeInput():                                                                                           
    cmmnd = input("->")                                                                                           
    return cmmnd                                                                                           
        
# def MyCommand():                                                                                           
#     r = sr.Recognizer()                                                                                           
        
#     with sr.Microphone() as source:                                                                                           
#         r.adjust_for_ambient_noise(source, duration=1)                                                                                           
#         r.pause_threshold = 1                                                                                                                                                 
#         audio = r.listen(source)                                                                                                                                                 
                                                                    
#     try:                                                                                                                                                 
#         command = r.recognize_google(audio)                                                                                                                                                 
#         print("You said " + command + "\n")                                                                                                                                                 
                                                                    
#     except sr.UnknownValueError:                                                                                                                                                 
#         Assistant(MyCommand())                                                                                                                                                 
                                                                
#     return command                                                                                                                                                 
                                                                
                                                                
def LearnLocal(filePath, funcName):                                                                                                                                                 
    t = open("keyWords.txt", "a")                                                                                                                                                 
    t.write(" "+funcName)                                                                                                                                                 
    t.close()                                                                                                                                                 
    f = open("thingsCanDo.py", "a")                                                                                                                                                 
    f.write("""                                                                                                                                                 
def {}():                                                                                                                                                 
    import JARVIS                                                                                                                                                 
    subprocess.Popen("{}")                                                                                                                                                
    JARVIS.Assistant(JARVIS.TakeInput())                                                                                                                                                 
            """.format(funcName, filePath))
    f.close()                                                      
    imp.reload(do)                                                      
                                                      
def LearnOnline(webAdress, funcName):
    t = open("keyWords.txt", "a")
    t.write(" "+funcName)
    t.close()
    f = open("thingsCanDo.py", "a")
    f.write("""
def {}():
    import JARVIS
    wb.open("{}")
    JARVIS.Assistant(JARVIS.TakeInput())
            """.format(funcName, webAdress))
    f.close()
    imp.reload(do)

def Assistant(asd):
    do.AreYouStillThere(asd)


while True:
    Assistant(TakeInput())