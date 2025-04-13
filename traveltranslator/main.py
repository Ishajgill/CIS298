import customtkinter as ctk
from src.gui import TravelTalkApp

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    app = TravelTalkApp()
    app.mainloop()

    