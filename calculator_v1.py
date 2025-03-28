import tkinter as tk

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

def key_press(event):
    key = event.char
    if key in '0123456789.+-*/':
        button_click(key)
    elif key == '\r':  # /r is equal to the button_equal key
        button_equal()
    elif key == '\x1b':  # is for button_clear
        button_clear()

app = tk.Tk()
app.title("Calculator")
app.configure(bg="#55a4e0")
app.bind("<Key>", key_press)

entry = tk.Entry(app, width=18, borderwidth=5, font=('Arial', 17), bg="#faf8f7", fg="black", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_bg = "#e85123"
button_fg = "#f8f8f2"
button_active_bg = "#44475a"
button_active_fg = "#50fa7b"

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    action = button_equal if text == '=' else lambda x=text: button_click(x)
    tk.Button(app, text=text, padx=20, pady=20, command=action, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg).grid(row=row, column=col)

clear_button = tk.Button(app, text='C', padx=20, pady=20, command=button_clear, bg=button_bg, fg=button_fg, activebackground=button_active_bg, activeforeground=button_active_fg)
clear_button.grid(row=5, column=3, columnspan=5)

app.mainloop()
