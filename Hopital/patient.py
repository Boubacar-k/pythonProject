from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
import mysql.connector as Mysql
from tkinter.ttk import Treeview
import customtkinter

def rechercher():
    if(txtID_Patient.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer l'ID du patient à chercher")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM patients WHERE id_patient ='"+ txtID_Patient.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            txtNom.insert(0, row[1])
            Sexe.insert(0, row[2])
            txtAge_patient.insert(0, row[3])
            txtAdresse.insert(0, row[4])
            txtTelephone.insert(0, row[5])
            Fonction.insert(0, row[6])
            txtDateArrivee.insert(0, row[7])
        con.close();
def modifier():
    id_patient = txtID_Patient.get()
    nom_patient = txtNom.get()
    sex = Sexe.get()
    age_patient = txtAge_patient.get()
    adress = txtAdresse.get()
    telephone = txtTelephone.get()
    fonction = Fonction.get()
    date_arrivee = txtDateArrivee.get()

    if (id_patient=="" or nom_patient == "" or sex == "" or age_patient == "" or adress == "" or telephone == "" or fonction == "" or date_arrivee == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("update patients set nom_patient='"+ nom_patient+"',sex='"+ sex +"',age_patient='"+ age_patient+"',adress='"+ adress +"',telephone='"+ telephone +"',fonction='"+ fonction +"',date_arrivee='"+ date_arrivee+"' WHERE id_patient='"+ id_patient +"'")
        cursor.execute("commit");

        txtID_Patient.delete(0, 'end')
        txtNom.delete(0, 'end')
        Sexe.delete(0, 'end')
        txtAge_patient.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtDateArrivee.delete(0, 'end')
        Fonction.delete(0, 'end')
        messagebox.showinfo("Modification ", "Modifier avec succès")
        afficher()
        con.close();
def ajouter():
    id_patient = txtID_Patient.get()
    nom_patient = txtNom.get()
    sex = Sexe.get()
    age_patient = txtAge_patient.get()
    adress = txtAdresse.get()
    telephone = txtTelephone.get()
    fonction = Fonction.get()
    date_arrivee = txtDateArrivee.get()

    if (id_patient=="" or nom_patient == "" or sex == "" or age_patient == "" or adress == "" or telephone == "" or fonction == "" or date_arrivee == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute( "INSERT INTO patients VALUES ('" + id_patient + "','" + nom_patient + "','" + sex + "','" + age_patient + "','" + adress + "','" + telephone + "','" + fonction +  "','"  + date_arrivee + "')")
        cursor.execute("commit")

        txtID_Patient.delete(0, 'end')
        txtNom.delete(0, 'end')
        Sexe.delete(0, 'end')
        txtAge_patient.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtDateArrivee.delete(0, 'end')
        Fonction.delete(0, 'end')
        messagebox.showinfo("Patient ajouter ", "Inserer avec succès")
#afficher
        afficher()
        con.close();
def supprimer():
    if(txtID_Patient.get() == ""):
        messagebox.showinfo("Suppression ", "Spécifier l'ID du patient à supprimer")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("DELETE FROM patients WHERE id_patient ='"+ txtID_Patient.get() +"'")
        cursor.execute("commit")

        txtID_Patient.delete(0, 'end')
        txtNom.delete(0, 'end')
        Sexe.delete(0, 'end')
        txtAge_patient.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtDateArrivee.delete(0, 'end')
        Fonction.delete(0, 'end')
        messagebox.showinfo("Suppression ", "Supprimer avec succès")
        afficher()
        con.close();
def afficher():
    con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM patients")
    table.delete(*table.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id_patient,nom_patient,sex,age_patient,adress,telephone,fonction,date_arrivee) in enumerate(records, start=1):
        table.insert("", "end", values=(id_patient,nom_patient,sex,age_patient,adress,telephone,fonction,date_arrivee))
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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE PATIENT",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#ID

lblID_Patient=Label(fenetre,text="ID_Patient :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblID_Patient.place(x=216,y=100,width=150)
txtID_Patient = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtID_Patient.place(x=400,y=100,width=180)
#NOM

lblNom =Label(fenetre,text="Nom et Prénom :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=140,width=150)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=140,width=180)

#SEXE

content =['Homme','Femme']

lblSexe =Label(fenetre,text="Sexe :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSexe.place(x=216,y=180,width=180)
Sexe = ttk.Combobox(fenetre,values=content)

Sexe.place(x=400,y=180,width=180)

#Age_Patient

lblAge_patient =Label(fenetre,text="Age Patient :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAge_patient.place(x=216,y=220,width=180)
txtAge_patient = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAge_patient.place(x=400,y=220,width=180)
#Adresse

lblAdresse =Label(fenetre,text="Adresse :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAdresse.place(x=600,y=100,width=180)
txtAdresse = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAdresse.place(x=800,y=100,width=180)
#Télephone

lblTelephone =Label(fenetre,text="Télephone :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTelephone.place(x=600,y=140,width=180)
txtTelephone = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtTelephone.place(x=800,y=140,width=180)

#FONCTION
liste =['Commercant','professionnel','étudiant','élève','autre']

lblFonction =Label(fenetre,text="Fonction :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblFonction.place(x=600,y=180,width=180)
Fonction = ttk.Combobox(fenetre,values=liste)

Fonction.place(x=800,y=180,width=180)

#Date

lblDateArrivee =Label(fenetre,text="Date de création :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDateArrivee.place(x=600,y=220,width=180)
txtDateArrivee = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDateArrivee.place(x=800,y=220,width=180)

#BOUTON Ajouter
btnAjouter=Button(fenetre,text="Ajouter",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=ajouter)
btnAjouter.place(x=250,y=260,width=180)
#BOUTON MODIFIER
btnModifier=Button(fenetre,text="Modifier",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=modifier)
btnModifier.place(x=450,y=260,width=180)
#BOUTON SUPPRIMER
btnSupprimer=Button(fenetre,text="Supprimer",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=supprimer)
btnSupprimer.place(x=650,y=260,width=180)
#BOUTON RECHERCHER
btnRechercher=Button(fenetre,text="Rechercher",font=("Arial",14),bg="#1D314F",fg="white",borderwidth=0,command=rechercher)
btnRechercher.place(x=850,y=260,width=180)
#LISTE DES PATIENTS
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="LISTE DES PATIENTS",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=320,width=880,height=30)

#Tableau
table = ttk.Treeview(fenetre, columns = (1, 2, 3,4,5,6,7,8), height = 2, show = "headings")
table.place(x = 202,y = 353, width = 875, height = 215)
#Entete
table.heading(1 , text = "ID_patient")
table.heading(2 , text = "Nom et prénom")
table.heading(3 , text = "Sexe")
table.heading(4 , text = "Age patient")
table.heading(5 , text = "Adresse")
table.heading(6 , text = "Télephone")
table.heading(7 , text = "Profession")
table.heading(8 , text = "Date de création")
#definir les dimentions des colonnes
table.column(1,width = 10)
table.column(2,width = 100)
table.column(3,width = 20)
table.column(4,width = 10)
table.column(5,width = 60)
table.column(6,width = 70)
table.column(7,width = 50)
table.column(8,width = 60)
con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
cursor = con.cursor()
cursor.execute("select * from patient ")
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
#BOUTONS
btnAccueil=customtkinter.CTkButton(master=dash,text="Accueil",text_font=("Arial",14),bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Accueil)
btnAccueil.place(x=10,y=60,width=180)
btnPersonnel=customtkinter.CTkButton(master=dash,text="Personnel",text_font=("Arial",14),bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Personnel)
btnPersonnel.place(x=10,y=110,width=180)
btnDepartement=customtkinter.CTkButton(master=dash,text="Département",text_font=("Arial",14),bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Depatement)
btnDepartement.place(x=10,y=160,width=180)
btnPatient=customtkinter.CTkButton(master=dash,text="Patient",text_font=("Arial",14),bg_color="#4062DD",fg_color="#0052CC",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Patient)
btnPatient.place(x=10,y=210,width=180)
btnOrdonnance=customtkinter.CTkButton(master=dash,text="Ordonnance",text_font=("Arial",14),bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Ordonnance)
btnOrdonnance.place(x=10,y=260,width=180)
btnComptabilite=customtkinter.CTkButton(master=dash,text="Comptabilité",text_font=("Arial",14),bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Comptabilite)
btnComptabilite.place(x=10,y=310,width=180)
btnRdv=customtkinter.CTkButton(master=dash,text="Rendez-vous",text_font=("Arial",14),bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Rdv)
btnRdv.place(x=10,y=360,width=180)

btnDeconnecter=customtkinter.CTkButton(master=dash,text="Deconnecter",text_font=("Arial",14),bg_color="#4062DD",fg_color="#3D88F9",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Rdv)
btnDeconnecter.place(x=10,y=440,width=180)

fenetre.mainloop()