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
        self.geometry("700x680")
        self.resizable(False, False)

        # Appearance and Theme
        #made appearance status into variable to be switchable
        self.current_ld_mode = "Dark"
        ctk.set_appearance_mode(self.current_ld_mode)
        ctk.set_default_color_theme("green")
        # counting actual number times a word is spoken or typed
        self.translation_counts = defaultdict(int)
        self.custom_dictionary = {
            "restroom": "bathroom",
            "cellphone": "mobile phone",
            "gas": "petrol"
        }
        #Quick Phrase Tab
        self.country_to_lang = {
            "Arabic": "Arabic",
            "France": "French",
            "Germany": "German",
            "Italy": "Italian",
            "Mexico": "Spanish",
            "Russia": "Russian",
            "Chinese": "Chinese",
            "Korea": "Korean"
        }

        # Title - switched it to make it switchable via Light/Dark Mode button
        self.Title = ctk.CTkLabel(
            self,
            text="\U0001F30D Personal Travel Talk/Text Translator",
            font=("Arial", 24, "bold"),
            text_color="#ffffff"
        )
        self.Title.pack(pady=10)

        # Country + Category Toolbar
        toolbar_frame = ctk.CTkFrame(self, fg_color="transparent")
        toolbar_frame.pack(pady=10)

        self.country_var = ctk.StringVar(value="Mexico")
        self.country_var.trace("w", self.sync_language_with_country)
        ctk.CTkOptionMenu(
            toolbar_frame,
            values=list(self.country_to_lang.keys()),
            variable=self.country_var,
            fg_color="#ffffff",
            text_color="black",
            button_color="#2982d7"
        ).pack(side="left", padx=10)

        colors = {
            "Food": "#5fc234",
            "Directions and Transportation": "#ffed03",
            "Emergencies": "#e52020"
        }
        for category in ["Food", "Directions and Transportation", "Emergencies"]:
            ctk.CTkButton(
                toolbar_frame,
                text=category,
                width=120,
                fg_color=colors[category],
                text_color="black",
                hover_color="#333",
                command=lambda c=category: self.load_phrases(c)
            ).pack(side="left", padx=10)

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

        lang_frame = ctk.CTkFrame(self, fg_color="#444444")
        lang_frame.pack(pady=5)

        #set from color to manually to white
        ctk.CTkLabel(lang_frame, text="From:", text_color="white").pack(side="left", padx=(0, 5))
        self.source_lang_menu = ctk.CTkOptionMenu(
            lang_frame, values=list(self.languages.keys()), variable=self.from_lang_var,
            command=lambda _: self.update_voice_button_text(),
            fg_color="#2196F3"
        )
        self.source_lang_menu.pack(side="left", padx=10)

        # Swap Button
        swap_button = ctk.CTkButton(
            lang_frame,
            text="\U0001F501",
            width=40,
            height=32,
            command=self.swap_languages,
            fg_color="#FFD700",
            text_color="black"
        )
        swap_button.pack(side="left", padx=5)

        #set To color manually to white
        ctk.CTkLabel(lang_frame, text="To:", text_color="white").pack(side="left", padx=(20, 5))
        self.target_lang_menu = ctk.CTkOptionMenu(
            lang_frame, values=list(self.languages.keys()), variable=self.to_lang_var,
            command=lambda _: self.update_voice_button_text(),
            fg_color="#E91E63"
        )
        self.target_lang_menu.pack(side="left", padx=10)

        self.output_text = ctk.CTkTextbox(self, width=600, height=200, fg_color="#F7FFF7", text_color="#000")
        self.output_text.pack(pady=10)

        #split Type any sentence configuration to be switchable via Light/Dark Mode button
        self.TAS = ctk.CTkLabel(self, text="Type any sentence:", text_color="#ffffff")
        self.TAS.pack()

        self.input_entry = ctk.CTkEntry(self, width=500, fg_color="white", text_color="black")
        self.input_entry.pack(pady=5)

        ctk.CTkButton(
            self,
            text="\U0001F501 Translate Text",
            command=self.handle_custom_translation,
            fg_color="#007BFF",
            text_color="white",
        ).pack(pady=5)

        self.voice_button = ctk.CTkButton(self, text="", command=self.handle_voice_translation, fg_color="#007BFF")
        self.voice_button.pack(pady=5)
        # all the translations done so far
        ctk.CTkButton(
            self,
            text="\u2728 Show Translation Stats",
            command=self.show_translation_stats,
            fg_color="#007BFF",
            text_color="white"
        ).pack(pady=5)

        #Light/Dark Mode button to switch UI Base colors
        def ld_mode():
            if self.current_ld_mode == "Dark":
                self.current_ld_mode = "Light"
                ctk.set_appearance_mode(self.current_ld_mode)
                self.Title.configure(text_color="#000000")
                self.TAS.configure(text_color="#000000")

            else:
                self.current_ld_mode = "Dark"
                ctk.set_appearance_mode(self.current_ld_mode)
                self.Title.configure(text_color="#ffffff")
                self.TAS.configure(text_color="#ffffff")
        self.switch_mode = ctk.CTkButton(self, text="🌗 Light/Dark Mode", command=ld_mode, fg_color="#007BFF" )
        self.switch_mode.pack(pady=5)

        self.update_voice_button_text()

        ctk.CTkButton(
            self,
            text="\U0001F5D1 Clear Translation History",
            command=self.clear_translation_history,
            fg_color="#007BFF",
            text_color="white",
        ).pack(pady=5)

    def clear_translation_history(self):
        self.translation_counts.clear()
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", "Translation history has been cleared.\n")
        self.after(2000, lambda: self.output_text.delete("1.0", "end"))  # clears after 2 seconds


    def swap_languages(self):
        from_lang = self.from_lang_var.get()
        to_lang = self.to_lang_var.get()
        self.from_lang_var.set(to_lang)
        self.to_lang_var.set(from_lang)
        self.update_voice_button_text()

    def update_voice_button_text(self):
        from_lang = self.from_lang_var.get()
        to_lang = self.to_lang_var.get()
        self.voice_button.configure(text=f"\U0001F3A4 {from_lang} \u2192 {to_lang} (Speak)")

    #Called automatically when the user changes the selected country.
    def sync_language_with_country(self, *args):
        country = self.country_var.get()
        if country in self.country_to_lang:
            self.to_lang_var.set(self.country_to_lang[country])
            self.update_voice_button_text()

    #removing punctuation
    def clean_input(self, text):
        text = text.lower().strip()
        text = re.sub(r'[^\w\s]', '', text)
        for key, value in self.custom_dictionary.items():
            text = text.replace(key, value)
        return text

    def load_phrases(self, category):
        self.output_text.delete("1.0", "end")
        country = self.country_var.get().lower()
        language = self.country_to_lang.get(country.title())  # Get corresponding language
        if not language:
            self.output_text.insert("end", f"Language for {country.title()} not found.\n")
            return

        filename = f"data/{category.replace(' ', '_').lower()}_{country.lower()}.json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            self.output_text.insert("end", f"No phrases found for {category.title()} in {country.title()}.")
            return

        self.output_text.insert("end", f"\U0001F4D8 {category.title()} Phrases in {country.title()}:\n\n")
        for i, phrase in enumerate(data.get("phrases", []), start=1):
            translated_phrase = phrase.get(language.lower())  # e.g. 'italian', 'spanish', etc.
            if translated_phrase:
                self.output_text.insert("end", f"{i}. {phrase['english']}\n   \u2192 {translated_phrase}\n\n")
            else:
                self.output_text.insert("end", f"{i}. {phrase['english']}\n   \u2192 Translation not available\n\n")

    # Translates user input from the "From" language to the "To" language,
    # speaks the result aloud, and displays it in the output text area.
    def handle_custom_translation(self):
        user_input = self.input_entry.get()
        if not user_input.strip(): return
        cleaned = self.clean_input(user_input)
        source_lang = self.languages[self.from_lang_var.get()]
        target_lang = self.languages[self.to_lang_var.get()]
        translated = translate(cleaned, source_lang=source_lang, target_lang=target_lang)
        self.translation_counts[cleaned] += 1
        self.output_text.insert("end", f"You: {user_input}\n\U0001F501 Translated: {translated}\n\n")
        speak(translated, lang=target_lang)
        self.input_entry.delete(0, "end")

    # Normalizes the speech (lowercased, punctuation removed, custom substitutions)
    def handle_voice_translation(self):
        from_lang_key = self.from_lang_var.get()
        to_lang_key = self.to_lang_var.get()
        from_lang_code = self.languages[from_lang_key]
        to_lang_code = self.languages[to_lang_key]

        self.output_text.insert("end", f"\U0001F3A4 Listening for {from_lang_key} input...\n")
        user_input = listen_and_transcribe()
        self.output_text.insert("end", f"\U0001F9E0 Detected: {user_input}\n")
        if user_input.startswith("["): return
        cleaned = self.clean_input(user_input)
        translated = translate(cleaned, source_lang=from_lang_code, target_lang=to_lang_code)
        self.translation_counts[cleaned] += 1
        self.output_text.insert("end", f"\U0001F501 {to_lang_key}: {translated}\n\n")
        speak(translated, lang=to_lang_code)

    def show_translation_stats(self):
        self.output_text.delete("1.0", "end")
        if not self.translation_counts:
            self.output_text.insert("end", "No translations yet.\n")
            return
        self.output_text.insert("end", "\U0001F4CA Translation Frequency:\n\n")
        sorted_counts = sorted(self.translation_counts.items(), key=lambda x: x[1], reverse=True)
        for i, (phrase, count) in enumerate(sorted_counts, start=1):
            self.output_text.insert("end", f"{i}. '{phrase}' \u2192 used {count} time(s)\n")

if __name__ == "__main__":
    app = TravelTalkApp()
    app.mainloop()
