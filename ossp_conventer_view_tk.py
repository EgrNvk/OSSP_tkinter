
import tkinter as tk

class VolumeView:
    def __init__(self, root, controller, units):
        self.root = root
        self.controller = controller
        self.units = units

        self.root.title("Конвертер об'єму")
        self.root.geometry("500x400")
        self.root.configure(bg="light gray")

        tk.Label(self.root, text="Конвертер об'єму", font=("Arial", 20, "bold"), bg="light gray").pack(pady=10)

        tk.Label(self.root, text="Введіть число:", font=("Arial", 16, "bold"), bg="light gray").pack()
        self.value_entry=tk.Entry(self.root, width=15, justify="center")
        self.value_entry.pack(pady=3)

        tk.Label(self.root, text="Звідки:", font=("Arial", 16, "bold"), bg="light gray").pack()
        self.from_var=tk.StringVar(self.root)
        self.from_var.set(units[0])
        tk.OptionMenu(self.root, self.from_var, *units).pack(pady=3)

        tk.Label(self.root, text="Куди:", font=("Arial", 16, "bold"), bg="light gray").pack()
        self.to_var = tk.StringVar(self.root)
        self.to_var.set(units[1])
        tk.OptionMenu(self.root, self.to_var, *units).pack(pady=3)

        tk.Button(self.root, text="Конвертувати", bg="blue", fg="white", font=("Arial", 10, "bold"), command=self.on_convert).pack(pady=10)

        self.result_label=tk.Label(self.root, text="", font=("Arial", 12, "bold"), bg="light gray")
        self.result_label.pack(pady=5)

    def on_convert(self):
        value_str=self.value_entry.get()
        from_unit=self.from_var.get()
        to_unit=self.to_var.get()

        self.controller.convert(value_str, from_unit, to_unit)

    def update_result(self, text: str, color: str):
        self.result_label.config(text=text, fg=color)