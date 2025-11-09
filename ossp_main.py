import tkinter as tk

root = tk.Tk()
root.title("Title")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

label = tk.Label(root, text = "Введите возраст:", font=("Arial",14), bg="#f2f2f2")
label.pack(pady=(20,5))

entry = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry.pack(pady=10)

label_res = tk.Label(root, text="", font=("Arial", 20, "bold"), fg="blue", bg="#f2f2f2")
label_res.pack(pady=20)

def btnClick():
    name = int(entry.get())
    if name>=18:
        label_res.configure(text = f"Вы взрослый, {name}")
    else:
        label_res.configure(text=f"Вы ребёнок!")

button = tk.Button(root, text="Проверить", font=("Arial", 14), command=btnClick)
button.pack(pady=10)

root.mainloop()