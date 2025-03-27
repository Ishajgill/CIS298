
import speech_recognition as sr

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print(" Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "[No speech detected]"
        except sr.UnknownValueError:
            return "[Sorry, could not understand you]"
        except sr.RequestError:
            return "[API error – check internet]"
