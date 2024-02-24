import customtkinter as ctk
import tkinter as tk
from CTkListbox import *

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("VerifyVideoGUI")
        self.root.geometry("600x400")

        # List of files
        filesListbox = CTkListbox(root)
        filesListbox.pack(fill="both", expand=False, padx=10, pady=10)
        filesListbox.insert(0, "Option 0")
        filesListbox.insert(1, "Option 1")
        filesListbox.insert(2, "Option 2")
        filesListbox.insert(3, "Option 3")
        filesListbox.insert(4, "Option 4")
        
        # Skip ffmpeg check checkbox
        self.skip_ffmpeg_check_checkbox = ctk.CTkCheckBox(root, text="Skip ffmpeg Check", onvalue="on", offvalue="off")
        self.skip_ffmpeg_check_checkbox.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        # Filter files suffix
        self.filter_checkbox_state = ctk.StringVar(value="off")
        self.suffix_var = ctk.StringVar(value="_new")
        self.filter_suffix_checkbox = ctk.CTkCheckBox(root, text="Filter out files with suffix ", command=self.toggle_filter_checkbox, variable=self.filter_checkbox_state, onvalue="on", offvalue="off")
        self.filter_suffix_entry = ctk.CTkEntry(root, textvariable=self.suffix_var, placeholder_text="_new", state="disabled")
        self.filter_suffix_checkbox.place(relx=0.4, rely=0.6, anchor=ctk.CENTER)
        self.filter_suffix_entry.place(relx=0.7, rely=0.6, anchor=ctk.CENTER)
        
        # Verify Button
        self.verify_button = ctk.CTkButton(root, text="Verify Video", command=self.on_verify_button_clicked)
        self.verify_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

    def toggle_filter_checkbox(self):
        if self.filter_suffix_checkbox.get() == "on":
            self.filter_suffix_entry.configure(state="normal")
            print("checkbox enabled")
        else:
            self.filter_suffix_entry.configure(state="disabled")
            print("checkbox disabled")

    def on_verify_button_clicked(self):
        # Assuming the video path is predefined or obtained through another UI component
        print("button pressed")