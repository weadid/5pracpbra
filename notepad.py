import tkinter as tk
from tkinter import scrolledtext

# Создание основного окна
root = tk.Tk()
root.title("Блокнот")

# Создание области для текста
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD)
text_area.pack(expand=True, fill='both')

# Запуск главного цикла
root.mainloop()
