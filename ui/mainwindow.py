import customtkinter

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("VerifyVideoGUI")
        self.root.geometry("600x400")

        # List of files
        

        # Button
        self.verify_button = customtkinter.CTkButton(root, text="Verify Video", command=self.on_verify_button_clicked)
        self.verify_button.place(relx=0.5, rely=0.7, anchor=customtkinter.CENTER)

    def on_verify_button_clicked(self):
        # Assuming the video path is predefined or obtained through another UI component
        print("button pressed")

# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# ignore_ffmpeg_check = customtkinter.CTkCheckBox(master=app)
# button = customtkinter.CTkButton(master=app, text="Verify", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)