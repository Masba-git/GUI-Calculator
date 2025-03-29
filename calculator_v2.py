import tkinter as tk
import math

memory_value = 0  

def button_click(number):
    current = entry.get().replace(' ', '')
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = str(eval(entry.get().replace(' ', '')))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')

def button_sqrt():
    try:
        value = float(entry.get())
        result = str(math.sqrt(value))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')

def button_percentage():
    try:
        value = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(0, str(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')

def button_memory_add():
    global memory_value
    memory_value += float(entry.get())
    entry.delete(0, tk.END)

def button_memory_subtract():
    global memory_value
    memory_value -= float(entry.get())
    entry.delete(0, tk.END)

def button_memory_recall():
    entry.delete(0, tk.END)
    entry.insert(0, str(memory_value))

def key_press(event):
    key = event.keysym
    if key in '0123456789':
        button_click(key)
    elif key in ['plus', 'minus', 'asterisk', 'slash']:
        operators = {'plus': '+', 'minus': '-', 'asterisk': '*', 'slash': '/'}
        button_click(operators[key])
    elif key == 'Return':
        button_equal()
    elif key == 'Escape':
        button_clear()
    elif key == 'percent':
        button_percentage()
    elif key == 'r':
        button_sqrt()

app = tk.Tk()
app.title("Advanced Calculator")
app.configure(bg="#1e1e2e")
app.bind('<Key>', key_press)

entry = tk.Entry(app, width=18, borderwidth=5, font=('Arial', 17), bg="#faf8f7", fg="black", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('√', 5, 0), ('%', 5, 1), ('M+', 5, 2), ('M-', 5, 3),
    ('MR', 6, 0), ('C', 6, 1)
]

for (text, row, col) in buttons:
    action = {
        '=': button_equal,
        '√': button_sqrt,
        '%': button_percentage,
        'M+': button_memory_add,
        'M-': button_memory_subtract,
        'MR': button_memory_recall,
        'C': button_clear
    }.get(text, lambda x=text: button_click(x))
    tk.Button(app, text=text, padx=20, pady=20, command=action, bg="#e85123", fg="#f8f8f2", activebackground="#44475a", activeforeground="#50fa7b").grid(row=row, column=col)

app.mainloop()
"""