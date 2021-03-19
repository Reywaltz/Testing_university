import tkinter as tk
from tkinter.constants import END
from tkinter import messagebox
from internal.additions import additions


W_WIDTH = 630
W_HEIGHT = 650


def start_GUI():
    """Метод инициализации графического интерфейса"""
    root = tk.Tk()
    top = Toplevel1(root)
    root.mainloop()


class Toplevel1:
    """Класс графического интерфейса"""

    def __init__(self, top=None):
        top.geometry(f"{W_WIDTH}x{W_HEIGHT}")
        top.minsize(W_WIDTH, W_HEIGHT)
        top.resizable(0, 0)
        top.title("Преобразователь предложений")

        self.Input_field = tk.Text(top)
        self.Input_field.place(x=W_WIDTH//2, y=W_HEIGHT//2, height=10)

        self.Input_field.pack(padx=5, pady=10)

        self.Button1 = tk.Button(top, command=self.transform)
        self.Button1.place(height=31)
        self.Button1.configure(text='Получить слова')

        self.Button1.pack(fill="x", padx=15, pady=5)

        self.Listbox1 = tk.Listbox(top)

        self.Scrollbar = tk.Scrollbar(top, orient="vertical")
        self.Scrollbar.config(command=self.Listbox1.yview)

        self.Listbox1.config(yscrollcommand=self.Scrollbar.set)

        self.Scrollbar.pack(side='right', fill='y', pady=5)
        self.Listbox1.pack(fill="x", padx=5, pady=5)

    def transform(self):
        """Метод обратчика кнопки"""
        self.Listbox1.delete(0, 'end')
        form_input = self.Input_field.get(1.0, "end-1c")

        if len(form_input) > 1000:
            messagebox.showerror("Ошибка вввода",
                                 "Превышение длины входной строки. Повторите ввод") # noqa
            return

        format_input = additions.prepare_input(form_input)
        if (format_input == []) or (format_input == ['']):
            messagebox.showerror("Ошибка вввода",
                                 "Введена пустая строка. Повторите ввод")
            return

        items = additions.sentence_transform(format_input)
        for item in items:
            if item != '':
                self.Listbox1.insert(END, item)
