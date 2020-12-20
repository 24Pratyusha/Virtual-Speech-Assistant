import speech_recognition as sr
import pyaudio
import playsound
import webbrowser
import time
import datetime
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        stranger_speak("Good morning Boss")
    elif hour>=12 and hour<4:
        stranger_speak("Good afternoon Boss")
    else:
        stranger_speak("Good evening Boss")

    stranger_speak("I am your Assistant Stranger")

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            stranger_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            stranger_speak('Sorry Boss, I did not get that...can you repeat that again?')
        except sr.RequestError:
            stranger_speak('Sorry Boss, my speech service is down..')
        return voice_data

def stranger_speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1,10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        stranger_speak('My name is Stranger.I am your Assistant.')
    if 'who am I' in voice_data:
        stranger_speak('You are my boss,Pratyusha Cheepu')
    if 'what time is it' in voice_data:
        stranger_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        stranger_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location you want to search?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        stranger_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

time.sleep(0.1)
w = wishMe()
stranger_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
