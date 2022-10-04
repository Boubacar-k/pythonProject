from tkinter import *
from tkinter import ttk
from subprocess import call
from tkcalendar import *
from subprocess import call
from tkinter import messagebox
import mysql.connector as Mysql
from tkinter.ttk import Treeview
import customtkinter
from PIL import ImageTk,Image
import pickle

def rechercher():
    if(txtE_mail.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer l'e-mail du patient à chercher")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM rdv WHERE E_mail ='"+ txtE_mail.get() +"'")
        rows = cursor.fetchall()

        for row in rows:

            txtNom.insert(0, row[3])
            txtDate_naissance.insert(0, row[4])
            txtTelephone.insert(0, row[5])
            txtAdresse.insert(0, row[6])
            txtDate_rdv.insert(0, row[7])
            txtheure_rdv.insert(0, row[8])
            Traitant.insert(0, row[9])

        con.close();
def modifier():
    E_mail = txtE_mail.get()
    nom = txtNom.get()
    date_naissance = txtDate_naissance.get()
    telephone = txtTelephone.get()
    adresse = txtAdresse.get()
    date_rdv = txtDate_rdv.get()
    heure_rdv = txtheure_rdv.get()
    traitant = Traitant.get()

    if (E_mail=="" or nom == "" or date_naissance == "" or adresse == "" or telephone == "" or date_rdv== "" or heure_rdv== "" or traitant=="" ):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit être vide")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("update rdv set E_mail='"+ E_mail+"', nom ='"+ nom+"',date_naissance='"+ date_naissance +"',telephone='"+ telephone+"',adresse='"+ adresse +"',date_rdv='"+ date_rdv +"',heure_rdv='"+ heure_rdv +"',traitant='"+ traitant+"' WHERE E_mail='"+ E_mail+"'")
        cursor.execute("commit");
        messagebox.showinfo("Modification ", "Modifier avec succès")

        txtE_mail.delete(0, 'end')
        txtNom.delete(0, 'end')
        txtDate_naissance.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtDate_rdv.delete(0, 'end')
        txtheure_rdv.delete(0, 'end')
        afficher()
        con.close();
def ajouter():
    with open("id.pickle", "rb") as infile:
        id1 = pickle.load(infile)
    id = str(id1)
    E_mail = txtE_mail.get()
    nom = txtNom.get()
    date_naissance = txtDate_naissance.get()
    telephone = txtTelephone.get()
    adresse = txtAdresse.get()
    date_rdv = txtDate_rdv.get()
    heure_rdv = txtheure_rdv.get()
    traitant = Traitant.get()

    if (E_mail == "" or nom == "" or date_naissance == "" or adresse == "" or telephone == "" or date_rdv == "" or heure_rdv == "" or traitant == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit être vide")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("INSERT INTO rdv (num_secretaire,E_mail,nom,date_naissance,telephone,adresse,date_rdv,heure_rdv,traitant) VALUES ("+id+", '" + E_mail + "','" + nom + "','" + date_naissance + "','" + telephone + "','" + adresse + "','" + date_rdv + "','" + heure_rdv + "','" + traitant + "')")
        cursor.execute("commit")

        txtE_mail.delete(0, 'end')
        txtNom .delete(0, 'end')
        txtDate_naissance.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtDate_rdv.delete(0, 'end')
        txtheure_rdv.delete(0, 'end')
        Traitant.delete(0, 'end')
        messagebox.showinfo("rdv ajouter ", "Inserer avec succès")
#afficher
        afficher();
        con.close();
def supprimer():
    if(txtE_mail.get() == ""):
        messagebox.showinfo("Suppression ", "Spécifier l'E_mail du patient à supprimer")
    else:
        con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("DELETE FROM rdv WHERE E_mail ='"+ txtE_mail.get() +"'")
        cursor.execute("commit")

        txtE_mail.delete(0, 'end')
        txtNom.delete(0, 'end')
        txtDate_naissance.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtDate_rdv.delete(0, 'end')
        txtheure_rdv.delete(0, 'end')
        Traitant.delete(0, 'end')
        messagebox.showinfo("Suppression ", "Supprimer avec succès")
        afficher()
        con.close();
def afficher():
    con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT id_rdv,E_mail,nom,date_naissance,telephone,adresse,date_rdv,heure_rdv,traitant FROM rdv")
    table.delete(*table.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (id_rdv,E_mail,nom,Date_naissance,telephone,adresse,Date_rdv,Heure_rdv,Traitant) in enumerate(records, start=1):
        table.insert("", "end", values=(id_rdv,E_mail,nom,Date_naissance,telephone,adresse,Date_rdv,Heure_rdv,Traitant))

        con.close()

def les_docteurs():
    con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT nom FROM personnels WHERE fonction = 'DOCTEUR'")
    doc = cursor.fetchall()
    docteur = list(doc)
    con.close()
    return docteur
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

def hide_me(widget):
    widget.place_forget()

fenetre = Tk()


#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Rendez-vous")
fenetre.resizable(False,False)
fenetre.iconbitmap("logo1.ico")
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


#Email

lblE_mail=Label(fenetre,text="E-mail du patient :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblE_mail.place(x=216,y=100,width=150)
txtE_mail = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtE_mail.place(x=400,y=100,width=180)
#NOM

lblNom =Label(fenetre,text="Nom du patient :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=140,width=150)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=140,width=180)

#Date_naisance

lblDate_naissance =Label(fenetre,text="Age :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDate_naissance.place(x=216,y=180,width=180)
txtDate_naissance = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDate_naissance.place(x=400,y=180,width=180)

#Telephone

lblTelephone =Label(fenetre,text="Télephone :",font=("Times New Roman",14),
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

lblDate_rdv =Label(fenetre,text="Date RDV :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDate_rdv.place(x=600,y=140,width=180)
txtDate_rdv = DateEntry(fenetre,bd=2,font=("Times New Roman",12),state='readonly',date_pattern="dd-mm-yy")
txtDate_rdv.place(x=800,y=140,width=180)

#Heure_rdv
lblheure_rdv =Label(fenetre,text="Heure RDV :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblheure_rdv.place(x=600,y=175,width=180)
txtheure_rdv = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtheure_rdv.place(x=800,y=175,width=180)

#Traitant

content = les_docteurs()

lblTraitant =Label(fenetre,text="Médecin traitant :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTraitant.place(x=600,y=220,width=180)
Traitant = ttk.Combobox(fenetre,state='readonly',values=content)
Traitant.place(x=800,y=220,width=180)

#BOUTON Ajouter
btnAjouter=customtkinter.CTkButton(master=fenetre,text="Ajouter",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#20843C",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=ajouter)
btnAjouter.place(x=250,y=260,width=180)
#BOUTON MODIFIER
btnModifier=customtkinter.CTkButton(master=fenetre,text="Modifier",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#1B3864",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=modifier)
btnModifier.place(x=450,y=260,width=180)
#BOUTON SUPPRIMER
btnSupprimer=customtkinter.CTkButton(master=fenetre,text="Supprimer",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#F46464",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=supprimer)
btnSupprimer.place(x=650,y=260,width=180)
#BOUTON RECHERCHER
btnRechercher=customtkinter.CTkButton(master=fenetre,text="Rechercher",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#DC8014",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=rechercher)
btnRechercher.place(x=850,y=260,width=180)
#LISTE DES RDV
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="LISTE DES RDV",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=320,width=880,height=30)

#style
style=ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
#Tableau
table = ttk.Treeview(fenetre, columns = (1, 2, 3,4,5,6,7,8,9), height = 2, show = "headings")
table.place(x = 202,y = 353, width = 875, height = 215)
#Entete
table.heading(1 , text = "ID_rdv")
table.heading(2 , text = "E_mail du patient")
table.heading(3 , text = "Nom du patient")
table.heading(4 , text = "Age")
table.heading(5 , text = "Télephone")
table.heading(6 , text = "Adresse")
table.heading(7 , text = "Date RDV")
table.heading(8 , text = "Heure RDV")
table.heading(9 , text = "Médecin traitant")
#definir les dimentions des colonnes
table.column(1,width = 10)
table.column(2,width = 100)
table.column(3,width = 20)
table.column(4,width = 10)
table.column(5,width = 60)
table.column(6,width = 70)
table.column(7,width = 50)
table.column(8,width = 60)
table.column(9,width = 70)
con = Mysql.connect(host="localhost", user="root", password="", database="hopital")
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
btnAccueil=customtkinter.CTkButton(master=dash,text="Accueil",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Accueil)
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
btnRdv=customtkinter.CTkButton(master=dash,text="Rendez-vous",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#0052CC",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Rdv)
btnRdv.place(x=10,y=360,width=180)

btnDeconnecter=customtkinter.CTkButton(master=dash,text="Deconnecter",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#3D88F9",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)


with open("doc.pickle","rb") as infile:
    fonction = pickle.load(infile)
if(fonction == 'DOCTEUR'):
    hide_me(btnPersonnel)
    hide_me(btnDepartement)
    hide_me(btnComptabilite)
    hide_me(btnAjouter)
    hide_me(btnModifier)
    btnRechercher.place(x=800)
    btnPatient.place(x=10,y=110)
    btnOrdonnance.place(x=10,y=160)
    btnRdv.place(x=10,y=210)
    hide_me(btnSupprimer)
elif(fonction == 'SECRETAIRE'):
    hide_me(btnPersonnel)
    hide_me(btnDepartement)
    hide_me(btnOrdonnance)
    btnPatient.place(x=10, y=110)
    btnComptabilite.place(x=10, y=160)
    btnRdv.place(x=10, y=210)
    hide_me(btnSupprimer)
    btnModifier.place(x=550)
infile.close()
#logo
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)

fenetre.mainloop()