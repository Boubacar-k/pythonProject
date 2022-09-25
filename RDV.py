from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
import mysql.connector





def Valider():

    Nomcomplet =labelTitre.get();
    DatedeNaissance = labelTitre.get();
    Téléphone = labelTitre.get();
    Adresse= labelTitre.get();
    Date= labelTitre.get();
    Heure=labelTitre.get();
    Traitant=labelTitre.get();

    con= mysql.connect('hopital')
    curser.execute("Inserer dans RDV('Nom complet','Date de naissance','Telephone','Adresse','Date','Heure','Traitant') values(?,?,?,?,?,?,?)")
    con.commit()
    con.close()
    messagebox.showinfo("RDV inseré")


    con = mysql.connect('hopital.db')
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

        con = mysql.connect('hopital.db')
        curser.execute(
            "Modifier RDV set Nom complet=?, Date de naissance=?,Téléphone=?, Adresse=?,Date=?,Heure=?,Traitant=? where Nom complet=?",
            [Nomcomplet, Datedenaissance, Téléphone, Adresse, Date, Heure, Traitant])
        con.commit()
        con.close()
        messagebox.showinfo("RDV modifié")

        con = mysql.connect('hopital.db')
        curser = con.cursor()
        select = curser.execute("select *from RDV order by Nom complet desc")
        select = list(select)
        table.insert('', END, values=select[0])
        con.close()

def Supprimer():
            codeSelectionner= table.item(table.selection())['values'][0]
            con = mysql.connect('hopital.db')
            curser = con.cursor()
            delete = curser.execute("delete from RDV where Nom complet={}".format(codeSelectionner))
            con.commit()
            table.delete(table.selection())

table= ttk.Treeview(colums= (1,2,3,4,5,6,7), height=5, show="headings")
table.place(x=400,y=60,width=880,height=30)


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



con= mysql.connect('hopital.db')
curser = con.cursor()
select = curser.execute("select * from RDV")
for row in select:
    table.insert('',END, value= row)
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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Insertion des RENDEZ-VOUS",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)




labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Liste des RENDEZ-VOUS",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=350,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#FRAME
dash = Frame(fenetre,background="#4062DD")
dash.place(x=0,y=90,width=200,height=480)

#BOUTONS
btnAccueil=Button(dash,text="Accueil",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Accueil)
btnAccueil.place(x=10,y=60,width=180)
btnPersonnel=Button(dash,text="Personnel",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Personnel)
btnPersonnel.place(x=10,y=110,width=180)
btnDepartement=Button(dash,text="Departement",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Depatement)
btnDepartement.place(x=10,y=160,width=180)
btnPatient=Button(dash,text="Patient",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Patient)
btnPatient.place(x=10,y=210,width=180)
btnOrdonnance=Button(dash,text="Ordonnance",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Ordonnance)
btnOrdonnance.place(x=10,y=260,width=180)
btnComptabilite=Button(dash,text="Comptabilité",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Comptabilite)
btnComptabilite.place(x=10,y=310,width=180)
btnRdv=Button(dash,text="Rendez-vous",font=("Arial",12),bg="#1D314F",fg="white",borderwidth=0,command=Rdv)
btnRdv.place(x=10,y=360,width=180)

btnDeconnecter=Button(dash,text="Se deconnecter",font=("Arial",12),bg="#3D88F9",fg="white",borderwidth=0,command=deconnection)
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
























fenetre.mainloop()