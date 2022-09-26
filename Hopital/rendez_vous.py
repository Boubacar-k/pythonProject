from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
import mysql.connector as Mysql
from tkinter.ttk import Treeview

def rechercher():
    if(txtID_rdv.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer l'ID du rdv à chercher")
    else:
        con = Mysql.connect(host="localhost", user="root", password="root", database="hopital")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM rdv WHERE id_rdv ='"+ txtID_Patient.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            txtNom.insert(0, row[1])
            txtDate_naissance.insert(0, row[2])
            txtTelephone.insert(0, row[3])
            txtAdresse.insert(0, row[4])
            txtDate_rdv.insert(0, row[5])
            txtHeure_rdv.insert(0, row[6])
            txtHeure_rdv.insert(0, row[7])
        con.close();
def modifier():
    id_rdv = txtID_rdv.get()
    nom = txtNom.get()
    date_naissance = txtDate_naissance.get()
    telephone = txtTelephone.get()
    adresse = txtAdresse.get()
    date_rdv = txtDate_rdv.get()
    traitant = txtTraitant.get()

    if (id_rdv=="" or nom == "" or Date_naissance == "" or adresse == "" or telephone == "" or date_rdv== "" or heure_rdv== "" or traitant=="" ):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = Mysql.connect(host="localhost", user="root", password="root", database="hopital")
        cursor = con.cursor()
        cursor.execute("update rdv set nom ='"+ nom+"',date_naissance='"+ date_naissance +"',telephone='"+ telephone+"',adresse='"+ adresse +"',date_rdv='"+ date_rdv +"',heure_rdv='"+ heure_rdv +"',traitant='"+ traitant+"', WHERE id_rdv='"+ id_rdv+"'")
        cursor.execute("commit");

        txtID_rdv.delete(0, 'end')
        txtNom.delete(0, 'end')
        txtDate_naissanceDate.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtDate_rdv.delete(0, 'end')
        txtHeure_rdv.delete(0, 'end')
        txtTraitant.delete(0, 'end')
        messagebox.showinfo("Modification ", "Modifier avec succès")
        afficher()
        con.close();
def valider():
    id_rdv = txtID_rdv.get()
    nom  = txtNom.get()
    date_naissance = txtDate_naissance.get()
    telephone = txtTelephone.get()
    adresse = txtAdresse.get()
    date_rdv = txtDate_rdv.get()
    heure_rdv = txtHeure_rdv.get()
    traitant = txtTraitant.get()

    if (id_rdv == "" or nom == "" or date_naissance == "" or adresse == "" or telephone == "" or date_rdv == "" or heure_rdv == "" or traitant == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = Mysql.connect(host="localhost", user="root", password="root", database="hopital")
        cursor = con.cursor()
        cursor.execute( "INSERT INTO rdv VALUES ('" + id_rdv + "','" + nom + "','" + Date_naissance + "','" + telephone + "','" + adress + "','" + date_rdv + "','" + heure_rdv +  "','"  + traitant + "')")
        cursor.execute("commit")

        txtID_rdv.delete(0, 'end')
        txtNom .delete(0, 'end')
        txtDate_naissance.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtDate_rdv.delete(0, 'end')
        txtHeure_rdv.delete(0, 'end')
        txtTraitant.delete(0, 'end')
        messagebox.showinfo("rdv ajouter ", "Inserer avec succès")
#afficher
        afficher()
        con.close();
def supprimer():
    if(txtID_rdv.get() == ""):
        messagebox.showinfo("Suppression ", "Spécifier l'ID du rdv à supprimer")
    else:
        con = Mysql.connect(host="localhost", user="root", password="root", database="hopital")
        cursor = con.cursor()
        cursor.execute("DELETE FROM rdv WHERE id_rdv ='"+ txtID_rdv.get() +"'")
        cursor.execute("commit")

        txtID_rdv.delete(0, 'end')
        txtNom.delete(0, 'end')
        txtDate_naissance.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtDate_rdv.delete(0, 'end')
        txtHeure_rdv.delete(0, 'end')
        txtTraitant.delete(0, 'end')
        messagebox.showinfo("Suppression ", "Supprimer avec succès")
        afficher()
        con.close();
def afficher():
    con = Mysql.connect(host="localhost", user="root", password="root", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM rdv")
    table.delete(*table.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id_rdv,nom,Date_naissance,telephone,adress,Date_rdv,Heure_rdv,traitant) in enumerate(records, start=1):
        table.insert("", "end", values=(id_rdv,nom,Date_naissance,telephone,adress,Date_rdv,Heure_rdv,traitant))
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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE RDV",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#ID

lblID_rdv=Label(fenetre,text="ID_rdv :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblID_rdv.place(x=216,y=100,width=150)
txtID_rdv = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtID_rdv.place(x=400,y=100,width=180)
#NOM

lblNom =Label(fenetre,text="Nom Complet :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=140,width=150)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=140,width=180)

#Date_naisance

lblDate_naissance =Label(fenetre,text="Date_naissance :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDate_naissance.place(x=216,y=180,width=180)
txtDate_naissance = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDate_naissance.place(x=400,y=180,width=180)

#Telephone

lblTelephone =Label(fenetre,text="Telephone :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTelephone.place(x=216,y=220,width=180)
txtTelephone = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtTelephone.place(x=400,y=220,width=180)
#Adresse

lblAdresse =Label(fenetre,text="Adresse :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAdresse.place(x=600,y=100,width=180)
txtAdresse = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAdresse.place(x=800,y=100,width=180)
#Date_rdv

lblDate_rdv =Label(fenetre,text="Date_rdv :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDate_rdv.place(x=600,y=140,width=180)
txtDate_rdv = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDate_rdv.place(x=800,y=140,width=180)

#Heure_rdv
lblHeure_rdv =Label(fenetre,text="Heure_rdv :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblHeure_rdv.place(x=600,y=175,width=180)
txtHeure_rdv = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtHeure_rdv.place(x=800,y=175,width=180)

#Traitant

lblTraitant =Label(fenetre,text="Traitant :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTraitant.place(x=600,y=220,width=180)
txtTraitant = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtTraitant.place(x=800,y=220,width=180)

#BOUTON Valider
btnValider=Button(fenetre,text="Valider",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=valider)
btnValider.place(x=250,y=260,width=180)
#BOUTON MODIFIER
btnModifier=Button(fenetre,text="Modifier",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=modifier)
btnModifier.place(x=450,y=260,width=180)
#BOUTON SUPPRIMER
btnSupprimer=Button(fenetre,text="Supprimer",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=supprimer)
btnSupprimer.place(x=650,y=260,width=180)
#BOUTON RECHERCHER
btnRechercher=Button(fenetre,text="Rechercher",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=rechercher)
btnRechercher.place(x=850,y=260,width=180)
#LISTE DES RDV
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="LISTE DES RDV",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=320,width=880,height=30)

#Tableau
table = ttk.Treeview(fenetre, columns = (1, 2, 3,4,5,6,7,8), height = 2, show = "headings")
table.place(x = 202,y = 353, width = 875, height = 215)
#Entete
table.heading(1 , text = "ID_rdv")
table.heading(2 , text = "Nom Complet")
table.heading(3 , text = "Date_naissance")
table.heading(4 , text = "Telephone")
table.heading(5 , text = "Adresse")
table.heading(6 , text = "Date_rdv")
table.heading(7 , text = "Heure_rdv")
table.heading(8 , text = "Traitant")
#definir les dimentions des colonnes
table.column(1,width = 10)
table.column(2,width = 100)
table.column(3,width = 20)
table.column(4,width = 10)
table.column(5,width = 60)
table.column(6,width = 70)
table.column(7,width = 50)
table.column(8,width = 60)
con = Mysql.connect(host="localhost", user="root", password="root", database="hopital")
cursor = con.cursor()
cursor.execute("select * from rdv ")
for row in cursor:
    table.insert('', END, value = row)
con.close()
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
btnRdv=Button(dash,text="Rendez-vous",font=("Arial",12),bg="#0052CC",fg="white",borderwidth=0,command=Rdv)
btnRdv.place(x=10,y=360,width=180)

btnDeconnecter=Button(dash,text="Se deconnecter",font=("Arial",12),bg="#3D88F9",fg="white",borderwidth=0,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)


fenetre.mainloop()