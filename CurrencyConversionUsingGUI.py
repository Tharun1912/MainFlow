import tkinter as tk
from tkinter import ttk
import requests

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    return response.json()['rates']

def convert_currency():
    amount = float(usd_entry.get())
    target_currency = currency_var.get()
    rate = exchange_rates.get(target_currency)
    result = amount * rate
    result_label.config(text=f"Converted Amount: {result:.2f} {target_currency}")

app = tk.Tk()
app.title("USD Currency Converter")

exchange_rates = get_exchange_rate()

tk.Label(app, text="Amount in USD:").grid(row=0, column=0)
usd_entry = tk.Entry(app)
usd_entry.grid(row=0, column=1)

tk.Label(app, text="Select Currency:").grid(row=1, column=0)
currency_var = tk.StringVar()
currency_dropdown = ttk.Combobox(app, textvariable=currency_var, values=list(exchange_rates.keys()))
currency_dropdown.grid(row=1, column=1)

convert_button = tk.Button(app, text="Convert", command=convert_currency)
convert_button.grid(row=2, column=1)

result_label = tk.Label(app, text="Converted Amount: ")
result_label.grid(row=3, column=1)

app.mainloop()
