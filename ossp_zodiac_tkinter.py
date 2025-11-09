import tkinter as tk



root = tk.Tk()
root.title("Title")
root.geometry("400x400")
root.configure(bg="#f2f2f2")

label1 = tk.Label(root, text = "Введите день рождения:", font=("Arial",14), bg="#f2f2f2")
label1.pack(pady=(20,5))
entry1 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry1.pack(pady=10)
label2 = tk.Label(root, text = "Введите месяц рождения:", font=("Arial",14), bg="#f2f2f2")
label2.pack(pady=(20,5))
entry2 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry2.pack(pady=10)
label3 = tk.Label(root, text = "Введите год рождения:", font=("Arial",14), bg="#f2f2f2")
label3.pack(pady=(20,5))
entry3 = tk.Entry(root, font=("Arial", 10), width=25, justify="center")
entry3.pack(pady=10)
def btnClick1():
    if (int(entry2.get()) == 1 and int(entry1.get()) >= 20) or (int(entry2.get()) == 2 and int(entry1.get()) <= 18):
        zodiac = "Водолей"
    elif (int(entry2.get()) == 2 and int(entry1.get()) >= 19) or (int(entry2.get()) == 3 and int(entry1.get()) <= 20):
        zodiac = "Рыбы"
    elif (int(entry2.get()) == 3 and int(entry1.get()) >= 21) or (int(entry2.get()) == 4 and int(entry1.get()) <= 19):
        zodiac = "Овен"
    elif (int(entry2.get()) == 4 and int(entry1.get()) >= 20) or (int(entry2.get()) == 5 and int(entry1.get()) <= 20):
        zodiac = "Телец"
    elif (int(entry2.get()) == 5 and int(entry1.get()) >= 21) or (int(entry2.get()) == 6 and int(entry1.get()) <= 20):
        zodiac = "Близнецы"
    elif (int(entry2.get()) == 6 and int(entry1.get()) >= 21) or (int(entry2.get()) == 7 and int(entry1.get()) <= 22):
        zodiac = "Рак"
    elif (int(entry2.get()) == 7 and int(entry1.get()) >= 23) or (int(entry2.get()) == 8 and int(entry1.get()) <= 22):
        zodiac = "Лев"
    elif (int(entry2.get()) == 8 and int(entry1.get()) >= 23) or (int(entry2.get()) == 9 and int(entry1.get()) <= 22):
        zodiac = "Дева"
    elif (int(entry2.get()) == 9 and int(entry1.get()) >= 23) or (int(entry2.get()) == 10 and int(entry1.get()) <= 22):
        zodiac = "Весы"
    elif (int(entry2.get()) == 10 and int(entry1.get()) >= 23) or (int(entry2.get()) == 11 and int(entry1.get()) <= 21):
        zodiac = "Скорпион"
    elif (int(entry2.get()) == 11 and int(entry1.get()) >= 22) or (int(entry2.get()) == 12 and int(entry1.get()) <= 21):
        zodiac = "Стрелец"
    else:
        zodiac = "Козерог"
    label4.config(text=f"Ваш знак зодиака — {zodiac}")




button = tk.Button(root, text="Знак зодиака", font=("Arial", 14), command=btnClick1)
button.pack(pady=10)

label4 = tk.Label(root, text = "Ваш знак зодиака - ", font=("Arial",14), bg="#f2f2f2")
label4.pack(pady=(20,5))


root.mainloop()