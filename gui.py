import tkinter as tk
from tkinter import ttk
from fetch_rates import get_exchange_rates
from convert_currency import convert
from format_output import format_result
from config import API_KEY, SUPPORTED_CURRENCIES
import sys

def fetch_and_convert(amount_entry, from_currency_combobox, to_currency_combobox, result_label):
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    
    exchange_rates = get_exchange_rates(API_KEY)
    if exchange_rates:
        result = convert(amount, from_currency, to_currency, exchange_rates)
        output = format_result(amount, from_currency, to_currency, result)
        result_label.config(text=output)
    else:
        result_label.config(text="Error: Unable to fetch exchange rates")

def run_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Currency Converter")
    root.geometry("400x200")

    # SET ICON
    if sys.platform.startswith('win'):
        root.wm_iconbitmap("icon.ico")
    elif sys.platform == "darwin":
        # Replace "icon.icns" with your macOS icon file
        root.iconbitmap("icon.icns")

    # Create and place labels, entry widgets, and comboboxes
    amount_label = ttk.Label(root, text="Amount:")
    amount_label.grid(column=0, row=0, padx=5, pady=5, sticky="w")

    amount_entry = ttk.Entry(root)
    amount_entry.grid(column=1, row=0, padx=5, pady=5, sticky="we")

    from_currency_label = ttk.Label(root, text="From:")
    from_currency_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")

    from_currency_combobox = ttk.Combobox(root, values=SUPPORTED_CURRENCIES)
    from_currency_combobox.current(0)
    from_currency_combobox.grid(column=1, row=1, padx=5, pady=5, sticky="we")

    to_currency_label = ttk.Label(root, text="To:")
    to_currency_label.grid(column=0, row=2, padx=5, pady=5, sticky="w")

    to_currency_combobox = ttk.Combobox(root, values=SUPPORTED_CURRENCIES)
    to_currency_combobox.current(1)
    to_currency_combobox.grid(column=1, row=2, padx=5, pady=5, sticky="we")

    # Create and place convert button and result label
    convert_button = ttk.Button(root, text="Convert", command=lambda: fetch_and_convert(amount_entry, from_currency_combobox, to_currency_combobox, result_label))
    convert_button.grid(column=0, row=3, padx=5, pady=5, sticky="we")

    result_label = ttk.Label(root, text="")
    result_label.grid(column=1, row=3, padx=5, pady=5, sticky="w")

    # Configure column and row weights
    root.columnconfigure(1, weight=1)
    root.rowconfigure(3, weight=1)

    # Start the main event loop
    root.mainloop()
