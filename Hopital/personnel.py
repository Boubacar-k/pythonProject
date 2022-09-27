from tkinter import *
from subprocess import call
from tkinter import messagebox, ttk
import customtkinter
from tkcalendar import DateEntry


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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE PERSONNEL",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#ID

ID_Personel=Label(fenetre,text="ID_Personnel :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
ID_Personel.place(x=216,y=120,width=150)
txtID_Personel = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtID_Personel.place(x=400,y=120,width=180)

#NOM et Prenom du Personnel

lblNom =Label(fenetre,text="Nom et Prénom :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=160,width=180)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=160,width=180)

#SEXE

content =['Homme','Femme','Autre']

lblSexe =Label(fenetre,text="sexe :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSexe.place(x=216,y=190,width=180)
sexe = ttk.Combobox(fenetre,values=content)
sexe.place(x=400,y=190,width=180)

#Age_Personnel

lblAge_personel =Label(fenetre,text="Date de Naissance :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAge_personel.place(x=216,y=220,width=180)
txtAge_patient = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAge_patient.place(x=400,y=220,width=180)
#Adresse

lblAdresse =Label(fenetre,text="Adresse :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAdresse.place(x=600,y=120,width=180)
txtAdresse = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAdresse.place(x=800,y=120,width=180)
#Télephone

lblTelephone =Label(fenetre,text="Contact :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTelephone.place(x=600,y=160,width=180)
txtTelephone = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtTelephone.place(x=800,y=160,width=180)

#FONCTION du Personnelle
liste =['Medecin','Comptable','Directeur','Stagiaire','autre']

lblFonction =Label(fenetre,text="Fonction :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblFonction.place(x=600,y=190,width=180)
fonction = ttk.Combobox(fenetre,values=liste)
fonction.place(x=800,y=190,width=180)

#Departement du Personnelle
list =['Traumatologie','Comptabilité','Direction','Pédiatrie','Urgence']

lbldepart =Label(fenetre,text="Département:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lbldepart.place(x=600,y=220,width=200)
departement = ttk.Combobox(fenetre,values=list)
departement.place(x=800, y=220, width=180)
#Date

lblinscrit =Label(fenetre,text="Date d'inscription :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblinscrit.place(x=216,y=260,width=180)
txtinscrit = DateEntry(fenetre,bd=2,font=("Times New Roman",12), date_pattern="dd/mm/yy")
txtinscrit.place(x=400,y=260,width=180)

#Boutton ajouter
btnajouter= Button(fenetre, text="Enregistrer", background="#0052CC", font=('time new rooman',15))
btnajouter.place(x=390, y=300)

#Boutton Modifier
btnmodifier= Button(fenetre, text="Modifier", background="#0052CC", font=('time new rooman',15))
btnmodifier.place(x=540, y=300)

#Boutton Supprimer
btnsuprimer= Button(fenetre, text="Supprimer", background="#0052CC", font=('time new rooman',15))
btnsuprimer.place(x=670, y=300)

#Boutton Rechercher
btnrechercher= Button(fenetre, text="Rechercher", fg="black", background="#0052CC", font=('time new rooman',15))
btnrechercher.place(x=810, y=300)

#Liste de Presonnel
labelliste = Label(fenetre,text="La liste de Personnel",font=("Sans Serif bold",15),
                   background="#7DA0D6",foreground="#000000")
labelliste.place(x=200,y=350,width=880,height=23)

#Tree View
tree= ttk.Treeview(fenetre, columns = (1,2,3,4,5,6,7,8,9), height = 7, show = "headings")
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
tree.place(x=210, y=380)
tree.heading(1, text= "ID_Personnel")
tree.heading(2, text= "Nom et Prenom")
tree.heading(3, text= "Sexe")
tree.heading(4, text= "Date de naissance")
tree.heading(5, text= "Fonction")
tree.heading(6, text= "Spécialité")
tree.heading(7, text= "Departement")
tree.heading(8, text= "Adresse")
tree.heading(9, text= "Date d'inscription")
tree.column(1, width= 90)
tree.column(2, width= 100)
tree.column(3, width= 90)
tree.column(4, width= 100)
tree.column(5, width= 90)
tree.column(6, width= 90)
tree.column(7, width= 90)
tree.column(8, width= 90)
tree.column(9, width= 100)

# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=1052,y=420,height=100)
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

fenetre.mainloop()