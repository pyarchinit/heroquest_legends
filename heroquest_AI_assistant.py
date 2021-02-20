# -*- coding: utf-8 -*-
"""
/***************************************************************************
        Heroquest's Legends by Mandor the Druid
                             -------------------
    begin                : 2021-01-02
    copyright            : (C) 2021 by Luca Mandolesi
    email                : mandoluca at gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import pyttsx3

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os
from playsound import playsound


class Heroquest_AI_assistant:
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'voices[0].id') #0 male voice 1 female voice

    def speak(text):
        engine.say(text)
        engine.runAndWait()

    def wishMe():
        hour=datetime.datetime.now().hour
        if hour>=0 and hour<12:
            speak("Hello,Good Morning")
            print("Hello,Good Morning")
        elif hour>=12 and hour<18:
            speak("Hello,Good Afternoon")
            print("Hello,Good Afternoon")
        else:
            speak("Hello,Good Evening")
            print("Hello,Good Evening")



    def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio=r.listen(source)

            try:
                statement=r.recognize_google(audio,language='en-in')
                print(f"user said:{statement}\n")

            except Exception as e:
                speak("Pardon me, please say that again")
                return "None"
            return statement

print("Loading your AI personal assistant G-One")
speak("Loading your AI personal assistant G-One")
wishMe()

if __name__=='__main__':


    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

if "good bye" in statement or "ok bye" in statement or "stop" in statement:

    speak('your personal assistant G-one is shutting down,Good bye')
    print('your personal assistant G-one is shutting down,Good bye')
    break