from gtts import gTTS
import speech_recognition as sr
import os
import pygame
import random
import webbrowser
def talkToMe(audio):
    r1 = random.randint(1,10000000)
    r2 = random.randint(1,10000000)
    randfile = str(r2)+"randomtext"+str(r1) +".mp3"
    tts = gTTS(text=audio, lang='en')
    tts.save(randfile)
    pygame.mixer.init()
    pygame.mixer.music.load(randfile)
    pygame.mixer.music.play()

def assistant(command):
    if command is None:
        return talkToMe("Sorry, I didn't understand  mujhe maaf kijiye m smjh nhi paari aap jo bolna chahte hain")
    if "hi" in command:
        talkToMe("Hi, I am Vaidya. I can  help you with: \n1. Diagnose of your disease\n2. Check your Symptoms\n3. Show Yoga\n4. Fix appointment")
    elif 'i am' in command:
        return talkToMe('Aap se milke accha laga' + command[4:]+'!' )
    elif 'help me' in command:
        return talkToMe('Yes please! Hum kaise madad kr sakte hain')
    elif 'mein' in command:
        return talkToMe('kripya apni pareshani btain')
    elif 'yoga' in command:
        webbrowser.open('https://www.yogajournal.com/', new=2)
        return talkToMe('The concepts and practices of Yoga originated in India about several thousand years ago. Its founders were great Saints and Sages. The great Yogis presented rational interpretation of their experiences of Yoga and brought about a practical and scientifically sound method within every one’s reach. Yoga today, is no longer restricted to hermits, saints, and sages; it has entered into our everyday lives and has aroused a worldwide awakening and acceptance in the last few decades. The science of Yoga and its techniques have now been reoriented to suit modern sociological needs and lifestyles. Experts of various branches of medicine including modern medical sciences are realizing the role of these techniques in the prevention and mitigation of diseases and promotion of health.')
    elif 'stress' in command:
        return talkToMe('chewing gum ...well thats what I do when feel stressed')
    elif 'cholestrol' in command:
        return talkToMe('quit smoking and start eating heart-healthy food')
    else:
        return talkToMe("mujhe ye sikhaya nhi guya hai")
