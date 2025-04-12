# TODO: make pyside6 front

import sys, os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.brain import Fuffy

fuffy = Fuffy()

def send():
    user_text = entry.get()
    if not user_text.strip():
        return

    chat.config(state="normal")
    chat.insert(tk.END, f"🧑‍💻 You: {user_text}\n", "user")
    chat.insert(tk.END, "⏳ Fuffy is thinking...\n", "thinking")
    chat.config(state="disabled")
    chat.see(tk.END)
    root.update()

    response = fuffy.think(user_text)

    chat.config(state="normal")
    chat.insert(tk.END, f"🤖 Fuffy: {response}\n\n", "assistant")
    chat.config(state="disabled")
    chat.see(tk.END)
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Fuffy — Chat GUI")
root.geometry("700x500")
root.resizable(True, True)

chat = ScrolledText(root, wrap=tk.WORD, font=("Courier New", 10), state="disabled")
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Courier New", 11))
entry.pack(padx=10, pady=5, fill=tk.X)
entry.bind("<Return>", lambda e: send())

send_button = tk.Button(root, text="Send", command=send)
send_button.pack(pady=5)

chat.tag_config("user", foreground="blue")
chat.tag_config("assistant", foreground="magenta")
chat.tag_config("thinking", foreground="gray")

root.mainloop()