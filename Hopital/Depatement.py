from tkinter import *
from subprocess import call
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import customtkinter

def deconnection():
    mbox = messagebox.askquestion("Deconnecter","Voulez-vous vraiment vous deconnecter?")
    if(mbox=='yes'):
        fenetre.destroy()
        call(["python", "connectPage.py"])

def Accueil():
    fenetre.destroy()
    call(["python", "accueil.py"])

def Personnel():
    fenetre.destroy()
    call(["python", "personnel.py"])

def Depatement():
    fenetre.destroy()
    call(["python", "depatement.py"])

def Patient():
    fenetre.destroy()
    call(["python", "patient.py"])

def Ordonnance():
    fenetre.destroy()
    call(["python", "ordonnance.py"])

def Comptabilite():
    fenetre.destroy()
    call(["python", "comptabilite.py"])

def Rdv():
    fenetre.destroy()
    call(["python", "rendez_vous.py"])
fenetre = Tk()

def Urgence():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("select d.num_dep,s.numero,s.nombre_lit,sum(numero),sum(nombre_lit) from departement d,salle s where d.num_dep = 1 and d.num_dep = s.num_dep group by d.num_dep,s.numero,s.nombre_lit")
    fenetre.destroy()
    call(["python", "depatement.py"])

def Odontolologie():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("select d.num_dep,s.numero,s.nombre_lit,sum(numero),sum(nombre_lit) from departement d,salle s where d.num_dep = 2 and d.num_dep = s.num_dep group by d.num_dep,s.numero,s.nombre_lit")
    fenetre.destroy()
    call(["python", "depatement.py"])

def Traumatologie():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("select d.num_dep,s.numero,s.nombre_lit,sum(numero),sum(nombre_lit) from departement d,salle s where d.num_dep =3 and d.num_dep = s.num_dep group by d.num_dep,s.numero,s.nombre_lit")
    fenetre.destroy()
    call(["python", "depatement.py"])

def Chirurgie():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("select d.num_dep,s.numero,s.nombre_lit,sum(numero),sum(nombre_lit) from departement d,salle s where d.num_dep =4 and d.num_dep = s.num_dep group by d.num_dep,s.numero,s.nombre_lit")
    fenetre.destroy()
    call(["python", "depatement.py"])

def Gynecologie():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("select d.num_dep,s.numero,s.nombre_lit,sum(numero),sum(nombre_lit) from departement d,salle s where d.num_dep =5 and d.num_dep = s.num_dep group by d.num_dep,s.numero,s.nombre_lit")
    fenetre.destroy()
    call(["python", "depatement.py"])

def Pediatrie():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("select d.num_dep,s.numero,s.nombre_lit,sum(numero),sum(nombre_lit) from departement d,salle s where d.num_dep =6 and d.num_dep = s.num_dep group by d.num_dep,s.numero,s.nombre_lit")
    fenetre.destroy()
    call(["python", "depatement.py"])

#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Accueil")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="I KA DOCTOROSO",font=("Sans Serif bold",26),
                   background="#4062DD",foreground="#FFFFFF")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=30)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE DEPARTEMENT",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#FRAME
dash = Frame(fenetre,background="#4062DD")
dash.place(x=0,y=90,width=200,height=480)

#BOUTONS
btnAccueil=customtkinter.CTkButton(master=dash,text="Accueil",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#0052CC",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Accueil)
btnAccueil.place(x=10,y=60,width=180)
btnPersonnel=customtkinter.CTkButton(master=dash,text="Personnel",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Personnel)
btnPersonnel.place(x=10,y=110,width=180)
btnDepartement=customtkinter.CTkButton(master=dash,text="Département",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Depatement)
btnDepartement.place(x=10,y=160,width=180)
btnPatient=customtkinter.CTkButton(master=dash,text="Patient",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Patient)
btnPatient.place(x=10,y=210,width=180)
btnOrdonnance=customtkinter.CTkButton(master=dash,text="Ordonnance",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Ordonnance)
btnOrdonnance.place(x=10,y=260,width=180)
btnComptabilite=customtkinter.CTkButton(master=dash,text="Comptabilité",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Comptabilite)
btnComptabilite.place(x=10,y=310,width=180)
btnRdv=customtkinter.CTkButton(master=dash,text="Rendez-vous",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Rdv)
btnRdv.place(x=10,y=360,width=180)

btnDeconnecter=customtkinter.CTkButton(master=dash,text="Deconnecter",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#3D88F9",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)

btnUrgence=Button(fenetre,text="URGENCE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Urgence)
btnUrgence.place(x=300,y=140,width=180,height=50)

btnOdonto=Button(fenetre,text="ODONTOLOGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Odontolologie)
btnOdonto.place(x=550,y=140,width=180,height=50)

btnTrauma=Button(fenetre,text="TRAUMATOLOGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Traumatologie)
btnTrauma.place(x=800,y=140,width=180,height=50)

btnChirurgie=Button(fenetre,text="CHIRURGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Chirurgie)
btnChirurgie.place(x=300,y=240,width=180,height=50)

btnGynecologie=Button(fenetre,text="GYNECOLOGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Gynecologie)
btnGynecologie.place(x=550,y=240,width=180,height=50)

btnPediatrie=Button(fenetre,text="PEDIATRIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Pediatrie)
btnPediatrie.place(x=800,y=240,width=180,height=50)
#Titre tableau
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="LISTE DES SALLES",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=300,width=880,height=30)



#Table
table = ttk.Treeview(fenetre,columns=(1,2,3,4,5),height=5,show="headings",)
table.place(x=200,y=330,width=880,height=240)

style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")

#Entete
table.heading(1,text="ID",)
table.heading(2,text="NUMERO SALLE")
table.heading(3,text="NUMERO LIT")
table.heading(4,text="NOMBRE SALLE")
table.heading(5,text="NOMBRE LIT")
table.column(1,width=50)

verscrlbar = ttk.Scrollbar(fenetre,orient="vertical",command=table.yview)
verscrlbar.place(x=1068,y=357,height=213)

table.configure(xscrollcommand=verscrlbar.set)

con= mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
curser = con.cursor()
curser.execute("select d.num_dep,s.numero,s.nombre_lit,sum(numero),sum(nombre_lit) from departement d,salle s where d.num_dep=1 and d.num_dep = s.num_dep group by d.num_dep,s.numero,s.nombre_lit")
for row in curser:
    table.insert('',END, value= row)
con.close()

fenetre.mainloop()