from tkinter import *
from tkcalendar import *
from subprocess import call
from tkinter import messagebox, ttk
import mysql.connector
import pickle
from PIL import ImageTk,Image
import customtkinter

def Id_secretaire():
    with open("id.pickle", "rb") as infile:
        id1 = pickle.load(infile)
        id = str(id1)
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
    cur = mysqldb.cursor()
    cur.execute("select num_secretaire FROM secretaire WHERE num_personnel ="+id)
    c = cur.fetchone()
    a = c[0]
    return a
def les_patients():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT id_patient,nom_patient FROM patient")
    doc = cursor.fetchall()
    pat = list(doc)
    con.close()
    return pat
def ajouter():
    id = Id_secretaire()
    i = str(id)
    print(i)
    numero = entrynumero.get()
    Date_payement = entrydatepayement.get()
    Montant = entrymontant.get()

    if (numero == "" or Date_payement == "" or Montant == "" ):
        messagebox.showerror("Erreur","Tous les champs sont obligatoires")
    else:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cur = mysqldb.cursor()
        cur.execute("insert into comptabilite (nom_patient,num_secretaire, date_payement, montant) values ('"+ numero +"',"+ i +", '" + Date_payement + "', " + Montant + ")")
        cur.execute("commit")
        messagebox.showinfo("Insert Status", "Enregisrement reussi")
        entrynumero.delete(0, 'end')
        entrydatepayement.delete(0, 'end')
        entrymontant.delete(0, 'end')
        mysqldb.close()
        afficher()

def modifier():
    nomPatient = entrynumero.get()
    date = entrydatepayement.get()
    montant = entrymontant.get()

    if (nomPatient=="" or date == ""or montant ==""):
        messagebox.showinfo("Erreur:", "Aucun champ ne doit etre vide")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("update comptabilite set nom_patient='"+nomPatient+"',date_payement="+date+",montant="+montant+" WHERE nom_patient='"+ nomPatient+"'")
        cursor.execute("commit");

        nomPatient.delete(0, 'end')
        date.delete(0, 'end')
        montant.delete(0, 'end')
        messagebox.showinfo("Modification ", "Modifier avec succès")
        afficher()
        con.close()
def Rechercher():
    numero = entrynumero.get()
    Date_payement = entrydatepayement.get()
    Montant = entrymontant.get()

    if (numero==""):
        messagebox.showinfo("Erreur","Entrer un nom patient")
    else:
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cur = mysqldb.cursor()
        cur.execute("select * from comptabilite where nom_patient ='" + entrynumero.get() + "'")
        rows = cur.fetchall()

        entrydatepayement.delete(0, 'end')

        for row in rows:
            entrynumero.insert(0, row[2])
            entrydatepayement.insert(0, row[3])
            entrymontant.insert(0, row[4])

        mysqldb.close()
def supprimer():
    if(entrynumero.get() == ""):
        messagebox.showinfo("Suppression ", "Spécifier le nom du patient à supprimer")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("DELETE FROM comptabilite WHERE nom_patient ='"+ entrynumero.get() +"'")
        cursor.execute("commit")

        entrynumero.delete(0, 'end')
        entrydatepayement.delete(0, 'end')
        entrymontant.delete(0, 'end')
        messagebox.showinfo("Suppression ", "Supprimer avec succès")
        afficher()
        con.close()

#afficher
def afficher():
    con = mysql.connector.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT nom_patient,date_payement,montant FROM comptabilite")
    tree.delete(*tree.get_children())
    records = cursor.fetchall()
    for i in records:
        tree.insert("", "end", values=i)
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

def hide_me(widget):
    widget.place_forget()
fenetre = Tk()


#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("Comptabilité")
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

labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="BIENVENUE SUR LA PAGE COMPTABILITE",font=("Sans Serif bold",20),
                   background="#7DA0D6",foreground="#000000")
labelTitre.place(x=200,y=60,width=880,height=30)

#pied de page
labelTitre = Label(fenetre,borderwidth=0,relief=SUNKEN,text="Copyright:tout droit reservé",font=("Arial Bold",10),
                   background="#1D314F",foreground="#000000")
labelTitre.place(x=0,y=570,width=1080,height=30)

# Titre Nom et Prénom de la persone à payé
labelnumero = Label(fenetre, text="Nom Patient", background="#7DA0D6",font=('time new rooman',12))
labelnumero.place(x=250, y=130 )
l = les_patients()
l1 = l[0]
liste2 = l1[1]
# Entrez le nom du Patient
entrynumero= ttk.Combobox(fenetre,state="readonly",values=liste2)
entrynumero.configure(font=('time new rooman',15))
entrynumero.place(x=420, y=130, width=180)

# Titre date de payement de la persone
labeldate = Label(fenetre, text="Date de payement", background="#7DA0D6",font=('time new rooman',12))
labeldate.place(x=250, y=210 )

# Entrez la date de payement de la personne
entrydatepayement= DateEntry(fenetre, bg="#D9D9D9", date_pattern="yyyy-mm-dd")
entrydatepayement.place(x=420, y= 210,width=180)

# Titre du montant de payement
lblmontant= Label(fenetre, bg="#7DA0D6", text="Montant")
lblmontant.configure(font=('time new rooman',15))
lblmontant.place(x=630, y=130)
# Le montant
entrymontant= Entry(fenetre, bg="#D9D9D9")
entrymontant.configure(font=('time new rooman',15))
entrymontant.place(x=790, y=130, width=180)

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

#Boutton ajouter
btnajouter= customtkinter.CTkButton(master=fenetre,text="Ajouter",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#20843C",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=ajouter)
btnajouter.place(x=250, y=270)

#Boutton Modifier
btnmodifier= customtkinter.CTkButton(master=fenetre,text="Modifier",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#1B3864",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=modifier)
btnmodifier.place(x=450, y=270)

#Boutton Supprimer
btnsuprimer= customtkinter.CTkButton(master=fenetre,text="Supprimer",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#F46464",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=supprimer)
btnsuprimer.place(x=650, y=270)

#Boutton Rechercher
btnrechercher= customtkinter.CTkButton(master=fenetre,text="Rechercher",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#DC8014",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Rechercher)
btnrechercher.place(x=850, y=270)

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
tree.heading(3, text= "Montant")
tree.column(1, width= 200)
tree.column(2, width= 200)
tree.column(3, width= 200)

# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=900,y=357,height=200)

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
btnComptabilite=customtkinter.CTkButton(master=dash,text="Comptabilité",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#0052CC",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Comptabilite)
btnComptabilite.place(x=10,y=310,width=180)
btnRdv=customtkinter.CTkButton(master=dash,text="Rendez-vous",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Rdv)
btnRdv.place(x=10,y=360,width=180)

btnDeconnecter=customtkinter.CTkButton(master=dash,text="Deconnecter",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#3D88F9",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)

with open("doc.pickle","rb") as infile:
    fonction = pickle.load(infile)
if(fonction == 'SECRETAIRE'):
    hide_me(btnPersonnel)
    hide_me(btnDepartement)
    hide_me(btnOrdonnance)
    btnPatient.place(x=10, y=110)
    btnComptabilite.place(x=10, y=160)
    btnRdv.place(x=10, y=210)
    hide_me(btnsuprimer)
    btnmodifier.place(x=550)
infile.close()
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)
afficher()
fenetre.mainloop()