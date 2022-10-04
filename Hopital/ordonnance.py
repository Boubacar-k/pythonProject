from tkinter import *
from subprocess import call
from tkinter import messagebox, ttk
import mysql.connector as mysql
from tkcalendar import DateEntry
from PIL import ImageTk,Image
import pickle
import customtkinter


def imprimer():
    pass
def les_patients():
    con = mysql.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT id_patient,nom_patient FROM patient")
    doc = cursor.fetchall()
    pat = list(doc)
    con.close()
    return pat

def les_docteurs():
    con = mysql.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT num_personnel ,nom FROM personnels WHERE fonction = 'DOCTEUR'")
    doc = cursor.fetchall()
    docteur = list(doc)
    con.close()
    return docteur
def ajouter():

    nom= entryNom.get()
    Date_prescription= entrydateprescription.get()
    ID_medecin= entryid_medecin.get()
    Date_rdv= entrydate_rdv.get()
    prescription= text.get("1.0",END)

    if (nom=="" or Date_prescription=="" or ID_medecin=="" or Date_rdv=="" or prescription=="" or prescription==""):
        messagebox.showerror("Tous les champs sont Obligatoire")
    else:
        mysqldb = mysql.connect(host="localhost", user="root", password="", database="hopital")
        cur = mysqldb.cursor()
        cur.execute("insert into ordonnance (nom_patient,nom_docteur, date_prescription, prescription, date_rdv) values ('" + nom + "', '" + ID_medecin + "', '" + Date_prescription + "','" + prescription + "', '" + Date_rdv + "')")
        cur.execute("commit")
        messagebox.showinfo("Message", "Enregisrement effectué")
        entryNom.delete(0, 'end')
        entrydateprescription.delete(0, 'end')
        entryid_medecin.delete(0, 'end')
        entrydate_rdv.delete(0, 'end')
        mysqldb.close()
        afficher()
def supprimer():
    nom = entryNom.get()
    Date_prescription = entrydateprescription.get()
    Num_medecin = entryid_medecin.get()
    Date_rdv = entrydate_rdv.get()
    prescription = text.get("1.0", END)

    if (nom == ""):
        mbox = messagebox.askquestion("", "Veuillez entrez d'abord le numéro du patient que vous voulez supprimer")
    else:
        mysqldb = mysql.connect(host="localhost", user="root", password="", database="hopital")
        cur = mysqldb.cursor()
        cur.execute("DELETE FROM ordonnance WHERE nom_patient= '" + entryNom.get() + "'")
        cur.execute("commit")
        afficher()

def rechercher():
    nom = entryNom.get()
    Date_prescription = entrydateprescription.get()
    Num_medecin = entryid_medecin.get()
    Date_rdv = entrydate_rdv.get()
    prescription = text.get("1.0", END)

    if (nom == ""):
        messagebox.showinfo("Recherche ", "Veuillez entrer le nom de patient")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="hopital")
        cursor = con.cursor()
        cursor.execute("SELECT * FROM ordonnance WHERE nom_patient ='" + entryNom.get() + "'")
        rows = cursor.fetchall()
        entrydateprescription.delete(0, 'end')
        for row in rows:
            entryid_medecin.insert(0, row[2])
            entrydateprescription.insert(0, row[3])
            prescription.insert(0, row[4])
            entrydate_rdv.insert(0, row[5])
        con.close()
def modifier():
    nom = entryNom.get()
    Date_prescription = entrydateprescription.get()
    ID_medecin = entryid_medecin.get()
    Date_rdv = entrydate_rdv.get()
    prescription = text.get("1.0", END)

    if (nom == ""):
        messagebox.showerror("Le numéro du patient est obligatoire")
    else:
        mysqldb = mysql.connect(host="localhost", user="root", password="", database="hopital")
        cur = mysqldb.cursor()
        cur.execute(
            "update ordonnance set  nom_patient='" + nom + "', nom_docteur='" + ID_medecin + "', date_prescription='" + Date_prescription + "', prescription='" + prescription + "', date_rdv='" + Date_rdv + "' where nom_patient='" + nom + "'")
        cur.execute("commit")
        messagebox.showinfo("Insert Status", "Modification reçu")
        entryNom.delete(0, 'end')
        entrydateprescription.delete(0, 'end')
        entryid_medecin.delete(0, 'end')
        entrydate_rdv.delete(0, 'end')
        text.delete(0, 'end')
        mysqldb.close()
        afficher()



def afficher():
    con = mysql.connect(host="localhost", user="root", password="", database="hopital")
    cursor = con.cursor()
    cursor.execute("SELECT num_ordonnance,nom_patient,nom_docteur,date_prescription,prescription,date_rdv FROM ordonnance")
    tree.delete(*tree.get_children())
    records = cursor.fetchall()
    for i in records:
        tree.insert("", "end", values=i)
        con.close()
    pass

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
fenetre.title("Ordonnance")
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

'''labelname = Label(fenetre, text=" Nom et Prenom :" ,font=('time new rooman',12), bg="white")
labelname.place(x=250, y=130 )

# Entrez le nom du Patient
entryname= Entry(fenetre, bg="#D9D9D9")
entryname.place(x=400, y=130, width=180)'''

# ID Patient
labelname = Label(fenetre, text=" Nom_patient :",font=('time new rooman',12), bg="white")
labelname.place(x=250, y=160 )
l = les_patients()
l1 = l[0]
liste2 = l1[1]
# Entrez l'ID du Patient
entryNom= ttk.Combobox(fenetre,values=liste2)
entryNom.place(x=400, y=160, width=180)

labelname = Label(fenetre, text="Date de Prescription :" ,font=('time new rooman',10), bg="white")
labelname.place(x=250, y=190 )

# Entrez la date de prescription de la personne
entrydateprescription= DateEntry(fenetre, bg="#D9D9D9", date_pattern="YYYY-MM-DD")
entrydateprescription.place(x=400, y= 190,width=180)

# Information Medecin

labelname = Label(fenetre, text=" Information Medecin Traitant" ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=630, y=95 )

'''labelname = Label(fenetre, text=" Nom et Prenom :" ,font=('time new rooman',12), bg="white")
labelname.place(x=630, y=130 )

# Entrez le nom du Medecin
entryname_medecin= Entry(fenetre, bg="#D9D9D9")
entryname_medecin.place(x=759, y=130, width=180)'''

# ID Medecin
a =les_docteurs()
liste = a[0]
liste1 = liste[1]
labelname = Label(fenetre, text=" Nom medecin :",font=('time new rooman',12), bg="white")
labelname.place(x=630, y=160 )

# Entrez l'ID du Medecin
entryid_medecin= ttk.Combobox(fenetre,values=liste1)
entryid_medecin.place(x=759, y=160, width=180)

# Prochain RDV
labelname= Label(fenetre, text="Prochain RDV :",font=('time new rooman',12), bg="white")
labelname.place(x=630, y=190 )

# Entrez Prochain RDV
entrydate_rdv= DateEntry(fenetre, bg="#D9D9D9", date_pattern="YYYY-MM-DD")
entrydate_rdv.place(x=759, y=195, width=180)
# Prescription liste


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
btnrechercher= customtkinter.CTkButton(master=fenetre,text="Rechercher",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#DC8014",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=rechercher)
btnrechercher.place(x=850, y=270)

#Boutton Imprimer
btnrechercher= customtkinter.CTkButton(master=fenetre,text="Imprimer",text_font=("Arial",14),text_color="white",bg_color="#FFFFFF",fg_color="#DC8014",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10)
btnrechercher.place(x=850, y=320)
'''#Liste des ordonnance
labelliste = Label(fenetre,text="La liste des Ordonnances",font=("Sans Serif bold",15),
                   background="#7DA0D6",foreground="#000000")
labelliste.place(x=200,y=450,width=880,height=23)'''

# Titre Ordonnance
labelname = Label(fenetre, text=" Prescription:" ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=260, y=320 )

#  Zone de saisie Texte
text = Text(fenetre,font=("times new roman",13) ,height= 11,bg="#D9D9D9")
text.place(x=210, y=350, width=260)

#Liste des ordonnance
labelname = Label(fenetre, text=" Liste des Ordonnance" ,font=('time new rooman bold',13), background="#7DA0D6")
labelname.place(x=630, y=320 )
#FRAME
dash = Frame(fenetre,background="#4062DD")
dash.place(x=0,y=90,width=200,height=480)

#Treeview de la liste des ordonnance
tree= ttk.Treeview(fenetre, columns = (1,2,3,4,5,6), height =8, show = "headings")
style = ttk.Style(fenetre)
style.theme_use("clam")
style.configure("Treeview.Heading", background="#D9D9D9", foreground="black")
tree.place(x=490, y=349)
tree.heading(1, text= "ID_ordonnance")
tree.heading(2, text= "Nom_Patient")
tree.heading(3, text= "Nom_Medecin")
tree.heading(4, text= "Date")
tree.heading(5, text= "Prescription")
tree.heading(6, text= "Prochain RDV")
tree.column(1, width= 50)
tree.column(2, width= 100)
tree.column(3, width= 100)
tree.column(4, width= 100)
tree.column(5, width= 90)
tree.column(6, width= 90)
# Bare de défilement du tree vew
verscrlbar = ttk.Scrollbar(fenetre,
                           orient="vertical",
                           command=tree.yview)
verscrlbar.place(x=1025,y=370,height=160)

#BOUTONS
btnAccueil=customtkinter.CTkButton(master=dash,text="Accueil",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Accueil)
btnAccueil.place(x=10,y=60,width=180)
btnPersonnel=customtkinter.CTkButton(master=dash,text="Personnel",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Personnel)
btnPersonnel.place(x=10,y=110,width=180)
btnDepartement=customtkinter.CTkButton(master=dash,text="Département",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Depatement)
btnDepartement.place(x=10,y=160,width=180)
btnPatient=customtkinter.CTkButton(master=dash,text="Patient",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Patient)
btnPatient.place(x=10,y=210,width=180)
btnOrdonnance=customtkinter.CTkButton(master=dash,text="Ordonnance",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#0052CC",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Ordonnance)
btnOrdonnance.place(x=10,y=260,width=180)
btnComptabilite=customtkinter.CTkButton(master=dash,text="Comptabilité",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Comptabilite)
btnComptabilite.place(x=10,y=310,width=180)
btnRdv=customtkinter.CTkButton(master=dash,text="Rendez-vous",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#1D314F",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=Rdv)
btnRdv.place(x=10,y=360,width=180)

btnDeconnecter=customtkinter.CTkButton(master=dash,text="Deconnecter",text_font=("Arial",14),text_color="white",bg_color="#4062DD",fg_color="#3D88F9",hover=True,hover_color="#0052CC",border_width=0,corner_radius=10,command=deconnection)
btnDeconnecter.place(x=10,y=440,width=180)

with open("doc.pickle","rb") as infile:
    fonction = pickle.load(infile)
if(fonction == 'DOCTEUR'):
    hide_me(btnPersonnel)
    hide_me(btnDepartement)
    hide_me(btnComptabilite)
    hide_me(btnsuprimer)
    btnmodifier.place(x=550)
    btnPatient.place(x=10,y=110)
    btnOrdonnance.place(x=10,y=160)
    btnRdv.place(x=10,y=210)
infile.close()
#logo
image_a=ImageTk.PhotoImage(Image.open('LOO.png'))
l1 = Label(fenetre, image=image_a,width=110,height=110,bg='#4062DD').place(x=40, y=0)
afficher()
fenetre.mainloop()