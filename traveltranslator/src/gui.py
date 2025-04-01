import customtkinter as ctk
import json
import re
from collections import defaultdict
from src.translator import translate
from src.tts import speak
from src.stt import listen_and_transcribe

class TravelTalkApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Travel Talk Translator")
        self.geometry("700x600")
        self.resizable(False, False)

        self.translation_counts = defaultdict(int)
        self.custom_dictionary = {
            "restroom": "bathroom",
            "cellphone": "mobile phone",
            "gas": "petrol"
        }

        # Title Label
        ctk.CTkLabel(self, text="🌍 Travel Talk Translator", font=("Arial", 24, "bold")).pack(pady=10)

        # Country Dropdown
        self.country_var = ctk.StringVar(value="Spain")
        ctk.CTkOptionMenu(self, values=["Spain", "Mexico", "Argentina"], variable=self.country_var).pack(pady=5)

        # Category Buttons
        category_frame = ctk.CTkFrame(self)
        category_frame.pack(pady=10)
        for category in ["Food", "Directions", "Emergencies"]:
            ctk.CTkButton(category_frame, text=category, width=120,
                          command=lambda c=category: self.load_phrases(c)).pack(side="left", padx=10)

        # Output Box
        self.output_text = ctk.CTkTextbox(self, width=600, height=200)
        self.output_text.pack(pady=10)

        # Input Field
        ctk.CTkLabel(self, text="Type any sentence:").pack()
        self.input_entry = ctk.CTkEntry(self, width=500)
        self.input_entry.pack(pady=5)

        # Action Buttons
        ctk.CTkButton(self, text="📝 Translate Text", command=self.handle_custom_translation).pack(pady=5)
        ctk.CTkButton(self, text="🎤 English → Spanish (Speak)", command=self.handle_english_to_spanish_voice).pack(
            pady=5)
        ctk.CTkButton(self, text="🎤 Spanish → English (Speak)", command=self.handle_spanish_to_english_voice).pack(
            pady=5)
        ctk.CTkButton(self, text="📊 Show Translation Stats", command=self.show_translation_stats).pack(pady=5)

    def clean_input(self, text):
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        for key, value in self.custom_dictionary.items():
            text = text.replace(key, value)
        return text

    def is_spanish(self, text):
        spanish_keywords = {'el', 'la', 'de', 'que', 'por', 'favor', 'gracias'}
        words = text.lower().split()
        matches = sum(1 for word in words if word in spanish_keywords)
        return matches > len(words) // 3

    def load_phrases(self, category):
        self.output_text.delete("1.0", "end")
        country = self.country_var.get().lower()
        filename = f"data/{category.lower()}_{country}.json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            self.output_text.insert("end", f"No phrases found for {category.title()} in {country.title()}.")
            return

        self.output_text.insert("end", f"📘 {category.title()} Phrases in {country.title()}:\n\n")
        for i, phrase in enumerate(data.get("phrases", []), start=1):
            self.output_text.insert("end", f"{i}. {phrase['english']}\n   → {phrase['spanish']}\n\n")

    def handle_custom_translation(self):
        user_input = self.input_entry.get()
        if not user_input.strip(): return
        cleaned = self.clean_input(user_input)
        is_span = self.is_spanish(cleaned)
        target_lang = 'en' if is_span else 'es'
        translated = translate(cleaned, source_lang='auto', target_lang=target_lang)
        self.translation_counts[cleaned] += 1
        self.output_text.insert("end", f"You: {user_input}\n🔁 Translated: {translated}\n\n")
        speak(translated, lang=target_lang)

    def handle_english_to_spanish_voice(self):
        self.output_text.insert("end", "🎙️ Listening for English input...\n")
        user_input = listen_and_transcribe()
        self.output_text.insert("end", f"🧠 Detected: {user_input}\n")
        if user_input.startswith("["): return
        cleaned = self.clean_input(user_input)
        translated = translate(cleaned, source_lang='en', target_lang='es')
        self.translation_counts[cleaned] += 1
        self.output_text.insert("end", f"🔁 Spanish: {translated}\n\n")
        speak(translated, lang='es')

    def handle_spanish_to_english_voice(self):
        self.output_text.insert("end", "🎙️ Listening for Spanish input...\n")
        user_input = listen_and_transcribe()
        self.output_text.insert("end", f"🧠 Detected: {user_input}\n")
        if user_input.startswith("["): return
        cleaned = self.clean_input(user_input)
        translated = translate(cleaned, source_lang='es', target_lang='en')
        self.translation_counts[cleaned] += 1
        self.output_text.insert("end", f"🔁 English: {translated}\n\n")
        speak(translated, lang='en')

    def show_translation_stats(self):
        self.output_text.delete("1.0", "end")
        if not self.translation_counts:
            self.output_text.insert("end", "No translations yet.\n")
            return
        self.output_text.insert("end", "📊 Translation Frequency:\n\n")
        sorted_counts = sorted(self.translation_counts.items(), key=lambda x: x[1], reverse=True)
        for i, (phrase, count) in enumerate(sorted_counts, start=1):
            self.output_text.insert("end", f"{i}. '{phrase}' → used {count} time(s)\n")