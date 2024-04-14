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

class BottomFrame(ctk.CTkFrame):
    def __init__(self, master, options_dict, verify_button_event):
        super().__init__(master)
        
        self.grid_columnconfigure(1, weight=1)
        
        options_frame = OptionsCheckboxFrame(self, options_dict)
        options_frame.grid(row=0, column=0, sticky="nsew")
        
        verify_button = ctk.CTkButton(self, text="Verify Video", command=verify_button_event)
        verify_button.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")