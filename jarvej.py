import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import os
import sys
import wikipedia


engine = pyttsx3.init('sapi5')                  # we can use voice on inbilt windos
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)        # this method is used to we can chuse the voise if we put 0 and 1 becaus we have only two voice
                                                 #in my com but we can downlod this  voise many in fucher i think like googl we can make voice;
    


def speak(audio):
    engine.say(audio)                          #this fuction is used for voice
    engine.runAndWait()
    


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good Morning!')
    elif hour>=12 and hour<18:
        speak('happy afternoon!')
    else:                                            #you can add may voice on hear in future i try to say good night but when i turn of my computer
        speak('happy evening!')                  
    
    speak(' I am jarvis sir. please tell me how may i help you')    
    
         
def myCommand():                                                 
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('sun raha huuuu bhaiii')
        r.pause_threshold=1
        audio =r.listen(source)
        
    try:
        print('recognize....')
        query = r.recognize_google_cloudc(audio, Language='en-in')
        print(f'user said :{query}\n')
        
    except Exception as e:
        #print(e)
        
        print ('say that agin please...')
        return 'Nune'
    return query


if __name__== "__main__":
    
        
    wishMe()
    while True:
        query=myCommand().lower()
        
        if 'wikipedia'in query:
            speak("searching Wikipedia...")
            query=query.replace('wikipedia','')       # i tell you replace wikipedia to blank 
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia results are')
            speak(resuls)
 