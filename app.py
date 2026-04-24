import tkinter as tk
from tkinter import ttk

from backend import get_message


def show_message():
    result_var.set(get_message(input_var.get()))


root = tk.Tk()
root.title("Hello World")
root.geometry("320x180")
root.resizable(False, False)

main = ttk.Frame(root, padding=20)
main.pack(fill="both", expand=True)

title = ttk.Label(main, text="請輸入數字", font=("Arial", 16))
title.pack(pady=(0, 12))

input_var = tk.StringVar()
entry = ttk.Entry(main, textvariable=input_var, font=("Arial", 14), justify="center")
entry.pack(fill="x", pady=(0, 12))
entry.focus()

button = ttk.Button(main, text="確認", command=show_message)
button.pack(pady=(0, 12))

result_var = tk.StringVar(value="")
result = ttk.Label(main, textvariable=result_var, font=("Arial", 14))
result.pack()

root.bind("<Return>", lambda _event: show_message())
root.mainloop()
