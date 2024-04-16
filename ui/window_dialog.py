import customtkinter as ctk

class WindowDialog(ctk.CTkToplevel):
    def __init__(self, parent, message, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent = parent
        self.title("Warning")
        self.geometry("250x110")
        self.resizable(False, False)
        # self.attributes("-toolwindow", True)
        
        self.label = ctk.CTkLabel(self, text=message)
        self.label.pack(padx=20, pady=20)
        
        self.okay_button = ctk.CTkButton(self, text="Ok", command=self.on_button_event)
        self.okay_button.pack()
        
        # Modal configuration
        self.transient(parent)  # This makes the dialog a transient window of parent, which means it will minimize and close with the parent window. Also gets rid of the minimize button
        self.grab_set()  # Prevents input to the main window
        self.protocol("WM_DELETE_WINDOW", self.on_button_event)  # Handle close button click
        
    def on_button_event(self):
        self.destroy()
        self.parent.focus_set()