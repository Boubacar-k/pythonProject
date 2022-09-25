from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox

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
lblID_Patient.place(x=216,y=140,width=150)
txtID_Patient = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtID_Patient.place(x=400,y=140,width=180)
#NOM

lblNom =Label(fenetre,text="Nom et Prénom :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=180,width=150)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=180,width=180)

#SEXE

content =['Homme','Femme']

lblSexe =Label(fenetre,text="sexe :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSexe.place(x=216,y=220,width=180)
sexe = ttk.Combobox(fenetre,values=content)

sexe.place(x=400,y=220,width=180)

#Age_Patient

lblAge_patient =Label(fenetre,text="Age Patient :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAge_patient.place(x=216,y=260,width=180)
txtAge_patient = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAge_patient.place(x=400,y=260,width=180)
#Adresse

lblAdresse =Label(fenetre,text="Adresse :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAdresse.place(x=600,y=140,width=180)
txtAdresse = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtAdresse.place(x=800,y=140,width=180)
#Télephone

lblTelephone =Label(fenetre,text="Télephone :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblTelephone.place(x=600,y=180,width=180)
txtTelephone = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtTelephone.place(x=800,y=180,width=180)

#FONCTION
liste =['Commercant','professionnel','étudiant','élève','autre']

lblContact =Label(fenetre,text="Fonction :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblContact.place(x=600,y=220,width=180)
fonction = ttk.Combobox(fenetre,values=liste)

fonction.place(x=800,y=220,width=180)

#Date

lblDateArrivee =Label(fenetre,text="Date d'insertion :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDateArrivee.place(x=600,y=260,width=180)
txtDateArrivee = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDateArrivee.place(x=800,y=260,width=180)

"""#BOUTON VALIDER
btnValider=Button(fenetre,text="Valider",font=("Arial",14),bg="#4062DD",fg="white",borderwidth=0,command=valider)
btnValider.place(x=800,y=400,width=180)

#BOUTON ANNULER
btnAnnuler=Button(fenetre,text="Annuler",font=("Arial",14),bg="#4062DD",fg="white",borderwidth=0,command=annuler)
btnAnnuler.place(x=600,y=400,width=180)
"""
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

fenetre.mainloop()