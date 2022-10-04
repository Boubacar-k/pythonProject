#importing library
from tkinter import *
from tkinter import font
from subprocess import call
import time

fenetre=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = fenetre.winfo_screenwidth()
screen_height = fenetre.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
fenetre.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
#w.configure(bg='#ED1B76')
fenetre.overrideredirect(1) #for hiding titlebar

#new window to open
def pageseconnect():
    fenetre.destroy()
    call(["python","connectPage.py"])

Frame(fenetre, width=427, height=250, bg='#272727').place(x=0, y=0)
image_c=PhotoImage(file = "image.png")
l0 = Label(fenetre, image=image_c, width=810, height=700, bg='#4062DD').place(x=-193, y=-227)
'''label1=Label(w, text='IKA DOCTORSO', fg='white', bg='#272727') #decorate it
label1.configure(font=("Arial", 24, "bold"))   #You need to install this font in your PC or try another one
label1.place(x=80,y=90)'''

label2=Label(fenetre, text='Chargement...', fg='black', bg='white') #decorate it
label2.configure(font=("Calibri", 11,'bold'))
label2.place(x=10,y=215)

#making animation

image_a=PhotoImage(file="c2.png")
image_b=PhotoImage(file="c1.png")
#image_c=PhotoImage(file="image.png")




for i in range(5): #5loops
    l1=Label(fenetre, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    fenetre.update_idletasks()
    time.sleep(0.3)

    l1=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(fenetre, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    fenetre.update_idletasks()
    time.sleep(0.3)

    l1=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(fenetre, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    fenetre.update_idletasks()
    time.sleep(0.3)

    l1=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(fenetre, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(fenetre, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    fenetre.update_idletasks()
    time.sleep(0.3)

pageseconnect()
fenetre.mainloop()
