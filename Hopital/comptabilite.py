from tkinter import *
from tkcalendar import *
from subprocess import call
import customtkinter
from tkinter import messagebox, ttk

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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE COMPTABILITE",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

# Titre Nom et Prénom de la persone à payé
labelname = Label(fenetre, text=" Nom et Prenom", background="#7DA0D6",font=('time new rooman',12))
labelname.place(x=250, y=130 )

# Entrez le nom de la personne
entryname= Entry(fenetre, bg="#D9D9D9")
entryname.configure(font=('time new rooman',15))
entryname.place(x=400, y=130, width=180)

# Titre date de payement de la persone
labelname = Label(fenetre, text="Date de payement", background="#7DA0D6",font=('time new rooman',12))
labelname.place(x=250, y=210 )

# Entrez la date de payement de la personne
entrydatepayement= DateEntry(fenetre, bg="#D9D9D9", date_pattern="dd/mm/yy")
entrydatepayement.place(x=400, y= 210,width=180)

# Titre motifs de payement de la persone à payé
labelname = Label(fenetre, text=" Motifs de payement", background="#7DA0D6",font=('time new rooman',12))
labelname.place(x=600, y=130 )

# Entrez le motifs de payement
entrymotif= Entry(fenetre, bg="#D9D9D9")
entrymotif.configure(font=('time new rooman',15))
entrymotif.place(x=760, y=130, width=180)

#Boutton ajouter
btnajouter= Button(fenetre, text="Enregistrer", background="#0052CC", font=('time new rooman',15))
btnajouter.place(x=390, y=260)

#Boutton Modifier
btnrechercher= Button(fenetre, text="Rechercher", background="#0052CC", font=('time new rooman',15))
btnrechercher.place(x=540, y=260)

'''#Boutton Supprimer
btnsuprimer= Button(fenetre, text="Supprimer", background="#0052CC", font=('time new rooman',15))
btnsuprimer.place(x=670, y=260)

#Boutton Rechercher
btnrechercher= Button(fenetre, text="Rechercher", fg="black", background="#0052CC", font=('time new rooman',15))
btnrechercher.place(x=810, y=260)'''

#Liste de payement
labelliste = Label(fenetre,text="La liste de payement",font=("Sans Serif bold",15),
                   background="#7DA0D6",foreground="#000000")
labelliste.place(x=200,y=320,width=880,height=23)

#Tree View
tree= ttk.Treeview(fenetre, columns = (1,2,3), height = 9, show = "headings")
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
tree.place(x=300, y=347)
tree.heading(1, text= "Nom et Prenom")
tree.heading(2, text= "Date de Payement")
tree.heading(3, text= "Motifs")
tree.column(1, width= 200)
tree.column(2, width= 200)
tree.column(3, width= 200)

# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=890,y=357,height=100)

tree.configure(xscrollcommand=verscrlbar.set)
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

fenetre.mainloop()