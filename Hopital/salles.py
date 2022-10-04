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

def nom_dep():
    con = mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
    curser = con.cursor()
    curser.execute("SELECT nom_dep FROM departement WHERE num_dep ={}".format(id))
    for row in curser:
        r = row[0]
        val = str(r)
    return val
    con.close()


def rechercher():
    if(entryname.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer un numero de salle")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM salle WHERE nom_salle ='"+ entryname.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            entryname_lit.insert(0, row[3])
        con.close()
def modifier():
    numeroSalle = entryname.get()
    numeroLit = entryname_lit.get()

    if (numeroSalle=="" or numeroLit == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("update salle set nom_salle='"+numeroSalle+"',nombre_lit="+numeroLit+" WHERE nom_salle='"+ numeroSalle+"'")
        cursor.execute("commit")

        entryname.delete(0, 'end')
        entryname_lit.delete(0, 'end')
        messagebox.showinfo("Modification ", "Modifier avec succès")
        afficher()
        con.close()
def ajouter():
    nomSalle = entryname.get()
    nombreLit = entryname_lit.get()

    print(id)
    if (nomSalle=="" or nombreLit == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit être vide")
        afficher()
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("INSERT INTO salle (num_dep,nom_salle,nombre_lit) VALUES ("+id+",'"+nomSalle+"',"+nombreLit+")")
        cursor.execute("commit")

        entryname.delete(0, 'end')
        entryname_lit.delete(0, 'end')
        messagebox.showinfo("Patient ajouter ", "Inserer avec succès")
#afficher
        afficher()
        con.close();
def supprimer():
    if(entryname.get() == ""):
        messagebox.showinfo("Suppression ", "Spécifier l'ID du patient à supprimer")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("DELETE FROM salle WHERE nom_salle ='"+ entryname.get() +"'")
        cursor.execute("commit")

        entryname.delete(0, 'end')
        entryname_lit.delete(0, 'end')
        messagebox.showinfo("Suppression ", "Supprimer avec succès")
        afficher()
        con.close();

#afficher
def afficher():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT id_salle,nom_salle,nombre_lit,SUM(id_salle) FROM salle WHERE num_dep ="+id+" GROUP BY id_salle")
    table.delete(*table.get_children())
    records = cursor.fetchall()
    for i in records:
        table.insert("", "end", values=i)
        con.close()

fenetre = Tk()

#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Salle")
fenetre.iconbitmap("logo1.ico")
fenetre.resizable(False,False)
fenetre.configure(background="#FFFFFF")

#DESERIALISATION
with open("urgence.pickle","rb") as infile:
    res = pickle.load(infile)
id = str(res)

#titre
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="I KA DOCTOROSO",font=("Sans Serif bold",26),
                   background="#4062DD",foreground="#FFFFFF")
labelTitre.place(x=0,y=0,width=1080,height=60)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=60,width=200,height=30)

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="DEPARTEMENT "+nom_dep(),font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#BOUTON RETOUR
btnretour= Button(fenetre, text="Retour", background="#7DA0D6", font=('time new rooman',15),command=Depatement)
btnretour.place(x=200, y=60,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

#FRAME
dash = Frame(fenetre,background="#4062DD")
dash.place(x=0,y=90,width=200,height=480)


labelname = Label(fenetre, text=" SALLES " ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=260, y=95 )

labelname = Label(fenetre, text=" Nom salle :" ,font=('time new rooman',12))
labelname.place(x=250, y=130 )

# Entrez num_salle
entryname= Entry(fenetre, bg="#D9D9D9")
entryname.place(x=400, y=130, width=180)


# Information Lit

labelname = Label(fenetre, text=" LIT " ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=630, y=95 )

labelname = Label(fenetre, text=" Nombre lit :" ,font=('time new rooman',12))
labelname.place(x=630, y=130 )

# Entrez num_lit
entryname_lit= Entry(fenetre, bg="#D9D9D9")
entryname_lit.place(x=759, y=130, width=180)

##BOUTON Ajouter
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
#Titre tableau
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="LISTE DES SALLES",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=300,width=880,height=30)



#Table
table = ttk.Treeview(fenetre,columns=(1,2,3,4,5),height=5,show="headings",)
table.place(x=200,y=330,width=880,height=240)

style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")

#Entete
table.heading(1,text="ID",)
table.heading(2,text="NOM SALLE")
table.heading(3,text="NOMBRE LIT")
table.heading(4,text="NOMBRE SALLE")
table.column(1,width=50)

verscrlbar = ttk.Scrollbar(fenetre,orient="vertical",command=table.yview)
verscrlbar.place(x=1068,y=357,height=213)

table.configure(xscrollcommand=verscrlbar.set)

con= mysql.connector.connect(host="localhost", user="root", password="", database='hopital')
curser = con.cursor()
curser.execute("SELECT id_salle,nom_salle,nombre_lit,SUM(id_salle) FROM salle WHERE num_dep ="+id+" GROUP BY id_salle")
for row in curser:
    table.insert('',END, value= row)
con.close()
#logo
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)
fenetre.mainloop()