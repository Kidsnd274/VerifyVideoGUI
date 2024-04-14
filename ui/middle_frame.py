import customtkinter as ctk
from tkinter import filedialog

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