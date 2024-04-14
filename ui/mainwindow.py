import customtkinter as ctk
import tkinter as tk
from CTkListbox import *
from tkinter import filedialog
from util.verify_options_object import VerifyOptionsObject

class OptionsCheckboxFrame(ctk.CTkFrame):
    def __init__(self, master, options_dict):
        super().__init__(master)
        
        self.title = ctk.CTkLabel(self, text="Options", fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        
        # Skip ffmpeg check checkbox
        self.skip_ffmpeg_check_checkbox = ctk.CTkCheckBox(self, text="Skip ffmpeg Check", onvalue="on", 
                                                          offvalue="off", variable=options_dict['skip_ffmpeg_variable'])
        self.skip_ffmpeg_check_checkbox.grid(row=1, column=0, padx=10, pady=(10,0), sticky='w')
        
        # Filter files suffix
        self.suffix_var = ctk.StringVar(value="_new")
        self.filter_suffix_checkbox = ctk.CTkCheckBox(self, text="Filter out files with '_new' suffix ", onvalue="on", 
                                                      offvalue="off", variable=options_dict['filter_suffix_variable'])
        self.filter_suffix_checkbox.grid(row=2, column=0, padx=10, pady=(10,10), sticky='w')
        # self.filter_suffix_entry = ctk.CTkEntry(self, textvariable=self.suffix_var, placeholder_text="_new", state="disabled")

class BottomFrame(ctk.CTkFrame):
    def __init__(self, master, options_dict, verify_button_event):
        super().__init__(master)
        
        self.grid_columnconfigure(1, weight=1)
        
        options_frame = OptionsCheckboxFrame(self, options_dict)
        options_frame.grid(row=0, column=0, sticky="nsew")
        
        verify_button = ctk.CTkButton(self, text="Verify Video", command=verify_button_event)
        verify_button.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
class MiddleFrame(ctk.CTkFrame):
    def __init__(self, master, path_variable):
        bg_color = master.cget('background')  # Set the same background as the original window
        super().__init__(master, fg_color=bg_color)
        
        self.grid_columnconfigure(1, weight=1)
        self.grid_configure(padx=50, pady=0, sticky="ew")
        
        path_label = ctk.CTkLabel(self, text="Folder Path: ")
        path_label.grid(row=0, column=0)
        
        self.path_variable = path_variable
        self.path_entry = ctk.CTkEntry(self, textvariable=self.path_variable)
        self.path_entry.grid(row=0, column=1, padx=10, sticky="nsew")
                
        browse_button = ctk.CTkButton(self, text="\U0001F4C1", width=40, height=30, command=self.browseFile)
        browse_button.grid(row=0, column=2, sticky="nsew")
        
    def browseFile(self):
        file_path = filedialog.askdirectory()
        if file_path:
            self.path_variable.set(file_path)  # Update the entry with the selected file path

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