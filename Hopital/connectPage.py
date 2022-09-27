from tkinter import *
from subprocess import call
from tkinter import messagebox
import mysql.connector
import customtkinter

#Afficher le mot de passe
def toggle_password():
    if txtMotDePasse.cget('show') == '':
        txtMotDePasse.config(show='*')
        btn_afficher.config(image=image2)
    else:
        txtMotDePasse.config(show='')
        btn_afficher.config(image=image)
def creer_compte():
    fenetre.destroy()
    call(["python","creerCompte.py"])

def seConnecter():
    nomUtilisteur = txtUtilisateur.get()
    password = txtMotDePasse.get()
    if (nomUtilisteur == "" or password == ""):
        messagebox.showinfo("Echec", "Aucun champ ne doit etre vide")
    else:
        try:
            sql = "SELECT * FROM personnels WHERE nom_utilisateur =%s AND mot_de_passe =%s"
            valeur = (nomUtilisteur,password)
            con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
            curser = con.cursor()
            curser.execute(sql,valeur)
            resultat =curser.fetchall()
            if resultat:
                messagebox.showinfo("INFO", "Connecter avec succès")
                fenetre.destroy()
                call(["python", "accueil.py"])
            else:
                messagebox.showinfo("Erreur", "Nom d'utilisateur ou mot de passe incorrect")
        except:
            messagebox.showinfo("Erreur", "Problème de connexion")

#MAIN________________________________________________________________________
#nouvelle fenetre:
fenetre = Tk()

#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("I KA DOCTOROSO")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="I KA DOCTOROSO",font=("Sans Serif bold",26),
                   background="#4062DD",foreground="#FFFFFF")
labelTitre.place(x=0,y=0,width=1080,height=60)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#titre de page
lblUtilisateur =Label(fenetre,text="LOGIN",font=("Arial, Bold",25),
                   bg="#FFFFFF",foreground="#000000")
lblUtilisateur.place(x=800,y=100,width=180)

#Nom d'utilisateur
lblUtilisateur =Label(fenetre,text="Nom d'utilisateur",font=("Arial, Bold",18),
                   bg="#FFFFFF",foreground="#000000")
lblUtilisateur.place(x=600,y=200,width=180)
txtUtilisateur = Entry(fenetre, textvariable=lblUtilisateur,bd=2,font=("Arial",12))
txtUtilisateur.place(x=800,y=200,width=200,height=30)

#Mot de passe
lblMotDePasse =Label(fenetre,text="Mot de passe",font=("Arial, Bold",18),
                   bg="#FFFFFF",foreground="#000000")
lblMotDePasse.place(x=580,y=280,width=180)
txtMotDePasse = Entry(fenetre,textvariable=lblMotDePasse,show="*",bd=2,font=("Arial",12))
txtMotDePasse.place(x=800,y=280,width=200,height=30)
image = PhotoImage(file="eye.png")
image2 = PhotoImage(file="invisible.png")
btn_afficher = Button(fenetre,image=image2, command=toggle_password)
btn_afficher.place(x=975,y=280)

#Bouton se connecter

btnSeConnecter=customtkinter.CTkButton(master=fenetre,text="Se connecter",text_font=("Arial",14),text_color="white",bg_color="white",fg_color="#4062DD",hover=True,hover_color="#4062DD",border_width=1,corner_radius=10,command=seConnecter)
btnSeConnecter.place(x=840,y=350,width=170)
#Bouton creer compte
btnCreerCompte=customtkinter.CTkButton(master=fenetre,text="Creer un compte",text_font=("Arial",14),text_color="white",bg_color="white",fg_color="#4062DD",hover=True,hover_color="#4062DD",border_width=1,corner_radius=10,command=creer_compte)
btnCreerCompte.place(x=840,y=400,width=170)


fenetre.mainloop()