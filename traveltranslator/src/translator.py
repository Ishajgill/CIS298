
from deep_translator import GoogleTranslator

def translate_to_spanish(text):
    if not text.strip():
        return ""
    try:
        translated = GoogleTranslator(source='auto', target='es').translate(text)
        return translated
    except Exception as e:
        return f"[Translation Error] {e}"
