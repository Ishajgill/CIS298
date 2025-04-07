import requests

# In memory cache (key = input phrase + lang combo)
_translation_cache = {}  #(pvt variable dont use outside module)

def translate(text, source_lang='auto', target_lang='es'):
    text = text.strip()
    if not text:
        return ""

    cache_key = f"{source_lang}:{target_lang}:{text.lower()}"

    # Check if translation is already cached
    if cache_key in _translation_cache:
        return _translation_cache[cache_key]

    url = "https://libretranslate.com/translate"
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }

    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        translated = response.json()["translatedText"]
        _translation_cache[cache_key] = translated  # Cache the result
        return translated
    except Exception as e:
        return f"[Translation Error] {e}"
