from tkinter import *
from subprocess import call
from tkinter import messagebox, ttk

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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE ORDONNANCE",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

# Information Patient

labelname = Label(fenetre, text=" Information Patient" ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=260, y=95 )

labelname = Label(fenetre, text=" Nom et Prenom :" ,font=('time new rooman',12))
labelname.place(x=250, y=130 )

# Entrez le nom du Patient
entryname= Entry(fenetre, bg="#D9D9D9")
entryname.place(x=400, y=130, width=180)

# ID Patient
labelname = Label(fenetre, text=" ID_Patient :",font=('time new rooman',12))
labelname.place(x=250, y=160 )

# Entrez l'ID du Patient
entryid= Entry(fenetre, bg="#D9D9D9")
entryid.place(x=400, y=160, width=180)

# ID Ordonance
labelname = Label(fenetre, text=" ID_Ordonance :",font=('time new rooman',12))
labelname.place(x=250, y=190 )

# Entrez l'ID de l'ordonance
entryid_ordo= Entry(fenetre, bg="#D9D9D9")
entryid_ordo.place(x=400, y=190, width=180)
# Titre date de prescription
labelname = Label(fenetre, text="Date de Prescription :" ,font=('time new rooman',10))
labelname.place(x=250, y=220 )

# Entrez la date de payement de la personne
entrydatepayement= DateEntry(fenetre, bg="#D9D9D9", date_pattern="dd/mm/yy")
entrydatepayement.place(x=400, y= 220,width=180)

# Information Medecin

labelname = Label(fenetre, text=" Information Medecin Traitant" ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=630, y=95 )

labelname = Label(fenetre, text=" Nom et Prenom :" ,font=('time new rooman',12))
labelname.place(x=630, y=130 )

# Entrez le nom du Medecin
entryname_medecin= Entry(fenetre, bg="#D9D9D9")
entryname_medecin.place(x=759, y=130, width=180)

# ID Medecin
labelname = Label(fenetre, text=" ID_Medecin :",font=('time new rooman',12))
labelname.place(x=630, y=160 )

# Entrez l'ID du Medecin
entryid_medecin= Entry(fenetre, bg="#D9D9D9")
entryid_medecin.place(x=759, y=160, width=180)

# Prescription liste


#Boutton ajouter
btnajouter= Button(fenetre, text="Enregistrer", background="#0052CC", font=('time new rooman',15))
btnajouter.place(x=390, y=260)

#Boutton Modifier
btnmodifier= Button(fenetre, text="Modifier", background="#0052CC", font=('time new rooman',15))
btnmodifier.place(x=540, y=260)

#Boutton Supprimer
btnsuprimer= Button(fenetre, text="Supprimer", background="#0052CC", font=('time new rooman',15))
btnsuprimer.place(x=670, y=260)

#Boutton Rechercher
btnrechercher= Button(fenetre, text="Rechercher", fg="black", background="#0052CC", font=('time new rooman',15))
btnrechercher.place(x=810, y=260)

'''#Liste des ordonnance
labelliste = Label(fenetre,text="La liste des Ordonnances",font=("Sans Serif bold",15),
                   background="#7DA0D6",foreground="#000000")
labelliste.place(x=200,y=450,width=880,height=23)'''

# Titre Ordonnance
labelname = Label(fenetre, text=" Prescription:" ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=260, y=320 )

text = Text(fenetre,font=("times new roman",13) ,height= 11,bg="#D9D9D9")

text.place(x=230, y=350, width=260)
#Liste des ordonnance
labelname = Label(fenetre, text=" Liste des Ordonnance" ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=630, y=320 )
#FRAME
dash = Frame(fenetre,background="#4062DD")
dash.place(x=0,y=90,width=200,height=480)

#Treeview de la liste des ordonnance
tree= ttk.Treeview(fenetre, columns = (1,2,3,4,5), height = 9, show = "headings")
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
tree.place(x=500, y=349)
tree.heading(1, text= "ID_Patient")
tree.heading(2, text= "ID_ordonnance")
tree.heading(3, text= "ID_Medecin")
tree.heading(4, text= "Date")
tree.heading(5, text= "Prescription")
tree.column(1, width= 90)
tree.column(2, width= 90)
tree.column(3, width= 90)
tree.column(4, width= 90)
tree.column(5, width= 200)
# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=1062,y=410,height=120)

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