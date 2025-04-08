
import speech_recognition as sr

def listen_and_transcribe(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("*** Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=timeout)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "[No speech detected]"
        except sr.UnknownValueError:
            return "[Sorry, could not understand you]"
        except sr.RequestError as e:
            return f"[API error – {e}]"
