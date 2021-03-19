import tkinter as tk
from tkinter import messagebox


W_WIDTH = 240
W_HEIGHT = 120


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
        top.title("Уравнения")

        self.Label = tk.Label(text='Значение X:')
        self.Label.pack(pady=10)

        self.Input_field = tk.Entry(top, justify='center')
        self.Input_field.pack(pady=5)

        self.Button1 = tk.Button(top, command=self.calculate)
        self.Button1.place(height=31)
        self.Button1.configure(text='Получить результат')

        self.Button1.pack(pady=10)

    def calculate(self):
        """Метод обратчика кнопки"""
        try:
            input_value = int(self.Input_field.get())
            if -5 <= input_value < 0:
                res = input_value**2 + input_value + 1
                messagebox.showinfo("Успех!", message=str(res))
                self.Input_field.delete(0, 'end')
            elif 0 <= input_value < 4:
                res = 7 * input_value
                messagebox.showinfo("Успех!", message=str(res))
                self.Input_field.delete(0, 'end')
            else:
                raise ValueError           
        except ValueError:
            self.Input_field.delete(0, 'end')
            messagebox.showerror("Ошибка", "Ошибка ввода")
            return
