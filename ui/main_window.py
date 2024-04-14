import customtkinter as ctk
import tkinter as tk
from CTkListbox import *
from tkinter import filedialog
from util.verify_options_object import VerifyOptionsObject
from ui.middle_frame import MiddleFrame
from ui.bottom_frame import BottomFrame

class MainWindow():
    def __init__(self, root, verifier_function):
        self.root = root
        self.verifier_function = verifier_function
        
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        
        self.folder_path_variable = ctk.StringVar(value="")
        self.skip_ffmpeg_variable = ctk.StringVar(value="off")
        self.filter_suffix_variable = ctk.StringVar(value="off")
        options_dict = {
            'skip_ffmpeg_variable': self.skip_ffmpeg_variable,
            'filter_suffix_variable': self.filter_suffix_variable           
        }
        
        title_font = ctk.CTkFont(size=24, weight="bold")
        title_label = ctk.CTkLabel(root, text="VerifyVideoGUI", justify="center", font=title_font)
        title_label.grid(row=0, column=0, padx=20, pady=10, sticky="ew", columnspan=100)

        middle_frame = MiddleFrame(root, self.folder_path_variable)
        middle_frame.grid(row=1)
        
        bottom_frame = BottomFrame(root, options_dict, self.on_verify_button_clicked)
        bottom_frame.grid(row=2, column=0, padx=50, pady=(0, 10), sticky="ew")

    def toggle_filter_checkbox(self):
        if self.filter_suffix_checkbox.get() == "on":
            self.filter_suffix_entry.configure(state="normal")
            print("checkbox enabled")
        else:
            self.filter_suffix_entry.configure(state="disabled")
            print("checkbox disabled")

    def on_verify_button_clicked(self):
        folder_path = self.folder_path_variable.get()
        ignore_ffmpeg = self.skip_ffmpeg_variable.get() == "on"
        filter_staxrip_suffix = self.filter_suffix_variable.get() == "on"
        
        options = VerifyOptionsObject(folder_path, ignore_ffmpeg, filter_staxrip_suffix)
        self.verifier_function(options)