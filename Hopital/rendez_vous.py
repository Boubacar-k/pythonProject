from subprocess import call
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import customtkinter


def Valider():

    Nomcomplet =labelTitre.get();
    DatedeNaissance = labelTitre.get();
    Téléphone = labelTitre.get();
    Adresse= labelTitre.get();
    Date= labelTitre.get();
    Heure=labelTitre.get();
    Traitant=labelTitre.get();

    con= mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser.execute("Inserer dans RDV('Nom complet','Date de naissance','Telephone','Adresse','Date','Heure','Traitant') values(?,?,?,?,?,?,?)")
    con.commit()
    con.close()
    messagebox.showinfo("RDV inseré")


    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser= con.cursor()
    select= curser.execute("select *from RDV order by Nom complet desc")
    select= list(select)
    table.insert('',END,values=select[0])
    con.close()

def Modifier():
        Nomcomplet = labelTitre.get();
        DatedeNaissance = labelTitre.get();
        Téléphone = labelTitre.get();
        Adresse = labelTitre.get();
        Date = labelTitre.get();
        Heure = labelTitre.get();
        Traitant = labelTitre.get();

        con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
        curser.execute(
            "Modifier RDV set Nom complet=?, Date de naissance=?,Téléphone=?, Adresse=?,Date=?,Heure=?,Traitant=? where Nom complet=?",
            [Nomcomplet, Datedenaissance, Téléphone, Adresse, Date, Heure, Traitant])
        con.commit()
        con.close()
        messagebox.showinfo("RDV modifié")

        con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
        curser = con.cursor()
        select = curser.execute("select *from RDV order by Nom complet desc")
        select = list(select)
        table.insert('', END, values=select[0])
        con.close()

def Supprimer():
            codeSelectionner= table.item(table.selection())['values'][0]
            con = mysql.connector.connect('hopital.db')
            curser = con.cursor()
            delete = curser.execute("delete from RDV where Nom complet={}".format(codeSelectionner))
            con.commit()
            table.delete(table.selection())


def Rechercher():
    Nomcomplet = labelTitre.get();
    DatedeNaissance = labelTitre.get();
    Téléphone = labelTitre.get();
    Adresse = labelTitre.get();
    Date = labelTitre.get();
    Heure = labelTitre.get();
    Traitant = labelTitre.get();

    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    select = curser.execute("select *from RDV order by Nom complet desc")
    select = list(select)
    table.insert('', END, values=select[0])
    con.commit()
    con.close()


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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE RENDEZ-VOUS",font=("Sans Serif bold",20),
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


labelTitre = Label(text = "Nom complet")
labelTitre.place(x=200,y=90)


labelTitre = Entry()
labelTitre.place(x=303,y=93)

labelTitre= Label(text = "Date de Naissance")
labelTitre.place(x=200,y=120)

labelTitre = Entry()
labelTitre.place(x=304,y=120)

labelTitre= Label(text = "Téléphone")
labelTitre.place(x=200,y=150)

labelTitre = Entry()
labelTitre.place(x=304,y=150)



labelTitre= Label(text = "Adresse")
labelTitre.place(x=700,y=90)

labelTitre = Entry()
labelTitre.place(x=755,y=93)

labelTitre= Label(text = "Date")
labelTitre.place(x=700,y=120)

labelTitre = Entry()
labelTitre.place(x=755,y=120)

labelTitre= Label(text = "Heure")
labelTitre.place(x=700,y=155)

labelTitre = Entry()
labelTitre.place(x=755,y=155)

labelTitre= Label(text = "Traitant")
labelTitre.place(x=700,y=190)

labelTitre = Entry()
labelTitre.place(x=755,y=190)

btnRdv=Button(text="Valider",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Rdv)
btnRdv.place(x=230,y=300,width=180)

btnRdv=Button(text="Modifier",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Rdv)
btnRdv.place(x=420,y=300,width=180)

btnRdv=Button(text="Supprimer",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Rdv)
btnRdv.place(x=610,y=300,width=180)

btnRdv=Button(text="Rechercher",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Rdv)
btnRdv.place(x=800,y=300,width=180)

#Titre tableau
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="LISTE DES RENDEZ-VOUS",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=340,width=880,height=30)

table = ttk.Treeview(fenetre,columns=(1,2,3,4,5,6,7),height=7,show="headings",)
table.place(x=200,y=370,width=880,height=200)

style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")


table.heading(1, text="Nom complet")
table.heading(2, text="Date de naissance")
table.heading(3, text="Téléphone")
table.heading(4, text="Adresse")
table.heading(5, text="Date")
table.heading(6, text="Heure")
table.heading(7, text="Traitant")


table.column(1, width = 50)
table.column(2, width = 150)
table.column(3, width = 150)
table.column(4, width = 50)
table.column(5, width = 150)
table.column(6, width = 100)
table.column(7, width = 150)



con= mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
curser = con.cursor()
select = curser.execute("select * from rdv")
for row in select or []:
    table.insert('',END, value= row)
con.close()




fenetre.mainloop()