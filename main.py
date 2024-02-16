from email.mime import audio
import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()

def SpeakText(command):

    engine=pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# SpeakText("Hello i am katy for your , persnal Ai assistant")

with sr.Microphone() as source2:
    r.adjust_for_ambient_noise(source2,duration=0.1)
    audio2=r.listen(source2)
    
    MyText=r.recognize_google(audio2)
    MyText=MyText.lower()
    
    print("did you say "+MyText)
    SpeakText(MyText)