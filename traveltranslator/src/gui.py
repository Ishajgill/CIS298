import customtkinter as ctk
import json
import os
from src.translator import translate
from src.tts import speak
from src.stt import listen_and_transcribe

class TravelTalkApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Travel Talk Translator")
        self.geometry("700x600")
        self.resizable(False, False)

        # Title Label
        title = ctk.CTkLabel(self, text="🌍 Travel Talk Translator", font=("Arial", 24, "bold"))
        title.pack(pady=10)

        # Country Selector
        self.country_var = ctk.StringVar(value="Spain")
        country_menu = ctk.CTkOptionMenu(self, values=["Spain", "Mexico", "Argentina"], variable=self.country_var)
        country_menu.pack(pady=5)

        # Category Buttons
        category_frame = ctk.CTkFrame(self)
        category_frame.pack(pady=10)

        for category in ["Food", "Directions", "Emergencies"]:
            btn = ctk.CTkButton(category_frame, text=category, width=120,
                                command=lambda c=category: self.load_phrases(c))
            btn.pack(side="left", padx=10)

        # Output Box
        self.output_text = ctk.CTkTextbox(self, width=600, height=250)
        self.output_text.pack(pady=10)

        # Custom Input Label
        input_label = ctk.CTkLabel(self, text="Type any sentence:")
        input_label.pack()

        # Entry field
        self.input_entry = ctk.CTkEntry(self, width=500)
        self.input_entry.pack(pady=5)

        # 📝 Translate typed text
        text_translate_btn = ctk.CTkButton(self, text="📝 Translate Text", command=self.handle_custom_translation)
        text_translate_btn.pack(pady=5)

        # 🎤 English → Spanish (voice)
        eng_to_spa_btn = ctk.CTkButton(self, text="🎤 English → Spanish (Speak)", command=self.handle_english_to_spanish_voice)
        eng_to_spa_btn.pack(pady=5)

        # 🎤 Spanish → English (voice)
        spa_to_eng_btn = ctk.CTkButton(self, text="🎤 Spanish → English (Speak)", command=self.handle_spanish_to_english_voice)
        spa_to_eng_btn.pack(pady=5)

    def load_phrases(self, category):
        self.output_text.delete("1.0", "end")

        country = self.country_var.get().lower()
        category = category.lower()
        filename = f"data/{category}_{country}.json"

        if not os.path.exists(filename):
            self.output_text.insert("end", f"No phrases found for {category.title()} in {country.title()}.\n")
            return

        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.output_text.insert("end", f"📘 {category.title()} Phrases in {country.title()}:\n\n")

        for i, phrase in enumerate(data.get("phrases", []), start=1):
            self.output_text.insert("end", f"{i}. {phrase['english']}\n   → {phrase['spanish']}\n\n")

    def handle_custom_translation(self):
        user_input = self.input_entry.get()
        if not user_input.strip():
            return

        # Detect direction based on simple Spanish keywords
        is_spanish = any(word in user_input.lower() for word in ['¿', 'el', 'la', 'cómo', 'por', 'favor'])
        target_lang = 'en' if is_spanish else 'es'

        translated = translate(user_input, source_lang='auto', target_lang=target_lang)
        self.output_text.insert("end", f"📝 You: {user_input}\n🔁 Translated: {translated}\n\n")
        speak(translated, lang=target_lang)

    def handle_english_to_spanish_voice(self):
        self.output_text.insert("end", "🎙️ Listening for English input...\n")

        user_input = listen_and_transcribe()
        self.output_text.insert("end", f"🧠 Detected: {user_input}\n")

        if user_input.startswith("["):
            return

        translated = translate(user_input, source_lang='en', target_lang='es')
        self.output_text.insert("end", f"🔁 Spanish: {translated}\n\n")
        speak(translated, lang='es')

    def handle_spanish_to_english_voice(self):
        self.output_text.insert("end", "🎙️ Listening for Spanish input...\n")

        user_input = listen_and_transcribe()
        self.output_text.insert("end", f"🧠 Detected: {user_input}\n")

        if user_input.startswith("["):
            return

        translated = translate(user_input, source_lang='es', target_lang='en')
        self.output_text.insert("end", f"🔁 English: {translated}\n\n")
        speak(translated, lang='en')
