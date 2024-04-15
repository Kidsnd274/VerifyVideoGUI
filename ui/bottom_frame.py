import customtkinter as ctk

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
        
    def disable_frame(self):
        for widget in self.winfo_children():
            widget.configure(state="disabled")
            
    def enable_frame(self):
        for widget in self.winfo_children():
            widget.configure(state="normal")

class BottomFrame(ctk.CTkFrame):
    def __init__(self, master, options_dict, verify_button_event):
        super().__init__(master)
        self.button_original_color = ""
        
        self.grid_columnconfigure(1, weight=1)
        
        self.options_frame = OptionsCheckboxFrame(self, options_dict)
        self.options_frame.grid(row=0, column=0, sticky="nsew")
        
        self.verify_button = ctk.CTkButton(self, text="Verify Video", command=verify_button_event)
        self.verify_button.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.button_original_color = self.verify_button.cget("fg_color")
        
    def disable_frame(self):
        self.verify_button.configure(fg_color='red')
        self.verify_button.configure(text="Verifying...")
        self.verify_button.configure(state="disabled")
        self.options_frame.disable_frame()
        
    def enable_frame(self):
        self.verify_button.configure(fg_color=self.button_original_color)
        self.verify_button.configure(text="Verify Video")
        self.verify_button.configure(state="normal")
        self.options_frame.enable_frame()
    