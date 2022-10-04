from tkinter import *
from subprocess import call
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import customtkinter
import pickle
from PIL import ImageTk,Image

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

def Urgence():
    with open("urgence.pickle", "wb") as outfile:
        pickle.dump(1, outfile)
    outfile.close()
    Salle()

def Odontolologie():
    with open("urgence.pickle", "wb") as outfile:
        pickle.dump(2, outfile)
    outfile.close()
    Salle()
def Traumatologie():
    with open("urgence.pickle", "wb") as outfile:
        pickle.dump(3, outfile)
    outfile.close()
    Salle()

def Chirurgie():
    with open("urgence.pickle", "wb") as outfile:
        pickle.dump(4, outfile)
    outfile.close()
    Salle()
def Gynecologie():
    with open("urgence.pickle", "wb") as outfile:
        pickle.dump(5, outfile)
    outfile.close()
    Salle()

def Pediatrie():
    with open("urgence.pickle", "wb") as outfile:
        pickle.dump(6, outfile)
    outfile.close()
    Salle()

def Salle():
    fenetre.destroy()
    call(["python", "salles.py"])

#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Département")
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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE DEPARTEMENT",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

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
btnDepartement=customtkinter.CTkButton(master=dash,text="Département",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#0052CC",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Depatement)
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
btnUrgence=Button(fenetre,text="URGENCE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Urgence)
btnUrgence.place(x=300,y=200,width=180,height=50)

btnOdonto=Button(fenetre,text="ODONTOLOGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Odontolologie)
btnOdonto.place(x=550,y=200,width=180,height=50)

btnTrauma=Button(fenetre,text="TRAUMATOLOGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Traumatologie)
btnTrauma.place(x=800,y=200,width=180,height=50)

btnChirurgie=Button(fenetre,text="CHIRURGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Chirurgie)
btnChirurgie.place(x=300,y=300,width=180,height=50)

btnGynecologie=Button(fenetre,text="GYNECOLOGIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Gynecologie)
btnGynecologie.place(x=550,y=300,width=180,height=50)

btnPediatrie=Button(fenetre,text="PEDIATRIE",font=("Arial",12),bg="#4062DD",fg="black",borderwidth=0,command=Pediatrie)
btnPediatrie.place(x=800,y=300,width=180,height=50)
#logo
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)
fenetre.mainloop()