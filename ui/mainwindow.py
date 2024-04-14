import customtkinter as ctk
import tkinter as tk
from CTkListbox import *
from tkinter import filedialog
from util.verify_options_object import VerifyOptionsObject

class MainWindow:
    def __init__(self, root, verifier_function):
        self.root = root
        self.root.title("VerifyVideoGUI")
        self.root.geometry("600x400")
        self.verifier_function = verifier_function

        self.check_path = ctk.StringVar(value="")
        self.path_entry = ctk.CTkEntry(root, textvariable=self.check_path)
        # self.path_entry.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)
        self.path_entry.pack()
        
        self.browse_button = ctk.CTkButton(root, text="Browse", command=self.browseFile)
        # self.browse_button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)
        self.browse_button.pack()
        
        # Skip ffmpeg check checkbox
        self.skip_ffmpeg_check_checkbox = ctk.CTkCheckBox(root, text="Skip ffmpeg Check", onvalue="on", offvalue="off")
        self.skip_ffmpeg_check_checkbox.pack()
        # self.skip_ffmpeg_check_checkbox.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        
        # Filter files suffix
        self.filter_checkbox_state = ctk.StringVar(value="off")
        self.suffix_var = ctk.StringVar(value="_new")
        self.filter_suffix_checkbox = ctk.CTkCheckBox(root, text="Filter out files with suffix ", command=self.toggle_filter_checkbox, variable=self.filter_checkbox_state, onvalue="on", offvalue="off")
        self.filter_suffix_entry = ctk.CTkEntry(root, textvariable=self.suffix_var, placeholder_text="_new", state="disabled")
        self.filter_suffix_checkbox.pack()
        # self.filter_suffix_checkbox.place(relx=0.4, rely=0.6, anchor=ctk.CENTER)
        # self.filter_suffix_entry.place(relx=0.7, rely=0.6, anchor=ctk.CENTER)
        
        # Verify Button
        self.verify_button = ctk.CTkButton(root, text="Verify Video", command=self.on_verify_button_clicked)
        # self.verify_button.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)
        self.verify_button.pack()

    def browseFile(self):
        file_path = filedialog.askdirectory()
        if file_path:
            # Update the entry with the selected file path
            self.check_path.set(file_path)

    def toggle_filter_checkbox(self):
        if self.filter_suffix_checkbox.get() == "on":
            self.filter_suffix_entry.configure(state="normal")
            print("checkbox enabled")
        else:
            self.filter_suffix_entry.configure(state="disabled")
            print("checkbox disabled")

    def on_verify_button_clicked(self):
        folder_path = self.check_path.get()
        ignore_ffmpeg = self.skip_ffmpeg_check_checkbox.get() == "on"
        filter_staxrip_suffix = self.filter_suffix_checkbox.get() == "on"
        
        options = VerifyOptionsObject(folder_path, ignore_ffmpeg, filter_staxrip_suffix)
        self.verifier_function(options)