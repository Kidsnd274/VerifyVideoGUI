import customtkinter as ctk
from ui.mainwindow import MainWindow
from util.app_logic import call_verifier

def main():
    ctk.set_appearance_mode("System") # Probably want to put this in settings next time
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    MainWindow(app, call_verifier)
    app.mainloop()

if __name__ == "__main__":
    main()