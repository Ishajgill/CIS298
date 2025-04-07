import pyttsx3

# Initialize the TTS engine once
engine = pyttsx3.init()
engine.setProperty('rate', 140)     # Speed of speech
engine.setProperty('volume', 1.0)   # Max volume

# Language code to keyword mapping (can expand this list)
LANG_VOICE_HINTS = {
    "en": ["english"],
    "es": ["spanish", "español", "helena", "sabina"],
    "fr": ["french", "français"],
    "it": ["italian", "italiano"],
    "de": ["german", "deutsch"],
    "pt": ["portuguese", "português"],
    "ru": ["russian", "русский"],
    "zh": ["chinese", "中文"],
    "ar": ["arabic", "عربي"],
    "hi": ["hindi", "हिन्दी"],
    "ja": ["japanese", "日本語"],
    "ko": ["korean", "한국어"],
    "tr": ["turkish", "türkçe"]
}

def speak(text: str, lang: str = "en"):
    try:
        voices = engine.getProperty('voices')
        selected_voice = None
        voice_hints = LANG_VOICE_HINTS.get(lang, [])

        for voice in voices:
            for hint in voice_hints:
                if hint.lower() in voice.name.lower() or hint.lower() in voice.id.lower():
                    selected_voice = voice
                    break
            if selected_voice:
                break

        if selected_voice:
            engine.setProperty('voice', selected_voice.id)
        else:
            print(f"[!] No exact voice match for language '{lang}', using default voice.")

        engine.say(text)
        engine.runAndWait()

    except Exception as e:
        print("Offline TTS Error:", e)
