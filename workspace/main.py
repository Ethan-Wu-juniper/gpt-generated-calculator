import tkinter as tk
from calculator_ui import CalculatorUI

def main():
    root = tk.Tk()
    calculator_ui = CalculatorUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
