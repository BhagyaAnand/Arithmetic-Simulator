import tkinter as tk
from tkinter import ttk
from gui import styles

class LabeledEntry(tk.Frame):
    """A labeled Entry widget"""
    def __init__(self, parent, label_text, width=20):
        super().__init__(parent, bg=styles.FRAME_BG)
        self.label = tk.Label(self, text=label_text, font=styles.LABEL_FONT, bg=styles.FRAME_BG)
        self.label.pack(side="left", padx=5, pady=5)
        self.entry = tk.Entry(self, font=styles.ENTRY_FONT, width=width)
        self.entry.pack(side="left", padx=5, pady=5)

    def get(self):
        return self.entry.get().strip()

    def set(self, text):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, text)

class StyledButton(tk.Button):
    """Button with consistent styling"""
    def __init__(self, parent, text, command):
        super().__init__(parent, text=text, command=command,
                         font=styles.BUTTON_FONT,
                         bg=styles.BUTTON_BG, fg=styles.BUTTON_FG,
                         relief="raised", bd=3, cursor="hand2")