import pyttsx3

# Initialize the TTS engine once
engine = pyttsx3.init()
engine.setProperty('rate', 140)  # Speed of speech
engine.setProperty('volume', 1.0)  # Max volume

def speak(text: str, lang: str = "es"):
    try:
        voices = engine.getProperty('voices')
        # Try to pick a voice based on language
        for voice in voices:
            if "helena" in voice.name.lower() or "sabina" in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Offline TTS Error:", e)

