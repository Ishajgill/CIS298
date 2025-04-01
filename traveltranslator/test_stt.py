import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("🎙️ Say something...")
    try:
        audio = r.listen(source, timeout=5)
        print("Translating...")
        text = r.recognize_google(audio)
        print(" You said:", text)
    except sr.WaitTimeoutError:
        print(" Timed out waiting for speech.")
    except sr.UnknownValueError:
        print(" Could not understand audio.")
    except sr.RequestError as e:
        print(" API error:", e)
