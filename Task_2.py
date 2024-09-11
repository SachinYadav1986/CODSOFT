import tkinter as tk

def button_click(number):
    current = entry_var.get()
    entry_var.set(current + str(number))

def button_clear():
    entry_var.set("")

def button_equal():
    current = entry_var.get()
    try:
        result = eval(current)
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")

root = tk.Tk()
root.title("Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, width=20, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), command=button_equal).grid(row=row_val, column=col_val, padx=5, pady=5)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16), command=lambda b=button: button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

clear_button = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 16), command=button_clear)
clear_button.grid(row=row_val, column=col_val, padx=5, pady=5)

root.mainloop()
