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

        self.country_to_lang = {
            "Italy": "Italian",
            "Mexico": "Spanish",
            "France": "French"
        }

        # Title
        ctk.CTkLabel(self, text="🌍 Travel Talk Translator", font=("Arial", 24, "bold")).pack(pady=10)

        # Country Dropdown
        self.country_var = ctk.StringVar(value="Mexico")
        self.country_var.trace("w", self.sync_language_with_country)
        ctk.CTkOptionMenu(self, values=list(self.country_to_lang.keys()), variable=self.country_var).pack(pady=5)

        self.languages = {
            "English": "en",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Italian": "it",
            "Portuguese": "pt",
            "Russian": "ru",
            "Chinese (Simplified)": "zh",
            "Arabic": "ar",
            "Hindi": "hi",
            "Japanese": "ja",
            "Korean": "ko",
            "Turkish": "tr"
        }

        self.from_lang_var = ctk.StringVar(value="English")
        self.to_lang_var = ctk.StringVar(value="Spanish")

        lang_frame = ctk.CTkFrame(self)
        lang_frame.pack(pady=5)

        ctk.CTkLabel(lang_frame, text="From:").pack(side="left", padx=(0, 5))
        self.source_lang_menu = ctk.CTkOptionMenu(
            lang_frame, values=list(self.languages.keys()), variable=self.from_lang_var,
            command=lambda _: self.update_voice_button_text()
        )
        self.source_lang_menu.pack(side="left", padx=10)

        ctk.CTkLabel(lang_frame, text="To:").pack(side="left", padx=(20, 5))
        self.target_lang_menu = ctk.CTkOptionMenu(
            lang_frame, values=list(self.languages.keys()), variable=self.to_lang_var,
            command=lambda _: self.update_voice_button_text()
        )
        self.target_lang_menu.pack(side="left", padx=10)

        category_frame = ctk.CTkFrame(self)
        category_frame.pack(pady=10)
        for category in ["Food", "Directions", "Emergencies"]:
            ctk.CTkButton(category_frame, text=category, width=120,
                          command=lambda c=category: self.load_phrases(c)).pack(side="left", padx=10)

        self.output_text = ctk.CTkTextbox(self, width=600, height=200)
        self.output_text.pack(pady=10)

        ctk.CTkLabel(self, text="Type any sentence:").pack()
        self.input_entry = ctk.CTkEntry(self, width=500)
        self.input_entry.pack(pady=5)

        self.voice_button = ctk.CTkButton(self, text="", command=self.handle_voice_translation)
        self.voice_button.pack(pady=5)

        ctk.CTkButton(self, text=" Show Translation Stats", command=self.show_translation_stats).pack(pady=5)

        self.update_voice_button_text()

    def update_voice_button_text(self):
        from_lang = self.from_lang_var.get()
        to_lang = self.to_lang_var.get()
        self.voice_button.configure(text=f"🎤 {from_lang} → {to_lang} (Speak)")

    def sync_language_with_country(self, *args):
        country = self.country_var.get()
        if country in self.country_to_lang:
            self.to_lang_var.set(self.country_to_lang[country])
            self.update_voice_button_text()

    def clean_input(self, text):
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        for key, value in self.custom_dictionary.items():
            text = text.replace(key, value)
        return text

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
        source_lang = self.languages[self.from_lang_var.get()]
        target_lang = self.languages[self.to_lang_var.get()]
        translated = translate(cleaned, source_lang=source_lang, target_lang=target_lang)
        self.translation_counts[cleaned] += 1
        self.output_text.insert("end", f"You: {user_input}\n🔁 Translated: {translated}\n\n")
        speak(translated, lang=target_lang)

    def handle_voice_translation(self):
        from_lang_key = self.from_lang_var.get()
        to_lang_key = self.to_lang_var.get()
        from_lang_code = self.languages[from_lang_key]
        to_lang_code = self.languages[to_lang_key]

        self.output_text.insert("end", f"🎤 Listening for {from_lang_key} input...\n")
        user_input = listen_and_transcribe()
        self.output_text.insert("end", f"🧠 Detected: {user_input}\n")
        if user_input.startswith("["): return
        cleaned = self.clean_input(user_input)
        translated = translate(cleaned, source_lang=from_lang_code, target_lang=to_lang_code)
        self.translation_counts[cleaned] += 1
        self.output_text.insert("end", f"🔁 {to_lang_key}: {translated}\n\n")
        speak(translated, lang=to_lang_code)

    def show_translation_stats(self):
        self.output_text.delete("1.0", "end")
        if not self.translation_counts:
            self.output_text.insert("end", "No translations yet.\n")
            return
        self.output_text.insert("end", "📊 Translation Frequency:\n\n")
        sorted_counts = sorted(self.translation_counts.items(), key=lambda x: x[1], reverse=True)
        for i, (phrase, count) in enumerate(sorted_counts, start=1):
            self.output_text.insert("end", f"{i}. '{phrase}' → used {count} time(s)\n")


if __name__ == "__main__":
    app = TravelTalkApp()
    app.mainloop()
