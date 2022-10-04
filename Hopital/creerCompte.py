from tkinter import *
from tkinter import ttk
from subprocess import call
from tkinter import messagebox
import tkcalendar
import mysql.connector
import customtkinter
from PIL import ImageTk,Image
def toggle_password():
    if txtMdp.cget('show') == '':
        txtMdp.config(show='*')
        btn_afficher.config(image=image2)
    else:
        txtMdp.config(show='')
        btn_afficher.config(image=image)

def toggle_password2():
    if txtConfirmer.cget('show') == '':
        txtConfirmer.config(show='*')
        btn_afficher.config(image=image2)
    else:
        txtConfirmer.config(show='')
        btn_afficher.config(image=image)
def annuler():
    fenetre.destroy()
    call(["python","connectPage.py"])

def valider():
    nom = txtNom.get()
    sex = sexe.get()
    dateN = txtDateN.get()
    contact = txtContact.get()
    fn = fonction.get()
    dep = departement.current()+1
    special = Specialite.get()
    nomUtisateur = txtUtilisateur.get()
    mot_de_passe = txtMdp.get()
    confimer = txtConfirmer.get()
    dateIns = txtDateIns.get()
    if(nom==""or sex=="" or dateN==""or contact==""or fn=="" or nomUtisateur=="" or mot_de_passe==""
    or confimer==""or dateIns==""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit être vide")
    elif (mot_de_passe != confimer):
        messagebox.showinfo("Information", "Votre mot de passe est différent de celui de la confirmation")
    elif (len(mot_de_passe)<8):
        messagebox.showinfo("Information", "Votre mot de passe ne doit pas être inferieur à 8 caractère")
    else:
        sql = "INSERT INTO personnels(num_dep,nom,sexe,date_naissance,contact,fonction,date_insertion," \
              "specialite,nom_utilisateur,mot_de_passe,Confirmer)" \
              " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

        val = "INSERT INTO directeur(num_personnel) SELECT num_personnel FROM personnels WHERE fonction = 'DIRECTEUR'"
        val1 ="INSERT INTO docteur(num_personnel) SELECT num_personnel FROM personnels WHERE fonction = 'DOCTEUR'"
        val3 ="INSERT INTO secretaire(num_personnel) SELECT num_personnel FROM personnels WHERE fonction = 'SECRETAIRE'"
        valeur = (dep, nom, sex,dateN,contact,fn,dateIns,special,nomUtisateur,mot_de_passe,confimer)
        maBase = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        mConnect = maBase.cursor()
        mConnect.execute(sql, valeur)
        mConnect.execute(val)
        mConnect.execute(val1,)
        mConnect.execute(val3,)
        maBase.commit()
        messagebox.showinfo("Information", "insertion effectuer")
        fenetre.destroy()
        call(["python","connectPage.py"])
#----------------------------------------------MAIN----------------------------------------------------------
fenetre = Tk()
#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Créer compte")
fenetre.iconbitmap("logo1.ico")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="I KA DOCTOROSO",font=("Sans Serif bold",26),
                   background="#4062DD",foreground="#FFFFFF")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=30)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="#4062DD",foreground="#000000")
labelTitre.place(x=0,y=90,width=200,height=30)

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
sexe = ttk.Combobox(fenetre,state="readonly",values=content)

sexe.place(x=200,y=180,width=180)

#Date naissance

lblDateN =Label(fenetre,text="Date de naissance :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDateN.place(x=16,y=220,width=180)
txtDateN = tkcalendar.DateEntry(fenetre,bd=2,font=("Times New Roman",12),date_pattern = "YYYY-MM-DD")
txtDateN.place(x=200,y=220,width=180)

#Contact

lblContact =Label(fenetre,text="Contact :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblContact.place(x=16,y=260,width=180)
txtContact = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtContact.place(x=200,y=260,width=180)

#FONCTION
liste =['DIRECTEUR','DOCTEUR','SECRETAIRE']

lblFonction =Label(fenetre,text="Fonction :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblFonction.place(x=16,y=300,width=180)
fonction = ttk.Combobox(fenetre,state="readonly",values=liste)
fonction.place(x=200,y=300,width=180)

#DEPARTEMENT
liste =['URGENCE','ODONTOLOGIE','TRAUMATOLOGIE','CHIRURGIE','GYNECOLOGIE','PEDIATRIE','AUTRE']

lblDepartement =Label(fenetre,text="Département :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDepartement.place(x=16,y=340,width=180)
departement = ttk.Combobox(fenetre,state="readonly",values=liste)

departement.place(x=200,y=340,width=180)

#SPECIALITE

specialite =['PEDIATRE','TRAUMATOLOGUE','GYNECOLOGUE','GENERALISTE','CHIRURGIEN','ODONTOLOGUE','AUTRE']

lblSpecialite =Label(fenetre,text="Spécialité :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSpecialite.place(x=600,y=140,width=180)
Specialite = ttk.Combobox(fenetre,state="readonly",values=specialite)

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
txtMdp = Entry(fenetre,bd=2,show="*",font=("Times New Roman",12))
txtMdp.place(x=800,y=220,width=180)
image = PhotoImage(file="eye.png")
image2 = PhotoImage(file="invisible.png")
btn_afficher = Button(fenetre,image=image2, command=toggle_password)
btn_afficher.place(x=955,y=220,height=25)

#MOT DE PASSE CONFIRMATION

lblConfirmer =Label(fenetre,text="Confirmer :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblConfirmer.place(x=600,y=260,width=180)
txtConfirmer = Entry(fenetre,bd=2,show="*",font=("Times New Roman",12))
txtConfirmer.place(x=800,y=260,width=180)
btn_afficher = Button(fenetre,image=image2, command=toggle_password2)
btn_afficher.place(x=955,y=260,height=25)

#Date Insertion

lblDateIns =Label(fenetre,text="Date d'insertion :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblDateIns.place(x=600,y=300,width=180)
txtDateIns = tkcalendar.DateEntry(fenetre,bd=2,font=("Times New Roman",12),date_pattern = "YYYY-MM-DD")
txtDateIns.place(x=800,y=300,width=180)

#BOUTON VALIDER
btnValider=customtkinter.CTkButton(master=fenetre,text="Valider",text_font=("Arial",14),text_color="white",bg_color="white",fg_color="#4062DD",hover=True,hover_color="#4062DD",border_width=1,corner_radius=10,command=valider)
btnValider.place(x=800,y=400,width=180)

#BOUTON ANNULER
btnAnnuler=customtkinter.CTkButton(master=fenetre,text="Annuler",text_font=("Arial",14),text_color="white",bg_color="white",fg_color="#4062DD",hover=True,hover_color="#4062DD",border_width=1,corner_radius=10,command=annuler)
btnAnnuler.place(x=600,y=400,width=180)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)
#-----------------------------------LES WIDGETS--------------------------------------------------------------
#logo
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)
fenetre.mainloop()