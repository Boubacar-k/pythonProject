from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox

def annuler():
    fenetre.destroy()
    call(["python","connectPage.py"])

def valider():
    nom = txtNom.get()
    sex = sexe.get()
    dateN = txtDateN.get()
    contact = txtContact.get()
    fn = fonction.get()
    special = Specialite.get()
    nomUtisateur = txtUtilisateur.get()
    mot_de_passe = txtMdp.get()
    confimer = txtConfirmer.get()
    dateIns = txtDateIns.get()
    if(nom==""or sex=="" or dateN==""or contact==""or fn==""or special=="" or nomUtisateur=="" or mot_de_passe==""
    or confimer==""or dateIns==""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    elif (mot_de_passe != confimer):
        messagebox.showinfo("Information", "Votre mot de passe est different de celui de la confirmation")
    else:
        messagebox.showinfo("Information", "Inscrit avec succès")
        fenetre.destroy()
        call(["python","connectPage.py"])
#----------------------------------------------MAIN----------------------------------------------------------
fenetre = Tk()

#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Creer compte")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="I KA DOCTOROSO",font=("Sans Serif bold",26),
                   background="#4062DD",foreground="#FFFFFF")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=30)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE D'INSCRIPTION",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)
#-----------------------------------LES WIDGETS--------------------------------------------------------------
#NOM

lblNom =Label(fenetre,text="Nom_complet :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=16,y=140,width=150)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=200,y=140,width=180)

#SEXE

content =['Homme','Femme']

lblSexe =Label(fenetre,text="sexe :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSexe.place(x=16,y=180,width=180)
sexe = ttk.Combobox(fenetre,values=content)

sexe.place(x=200,y=180,width=180)

#Date naissance

lblDateN =Label(fenetre,text="Date de naissance :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDateN.place(x=16,y=220,width=180)
txtDateN = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDateN.place(x=200,y=220,width=180)

#Contact

lblContact =Label(fenetre,text="Contact :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblContact.place(x=16,y=260,width=180)
txtContact = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtContact.place(x=200,y=260,width=180)

#FONCTION
liste =['directeur','docteur','secretaire']

lblContact =Label(fenetre,text="Fonction :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblContact.place(x=16,y=300,width=180)
fonction = ttk.Combobox(fenetre,values=liste)

fonction.place(x=200,y=300,width=180)

#SPECIALITE

specialite =['Pediatre','Generaliste','Chirurgien','Pneumologue']

lblSpecialite =Label(fenetre,text="Specialite :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSpecialite.place(x=600,y=140,width=180)
Specialite = ttk.Combobox(fenetre,values=specialite)

Specialite.place(x=800,y=140,width=180)

#NOM UTILISATEUR

lblUtilisateur =Label(fenetre,text="Nom_Utilisateur :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblUtilisateur.place(x=600,y=180,width=180)
txtUtilisateur = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtUtilisateur.place(x=800,y=180,width=180)

#MOT DE PASSE

lblMdp =Label(fenetre,text="Mot de passe :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblMdp.place(x=600,y=220,width=180)
txtMdp = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtMdp.place(x=800,y=220,width=180)

#MOT DE PASSE CONFIRMATION

lblConfirmer =Label(fenetre,text="Confirmer :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblConfirmer.place(x=600,y=260,width=180)
txtConfirmer = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtConfirmer.place(x=800,y=260,width=180)

#Date Insertion

lblDateIns =Label(fenetre,text="Date d'insertion :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDateIns.place(x=600,y=300,width=180)
txtDateIns = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtDateIns.place(x=800,y=300,width=180)

#BOUTON VALIDER
btnValider=Button(fenetre,text="Valider",font=("Arial",14),bg="#4062DD",fg="white",borderwidth=0,command=valider)
btnValider.place(x=800,y=400,width=180)

#BOUTON ANNULER
btnAnnuler=Button(fenetre,text="Annuler",font=("Arial",14),bg="#4062DD",fg="white",borderwidth=0,command=annuler)
btnAnnuler.place(x=600,y=400,width=180)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)
#-----------------------------------LES WIDGETS--------------------------------------------------------------

fenetre.mainloop()