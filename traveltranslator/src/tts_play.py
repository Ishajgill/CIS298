import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import pygame
import os

# Setup pygame for audio
pygame.mixer.init()

def recognize_speech(language_code='ar'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language=language_code)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results:", e)
    return None

def translate_text(text, dest_lang='en'):
    translator = Translator()
    translated = translator.translate(text, dest=dest_lang)
    print("Translated to:", translated.text)
    return translated.text

def speak_text(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = "output.mp3"
    tts.save(filename)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    os.remove(filename)

source_lang = 'ar'
target_lang = 'es'

spoken_text = recognize_speech(language_code=source_lang)
if spoken_text:
    translated = translate_text(spoken_text, dest_lang=target_lang)
    speak_text(translated, lang=target_lang)
