import customtkinter as ctk
from ui.mainwindow import MainWindow

def main():
    ctk.set_appearance_mode("System") # Probably want to put this in settings next time
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    MainWindow(app)
    app.mainloop()

if __name__ == "__main__":
    main()