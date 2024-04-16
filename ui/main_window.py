import customtkinter as ctk
import tkinter as tk
from CTkListbox import *
from util.verify_options_object import VerifyOptionsObject
from ui.middle_frame import MiddleFrame
from ui.bottom_frame import BottomFrame
from ui.window_dialog import WindowDialog

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

        self.middle_frame = MiddleFrame(root, self.folder_path_variable)
        self.middle_frame.grid(row=1)
            
        self.bottom_frame = BottomFrame(root, options_dict, self.on_verify_button_clicked)
        self.bottom_frame.grid(row=2, column=0, padx=50, pady=(0, 10), sticky="ew")
        

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
        
        if not folder_path:
            error_dialog = WindowDialog(self.root, "Your folder path cannot be empty!")
            error_dialog.wait_window()
            return
        
        self.disable_ui()
        
        options = VerifyOptionsObject(folder_path, ignore_ffmpeg, filter_staxrip_suffix)
        self.verifier_function(options, self.processing_stopped)
        
    def disable_ui(self):
        self.middle_frame.disable_frame()
        self.bottom_frame.disable_frame()
        
    def enable_ui(self):
        self.middle_frame.enable_frame()
        self.bottom_frame.enable_frame()
        
    def processing_stopped(self):
        self.enable_ui()
        self.root.lift()