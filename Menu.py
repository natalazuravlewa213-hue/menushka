from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x300")
root.title("Menu")
root.resizable(False,False)

def quotes():
    top = Toplevel()
    top.geometry("700x200")
    top.title("Цитаты")
    top.resizable(False,False)
    
    lbl0 = Label(top, text="Программист — это человек, который превращает кофе в код.")
    lbl0.pack()

    lbl1 = Label(top, text="Сначала код работает, потом ты не знаешь почему. Потом код не работает, и ты тоже не знаешь почему.")
    lbl1.pack()

    lbl2 = Label(top, text="Хороший программист — не тот, кто не ошибается, а тот, кто умеет находить ошибки.")
    lbl2.pack()
def help():
    messagebox.showinfo(title="Help", message="Эта программа — учебный проект на Python.", detail="Она демонстрирует работу меню и дополнительных окон, а также кнопок.")

def About():
    messagebox.showinfo(title="О программе", message="Версия программы: 0.1", detail="Автор программы: Андрюха")

def exit():
    if messagebox.askyesno(title="Точно?", message="Вы уверены что хотите выйти?"):
                   root.destroy()

def btn():
    messagebox.showinfo(title="-_-", message="Я просто кнопка")

def listik():
    t = Toplevel()
    t.geometry("500x500")
    t.title("Список")
    t.resizable(False,False)
    
    lb = Listbox(t, height=20, width=40)
    lb.pack()

    entry = Entry(t)
    entry.pack()

    def add():

        text = entry.get()
        if text:
            lb.insert(END, text)
            entry.delete(0, END)
        else:
            messagebox.showwarning("Ошибка", "Введите текст!")

    def delete():
        selected = lb.curselection()
        
        if selected:
            lb.delete(selected[0])
        else:
            messagebox.showwarning("Ошибка", "Выберите элемент!")
        
    btn_add = Button(t, text="Добавить", command=add)
    btn_add.pack(pady=5)

    btn_del = Button(t, text="Удалить", command=delete)
    btn_del.pack(pady=5)


        
menu = Menu(root, tearoff = 0)
root.config(menu=menu)

menu.add_cascade(label="Помощь", command=help)

menu.add_cascade(label="Выход", command=exit)

menu.add_cascade(label="О программе", command=About)



frm = Frame(root, height=100, bg="DodgerBlue")
frm.pack(fill=BOTH,expand=True)

lbl_panel = Label(frm, text="Панель управления", font=("Arial", 18, "bold"), bg="DodgerBlue")
lbl_panel.place(x=190, y=100)

btn_list = Button(frm, text="Список", font=("Arial", 15, "bold"), bg="DodgerBlue", cursor="hand1", activebackground="DodgerBlue", command=listik)
btn_list.place(x=10, y=240)

btn_quotes = Button(frm, text="Цитаты", font=("Arial", 15, "bold"), bg="DodgerBlue", cursor="hand1", activebackground="DodgerBlue", command=quotes)
btn_quotes.place(x=250, y=240)

btn_list = Button(frm, text="Нажми меня", font=("Arial", 15, "bold"), bg="DodgerBlue", cursor="hand1", activebackground="DodgerBlue", command=btn)
btn_list.place(x=450, y=240)

root.mainloop()
