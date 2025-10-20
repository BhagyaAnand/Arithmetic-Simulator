import tkinter as tk
from tkinter import ttk, messagebox

from core.converter import to_decimal, from_decimal
from core import operations
from gui import widgets, styles

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Arithmetic Operations Simulator")
        self.geometry("520x420")
        self.configure(bg=styles.BG_COLOR)
        self.resizable(False, False)

        # Title
        tk.Label(self, text="Arithmetic Operations Simulator",
                 font=styles.TITLE_FONT, bg=styles.BG_COLOR).pack(pady=10)

        # Input Frame
        input_frame = tk.Frame(self, bg=styles.FRAME_BG)
        input_frame.pack(pady=10, padx=10, fill="x")

        self.num1_widget = widgets.LabeledEntry(input_frame, "First Number:")
        self.num1_widget.pack(pady=5, fill="x")

        self.num2_widget = widgets.LabeledEntry(input_frame, "Second Number:")
        self.num2_widget.pack(pady=5, fill="x")

        # Operation Selector
        op_frame = tk.Frame(input_frame, bg=styles.FRAME_BG)
        op_frame.pack(pady=5, fill="x")
        tk.Label(op_frame, text="Operation:", font=styles.LABEL_FONT, bg=styles.FRAME_BG).pack(side="left", padx=5)
        self.operation_var = tk.StringVar()
        self.operation_dropdown = ttk.Combobox(op_frame, textvariable=self.operation_var,
                                               values=["+", "-", "*", "/"], width=17, state="readonly")
        self.operation_dropdown.pack(side="left", padx=5)
        self.operation_dropdown.current(0)

        # Calculate Button
        calc_btn = widgets.StyledButton(self, text="Calculate", command=self.calculate)
        calc_btn.pack(pady=10)

        # Result Frame
        result_frame = tk.LabelFrame(self, text="Results", font=styles.LABEL_FONT, bg=styles.RESULT_BG)
        result_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.result_labels = {}
        for system in ["Decimal", "Binary", "Octal", "Hexadecimal"]:
            lbl = tk.Label(result_frame, text=f"{system}: ", font=styles.LABEL_FONT,
                           bg=styles.RESULT_BG, fg=styles.RESULT_FG, anchor="w")
            lbl.pack(anchor="w", padx=10, pady=3)
            self.result_labels[system] = lbl

    def calculate(self):
        num1 = self.num1_widget.get()
        num2 = self.num2_widget.get()
        op = self.operation_var.get()

        if not num1 or not num2:
            messagebox.showerror("Error", "Please enter both numbers.")
            return

        try:
            n1, base1 = to_decimal(num1)
            n2, base2 = to_decimal(num2)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        try:
            if op == "+":
                result = operations.add(n1, n2)
            elif op == "-":
                result = operations.sub(n1, n2)
            elif op == "*":
                result = operations.mul(n1, n2)
            elif op == "/":
                result = operations.div(n1, n2)
            else:
                messagebox.showerror("Error", "Invalid operation.")
                return
        except ZeroDivisionError as e:
            messagebox.showerror("Error", str(e))
            return

        results = from_decimal(result)
        for system, lbl in self.result_labels.items():
            lbl.config(text=f"{system}: {results[system]}")