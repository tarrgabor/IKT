from tkinter import *
ablak1=Tk()

def klikk():
    print("Klikkeltem")

gyoker = 'H:\\ikt project munka\\python\\képek\\'
ablak1.geometry('450x450')
ablak1.title('IKT Tkinter')
icon = PhotoImage(file=gyoker+'icon.png')
ablak1.iconphoto(True, icon)

elsokep = PhotoImage(file=gyoker+"mukodj.png")

cimke=Label(ablak1,
                    text='Hello there!',
                    fg='#00A1FF',
                    bg='lightgrey',
                    font=('Arial', 45, 'bold'),
                    bd=10,
                    relief=RIDGE,
                    padx=10,
                    pady=10,
                    image=elsokep,
                    compound='bottom').pack()
ablak1.config(background='black')

gombkep = PhotoImage(file=gyoker+"giphy.gif")

gomb=Button(ablak1,
                    text='Kattints!',
                    fg="blue",
                    font=("Comic Sans", 35, 'bold'),
                    bg='black',
                    relief=SUNKEN,
                    bd=10,
                    command=klikk,
                    padx=12,
                    pady=12,
                    image=gombkep,
                    compound="bottom",
                    activebackground='blue',
                    activeforeground='yellow',
                    state=ACTIVE).pack()


ablak1.mainloop()