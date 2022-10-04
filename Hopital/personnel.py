from tkinter import *
from subprocess import call
from tkinter import messagebox, ttk
from PIL import ImageTk,Image
import customtkinter
from tkcalendar import DateEntry
import mysql.connector


def les_depatements():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT nom_dep FROM departement ")
    dep = cursor.fetchall()
    departement = list(dep)
    print(departement)
    con.close()
    return departement
def rechercher():
    if(txtTelephone.get() == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer le numéro du patient à chercher")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM personnels WHERE contact ='"+ txtTelephone.get() +"'")
        rows = cursor.fetchall()

        txtAge_personne.delete(0, 'end')
        txtinscrit.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        for row in rows:
            txtNom.insert(0, row[2])
            sexe.insert(0, row[3])
            txtAge_personne.insert(0, row[4])
            txtTelephone.insert(0, row[5])
            fonction.insert(0, row[6])
            txtinscrit.insert(0,row[7])
            txtAdresse.insert(0, row[8])
        con.close()
#DESACTIVATION DU BOUTON RECHERCHER APRES UNE RECHERCHE
        if txtTelephone!= 0:
            btnrechercher.configure(state=DISABLED)

def modifier():
    nom_personnel = txtNom.get()
    sex = sexe.get()
    dateN = txtAge_personne.get()
    dateIns = txtinscrit.get()
    adresse = txtAdresse.get()
    telephone = txtTelephone.get()
    fonct = fonction.get()
    depat = departement.get()

    idDep = 0
    if (depat == 'URGENCE'):
        idDep = 1
    elif (depat == 'ODONTOLOGIE'):
        idDep = 2
    elif (depat == 'TRAUMATOLOGIE'):
        idDep = 3
    elif (depat == 'CHIRURGIE'):
        idDep = 4
    elif (depat == 'GYNECOLOGIE'):
        idDep = 5
    elif (depat == 'PEDIATRIE'):
        idDep = 6
    elif (depat == 'AUTRE'):
        idDep = 7

    id1 = str(idDep)

    if (nom_personnel == "" or sex == "" or dateN == "" or dateIns=="" or adresse == "" or telephone == "" or fonct == "" or depat == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("update personnels set num_dep ="+ id1 +", nom='"+ nom_personnel+"',sexe='"+ sex +"',date_naissance='"+ dateN+"',adresse='"+ adresse +"',contact='"+ telephone +"',fonction='"+ fonct +"',date_insertion='"+ dateIns+"' WHERE contact='"+ telephone +"'")
        cursor.execute("commit")

        txtNom.delete(0, 'end')
        sexe.delete(0, 'end')
        txtAge_personne.delete(0, 'end')
        txtinscrit.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        fonction.delete(0, 'end')
        departement.delete(0, 'end')
        messagebox.showinfo("Modification ", "Modifier avec succès")
        afficher()
        con.close()
def ajouter():
    nom_personnel = txtNom.get()
    sex = sexe.get()
    dateN = txtAge_personne.get()
    dateIns = txtinscrit.get()
    adresse = txtAdresse.get()
    telephone = txtTelephone.get()
    fonct = fonction.get()
    depat = departement.get()

    if (nom_personnel == "" or sex == "" or dateN == "" or dateIns=="" or adresse == "" or telephone == "" or fonct == "" or depat == ""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        idDep = 0
        if(depat == 'URGENCE'):
            idDep  = 1
        elif(depat  == 'ODONTOLOGIE'):
            idDep = 2
        elif(depat == 'TRAUMATOLOGIE'):
            idDep = 3
        elif(depat == 'CHIRURGIE'):
            idDep = 4
        elif (depat == 'GYNECOLOGIE'):
            idDep = 5
        elif (depat == 'PEDIATRIE'):
            idDep = 6
        elif (depat == 'AUTRE'):
            idDep = 7

        id1  = str(idDep)
        cursor.execute( "INSERT INTO personnels (num_dep,nom,sexe,date_naissance,contact,fonction,date_insertion,adresse) VALUES ("+id1+ ",'" + nom_personnel + "','" + sex + "','" + dateN + "','" + telephone + "','" + fonct + "','" + dateIns + "','"+adresse+"')")
        cursor.execute("commit")
        print(idDep)
        messagebox.showinfo("Personnel ajouter ", "Ajouter avec succès")

        txtNom.delete(0, 'end')
        sexe.delete(0, 'end')
        txtAge_personne.delete(0, 'end')
        txtinscrit.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        fonction.delete(0, 'end')
        departement.delete(0, 'end')
#afficher
        afficher()
        btnrechercher.configure(state=ACTIVE)
        con.close()
def supprimer():
    if(txtTelephone.get() == ""):
        messagebox.showinfo("Suppression ", "Spécifier l'ID du patient à supprimer")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("DELETE FROM personnels WHERE contact ='"+ txtTelephone.get() +"'")
        cursor.execute("commit")

        txtNom.delete(0, 'end')
        sexe.delete(0, 'end')
        txtAge_personne.delete(0, 'end')
        txtinscrit.delete(0, 'end')
        txtAdresse.delete(0, 'end')
        txtTelephone.delete(0, 'end')
        fonction.delete(0, 'end')
        departement.delete(0, 'end')
        messagebox.showinfo("Suppression ", "Supprimer avec succès")
        afficher()
        con.close()
def afficher():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT p.num_personnel,d.nom_dep,p.nom,p.sexe,p.date_naissance,p.contact,p.fonction,p.date_insertion,p.adresse FROM personnels p,departement d WHERE d.num_dep = p.num_dep")
    tree.delete(*tree.get_children())
    records = cursor.fetchall()
    print(records)

    for i, (num_personnel,nom_dep,nom,sexe,date_naissance,contact,fonction,date_insertion,adresse) in enumerate(records, start=1):
        tree.insert("", "end", values=(num_personnel,nom_dep,nom,sexe,date_naissance,contact,fonction,date_insertion,adresse))
        con.close()
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
fenetre.title("Personnel")
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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE PERSONNEL",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)


#NOM et Prenom du Personnel

lblNom =Label(fenetre,text="Nom :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblNom.place(x=216,y=120,width=180)
txtNom = Entry(fenetre,bd=2,font=("Times New Roman",12))
txtNom.place(x=400,y=120,width=180)

#SEXE

content =['Homme','Femme']

lblSexe =Label(fenetre,text="sexe :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblSexe.place(x=216,y=160,width=180)
sexe = ttk.Combobox(fenetre,values=content)
sexe.place(x=400,y=160,width=180)

#Age_Personnel

lblAge_personel =Label(fenetre,text="Date de Naissance :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblAge_personel.place(x=216,y=190,width=180)
txtAge_personne = DateEntry(fenetre,bd=2,font=("Times New Roman",12),date_pattern="YYYY-MM-DD")
txtAge_personne.place(x=400,y=190,width=180)

#Date

lblinscrit =Label(fenetre,text="Date d'inscription :",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lblinscrit.place(x=216,y=220,width=180)
txtinscrit = DateEntry(fenetre,bd=2,font=("Times New Roman",12), date_pattern="YYYY-MM-DD")
txtinscrit.place(x=400,y=220,width=180)
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
list = ['URGENCE','ODONTOLOGIE','TRAUMATOLOGIE','CHIRURGIE','GYNECOLOGIE','PEDIATRIE','AUTRE']

lbldepart =Label(fenetre,text="Département:",font=("Times New Roman",14),
                   bg="#FFFFFF",foreground="#000000")
lbldepart.place(x=600,y=220,width=200)
departement = ttk.Combobox(fenetre,values=list)
departement.place(x=800, y=220, width=180)


#Boutton ajouter
btnajouter= customtkinter.CTkButton(master=fenetre,text="Ajouter",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#20843C",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=ajouter)
btnajouter.place(x=250, y=300)

#Boutton Modifier
btnmodifier= customtkinter.CTkButton(master=fenetre,text="Modifier",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#1B3864",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=modifier)
btnmodifier.place(x=450, y=300)

#Boutton Supprimer
btnsuprimer= customtkinter.CTkButton(master=fenetre,text="Supprimer",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#F46464",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=supprimer)
btnsuprimer.place(x=650, y=300)

#Boutton Rechercher
btnrechercher= customtkinter.CTkButton(master=fenetre,text="Rechercher",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#DC8014",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=rechercher)
btnrechercher.place(x=850, y=300)

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
tree.heading(2, text= "Departement")
tree.heading(3, text= "Nom")
tree.heading(4, text= "Sexe")
tree.heading(5, text= "Date de naissance")
tree.heading(6, text= "Contact")
tree.heading(7, text= "Fonction")
tree.heading(8, text= "Date d'inscription")
tree.heading(9, text= "Adresse")
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
btnAccueil=customtkinter.CTkButton(master=dash,text="Accueil",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Accueil)
btnAccueil.place(x=10,y=60,width=180)
btnPersonnel=customtkinter.CTkButton(master=dash,text="Personnel",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#0052CC",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Personnel)
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
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)
afficher()
fenetre.mainloop()