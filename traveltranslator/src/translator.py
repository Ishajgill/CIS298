from deep_translator import GoogleTranslator


def translate(text, source_lang='auto', target_lang='es'):
    if not text.strip():
        return ""
    try:
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        return translated
    except Exception as e:
        return f"[Translation Error] {e}"

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        translated = response.json()["translatedText"]
        _translation_cache[cache_key] = translated  # Cache the result
        return translated
    except Exception as e:
        return f"[Translation Error] {e}"
