import speech_recognition as sr
import pygame

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
