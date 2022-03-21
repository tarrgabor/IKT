from tkinter import *
def osszeg():
    a = int(mezo1.get())
    b = int(mezo2.get())
    c = a + b
    mezo3.delete(0, END)
    mezo3.insert(0, "Összeg: "+str(c))

def kivonas():
        a = int(mezo1.get())
        b = int(mezo2.get())
        c = a - b
        mezo3.delete(0, END)
        mezo3.insert(0, "Különbség: "+str(c))
def szorzas():
        a = int(mezo1.get())
        b = int(mezo2.get())
        c = a * b
        mezo3.delete(0, END)
        mezo3.insert(0, "A szorzat: "+str(c))
def osztas():
        a = int(mezo1.get())
        b = int(mezo2.get())
        if b==0:
            mezo3.delete(0, END)
            mezo3.insert(0, "Nem lehet nullával osztani")
        else: 
            c = a / b
            mezo3.delete(0, END)
            mezo3.insert(0, "A végeredmény: "+str(c))

def negyzetre():
        a = int(mezo1.get())
        c = a * a
        mezo3.delete(0, END)
        mezo3.insert(0, "a négyzete: "+str(c))
def gyokvonas():
        import math
        a = int(mezo1.get())
        if a<=0:
            mezo3.delete(0, END)
            mezo3.insert(0, "Nem lehetséges")
        else:
            c = math.sqrt(a) 
            mezo3.delete(0, END)
            mezo3.insert(0, "A gyöke: "+str(c))

foablak=Tk()
foablak.config()
cimke=Label(foablak, text="Üdvözöllek!", fg="green")
cimke.grid(row=0, column=1)

gomb3=Button(foablak, text="Kilépés", command=foablak.destroy , fg="green" , bg="white", pady=10, padx=5)
gomb3.grid(row=13, column=2)

cimke=Label(foablak, text="Első szám", fg="green")
cimke.grid(row= 1, column=0)

mezo1=Entry(foablak)
mezo1.grid(row=1, column=1)

cimke=Label(foablak, text="Második szám", fg="green")
cimke.grid(row=2, column=0)

mezo2=Entry(foablak)
mezo2.grid(row=2, column=1)

gomb4=Button(foablak, text="Összead", command=osszeg , fg="green" , bg="white", pady=3, padx=5)
gomb4.grid(row=4, column=1)

gomb5=Button(foablak, text="Kivon", command=kivonas , fg="green" , bg="white", pady=3, padx=5)
gomb5.grid(row=5, column=1)

gomb6=Button(foablak, text="Szoroz", command=szorzas , fg="green" , bg="white", pady=3, padx=5)
gomb6.grid(row=6, column=1)

gomb7=Button(foablak, text="Eloszt", command=osztas , fg="green" , bg="white" , pady=3, padx=5)
gomb7.grid(row=7, column=1)

gomb8=Button(foablak, text="Négyzetre emel", command=negyzetre , fg="green" , bg="white", pady=3, padx=5)
gomb8.grid(row=8, column=1)

gomb8=Button(foablak, text="Gyökvonás", command=gyokvonas , fg="green" , bg="white", pady=3, padx=5)
gomb8.grid(row=9, column=1)

cimke=Label(foablak, text="Végeredmény", fg="green",)
cimke.grid(row=10, column=0,)

mezo3=Entry(foablak)
mezo3.grid(row=10, column=1)

gyoker = 'H:\\ikt project munka\\python\\képek\\'

can1=Canvas(foablak, width=300, height=300, bg ='white')
photo = PhotoImage(file=gyoker+"a.gif")
item=can1.create_image(100, 200, image=photo)
can1.grid(row=11, column=1)



foablak.mainloop()