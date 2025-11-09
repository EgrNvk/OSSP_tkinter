import tkinter as tk

root = tk.Tk()
root.title("Title")
root.geometry("400x600")
root.configure(bg="#f2f2f2")

label1 = tk.Label(root, text = "Введите первое число:", font=("Arial",14), bg="#f2f2f2")
label1.pack(pady=(20,5))
entry1 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry1.pack(pady=10)

label2 = tk.Label(root, text = "Введите второе число:", font=("Arial",14), bg="#f2f2f2")
label2.pack(pady=(20,5))
entry2 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry2.pack(pady=10)

def btnClick1():
    a = float(entry1.get())
    b = float(entry2.get())
    label3.config(text = f"Результат: {a + b}")

def btnClick2():
    a = float(entry1.get())
    b = float(entry2.get())
    label3.config(text = f"Результат: {a - b}")

def btnClick3():
    a = float(entry1.get())
    b = float(entry2.get())
    if b != 0:
        label3.config(text = f"Результат: {a / b}")
    else:
        label3.config(text = "На ноль делить нельзя!")

def btnClick4():
    a = float(entry1.get())
    b = float(entry2.get())
    label3.config(text = f"Результат: {a * b}")


button1 = tk.Button(root, text="+", font=("Arial", 14), command=btnClick1)
button1.pack(pady=10)
button2 = tk.Button(root, text="-", font=("Arial", 14), command=btnClick2)
button2.pack(pady=10)
button3 = tk.Button(root, text="/", font=("Arial", 14), command=btnClick3)
button3.pack(pady=10)
button4 = tk.Button(root, text="*", font=("Arial", 14), command=btnClick4)
button4.pack(pady=10)

label3 = tk.Label(root, text = "Результат", font=("Arial",14), bg="#f2f2f2")
label3.pack(pady=(20,5))

root.mainloop()