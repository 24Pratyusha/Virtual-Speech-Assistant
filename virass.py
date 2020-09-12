import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

warnings.filterwarnings('Ignore')

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Say something!')
        audio = r.listen(source)

    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said: '+data)
    except sr.UnknownValuaError:
        print('Google Speech Recognition could not understand the audio,unknown error')
    except sr.RequestError as e:
        print('Request results from google speech recognition service error'+ e)

    return data