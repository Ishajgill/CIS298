
from deep_translator import GoogleTranslator
from langdetect import detect

def translate(text, source_lang='auto', target_lang='es'):
    if not text.strip():
        return ""
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"[Translation Error] {e}"
