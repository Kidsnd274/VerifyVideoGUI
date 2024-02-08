import customtkinter
from ui.mainwindow import MainWindow

def main():
    customtkinter.set_appearance_mode("System") # Probably want to put this in settings next time
    customtkinter.set_default_color_theme("blue")
    app = customtkinter.CTk()
    MainWindow(app)
    app.mainloop()

if __name__ == "__main__":
    main()