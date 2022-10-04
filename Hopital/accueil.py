from tkinter import *
from subprocess import call
from tkinter import messagebox
import customtkinter
import pickle
import mysql.connector
from PIL import ImageTk,Image

def hide_me(widget):
    widget.place_forget()
def deconnection():
    mbox = messagebox.askquestion("Deconnecter","Voulez-vous vraiment vous deconnecter?")
    if(mbox=='yes'):
        fenetre.destroy()
        call(["python", "connectPage.py"])

def nb_docteur():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("SELECT COUNT(num_personnel) FROM personnels")
    for row in curser:
        r = row[0]
        val = str(r)
    return val
    con.close()

def nb_patient():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("SELECT COUNT(id_patient) FROM patient")
    for row in curser:
        r = row[0]
        val = str(r)
    return val
    con.close()

def nb_dep():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("SELECT COUNT(num_dep) FROM departement")
    for row in curser:
        r = row[0]
        val = str(r)
    return val
    con.close()


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
fenetre.iconbitmap("logo1.ico")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")

#DESERIALISATION
with open("test.pickle","rb") as infile:
    res = pickle.load(infile)
print(res)
i = res[0]
fonction = i[6]
nom = i[2]
idS = i[0]

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="I KA DOCTOROSO",font=("Sans Serif bold",26),
                   background="#4062DD",foreground="#FFFFFF")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=30)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),text="LES STATISTIQUES",
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=500,y=150,width=200,height=30)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text= nom+" bienvenue sur votre espace de travail",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#FRAME
dash = Frame(fenetre,background="#4062DD")
dash.place(x=0,y=90,width=200,height=480)

stat = Frame(fenetre,background="gray",highlightthickness=4)
stat.place(x=280,y=220,width=200,height=90)

statPt = Frame(fenetre,background="orange",highlightthickness=4)
statPt.place(x=540,y=220,width=200,height=90)

statD = Frame(fenetre,background="green",highlightthickness=4)
statD.place(x=800,y=220,width=200,height=90)

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

btnDeconnecter=customtkinter.CTkButton(master=dash,text="Deconnecter",text_font=("Arial",10),text_color="white",bg_color="#4062DD",fg_color="#3D88F9",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)

#STATISTIQUE
labelDr = Label(stat,borderwidth=0,relief=SUNKEN,text="Personnel",font=("Arial bold",15),
                   background="gray",foreground="#FFFFFF")
labelDr.place(x=50,y=20,width=100,height=20)

labelDrCh = Label(stat,borderwidth=0,relief=SUNKEN,text=nb_docteur(),font=("Arial bold",15),
                   background="gray",foreground="#FFFFFF")
labelDrCh.place(x=50,y=50,width=100,height=20)

labelPatient = Label(statPt,borderwidth=0,relief=SUNKEN,text="Patient",font=("Arial bold",15),
                   background="orange",foreground="#FFFFFF")
labelPatient.place(x=50,y=20,width=100,height=20)

labelPatientCh = Label(statPt,borderwidth=0,relief=SUNKEN,text=nb_patient(),font=("Arial bold",15),
                   background="orange",foreground="#FFFFFF")
labelPatientCh.place(x=50,y=50,width=100,height=20)

labelDep = Label(statD,borderwidth=0,relief=SUNKEN,text="Departement",font=("Arial bold",15),
                   background="green",foreground="#FFFFFF")
labelDep.place(x=25,y=20,width=150,height=20)

labelDepCh = Label(statD,borderwidth=0,relief=SUNKEN,text=nb_dep(),font=("Arial bold",15),
                   background="green",foreground="#FFFFFF")
labelDepCh.place(x=50,y=50,width=100,height=20)

#logo
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)

if(fonction == 'DOCTEUR'):
    hide_me(btnPersonnel)
    hide_me(btnDepartement)
    hide_me(btnComptabilite)
    btnPatient.place(x=10,y=110)
    btnOrdonnance.place(x=10,y=160)
    btnRdv.place(x=10,y=210)
elif(fonction == 'SECRETAIRE'):
    hide_me(btnPersonnel)
    hide_me(btnDepartement)
    hide_me(btnOrdonnance)
    btnPatient.place(x=10, y=110)
    btnComptabilite.place(x=10, y=160)
    btnRdv.place(x=10, y=210)
print(fonction)
infile.close()
with open("doc.pickle","wb") as outfile:
    pickle.dump(fonction,outfile)
outfile.close()
with open("id.pickle","wb") as outfile:
    pickle.dump(idS,outfile)
outfile.close()
fenetre.mainloop()