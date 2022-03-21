from tkinter import *
ablak=Tk()
ablak.config()

gyoker = 'H:\\ikt project munka\\python\\képek\\'
ablak.geometry('400x200')

icon = PhotoImage(file=gyoker+'icon.png')
ablak.iconphoto(True, icon)



can1=Canvas(ablak, width=180, height=180, bg ='white')
photo = PhotoImage(file=gyoker+"lightbulb.png")
item=can1.create_image(80, 80, image=photo)
can1.grid(row=1, column=3 , rowspan=3)


cimke=Label(ablak, text="Első mező:")
cimke.grid(row= 1, column=0 , pady=20)

mezo1=Entry(ablak)
mezo1.grid(row=1, column=1)

cimke=Label(ablak, text="Második:")
cimke.grid(row= 2, column=0 , pady=20)

mezo1=Entry(ablak)
mezo1.grid(row=2, column=1)

cimke=Label(ablak, text="Harmadik:")
cimke.grid(row= 3, column=0 , pady=20)

mezo1=Entry(ablak)
mezo1.grid(row=3, column=1)

ablak.mainloop()