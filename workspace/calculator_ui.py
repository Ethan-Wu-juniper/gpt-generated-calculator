import tkinter as tk
from calculator import Calculator

class CalculatorUI:
    def __init__(self, master):
        self.master = master
        self.calculator = Calculator()
        self.create_widgets()
        self.current_operation = None

    def create_widgets(self):
        self.master.title("Calculator")
        self.master.configure(bg="black")

        self.display = tk.Entry(self.master, width=20, font=("Arial", 24), justify="right")
        self.display.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, column) in buttons:
            button = tk.Button(self.master, text=text, width=5, height=2, font=("Arial", 18), bg="yellow", command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5)

    def on_button_click(self, text):
        if text.isdigit() or text == ".":
            self.display.insert(tk.END, text)
        elif text in "+-*/":
            self.calculator.reset()
            try:
                self.calculator.add(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.current_operation = text
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == "=":
            try:
                value = float(self.display.get())
                if self.current_operation == "+":
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, self.calculator.add(value))
                elif self.current_operation == "-":
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, self.calculator.subtract(value))
                elif self.current_operation == "*":
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, self.calculator.multiply(value))
                elif self.current_operation == "/":
                    self.display.delete(0, tk.END)
                    self.display.insert(tk.END, self.calculator.divide(value))
                self.current_operation = None
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        elif text == "C":
            self.display.delete(0, tk.END)
            self.current_operation = None
