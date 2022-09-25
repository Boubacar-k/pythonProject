from subprocess import call
from tkinter import ttk
from tkinter import *
from cProfile import label
from tkinter import messagebox

import lb as lb
import mysql.connector
import PySimpleGUI as sg
from  mysql.connector import MySQLConnection,Error

#INSERER
def Inserer():
    id = int(txtId.get())
    nom = txtNom.get()
    num =txtNum.get()

    if (id =="" or nom =="" or num==""):
        messagebox.showinfo("Echec","Aucun champ ne doit etre vide")

    else:

        sql = "INSERT INTO tb_Personne(id,nom,numero) VALUES (%s,%s,%s) "
        valeur = (id, nom, num)

        try:
            maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Personne")
            mConnect = maBase.cursor()
            mConnect.execute(sql,valeur)
            maBase.commit()
            dernier = mConnect.lastrowid
            messagebox.showinfo("Information","insertion effectuer")
            txtId.delete(0,END)
            txtNom.delete(0,END)
            txtNum.delete(0,END)
            txtId.focus_set()
            call(["python","principal.py"])

        except Exception as e:
            print(e)

            maBase.rollback()
            maBase.close()

#MODIFIER
def Modifier():
    id = txtId.get()
    nom = txtNom.get()
    num =txtNum.get()

    based = mysql.connector.connect(host="localhost", user="root", password="", database="Personne")
    myConnect = based.cursor()

    try:
        sql = "UPDATE tb_Personne SET nom=%s,numero=%s WHERE id=%s "
        valeur = (nom,num,id)
        myConnect.execute(sql,valeur)
        based.commit()
        dernier = myConnect.lastrowid
        messagebox.showinfo("Information","Modification effectuer")
        txtId.delete(0, END)
        txtNom.delete(0, END)
        txtNum.delete(0, END)
        txtId.focus_set()

    except Exception as e:
        print(e)

        based.rollback()
        based.close()

#SUPPRIMER
def Supprimer():
    id = txtId.get()
    nom = txtNom.get()
    num = txtNum.get()

    based = mysql.connector.connect(host="localhost", user="root", password="", database="Personne")
    myConnect = based.cursor()

    try:
        sql = "DELETE FROM tb_Personne WHERE id=%s"
        valeur = (id,)
        myConnect.execute(sql,valeur)
        based.commit()
        dernier = myConnect.lastrowid
        messagebox.showinfo("Information","suppression effectuer")
        call(["python","principal.py"])
        txtId.delete(0, END)
        txtNom.delete(0, END)
        txtNum.delete(0, END)
        txtId.focus_set()

    except Exception as e:
        print(e)

        based.rollback()
        based.close()
#AFFICHER
def Afficher():
    id = txtId.get()
    nom = txtNom.get()
    num = txtNum.get()
    maBase = mysql.connector.connect(host="localhost", user="root", password="", database="Personne")
    mConnect = maBase.cursor()
    sql = "SELECT * FROM tb_Personne Where id=%s"
    valeur = (id,)
    mConnect.execute(sql,valeur)

    maBase.close()

def OnDoubleClick(event):
    item = table.selection()[0]
    data = event.widget.get(item)
    txtId.insert(0,data[0])
    txtNom.insert(0, data[1])
    txtNum.insert(0, data[2])
    print("you clicked on", table.item(item, "text"))

#nouvelle fenetre:
fenetre = Tk()

#parametre:
fenetre.geometry("1080x600+100+20")
fenetre.title("CRUD avec Tkiter et Mysql")
fenetre.resizable(False,False)
fenetre.configure(background="#808080")

#titre
labelTitre = Label(fenetre,borderwidth=3,relief=SUNKEN,text="CRUD",font=("Sans Serif",25),
                   background="#0000FF",foreground="#000000")
labelTitre.place(x=0,y=0,width=1080,height=50)

#ID
lblId =Label(fenetre,text="Entrer ID",font=("Arial",14),
                   bg="#808080",foreground="#FFFFFF")
lblId.place(x=6,y=80,width=150)
txtId = Entry(fenetre,bd=4,font=("Arial",12))
txtId.place(x=200,y=80,width=180)

#Nom
lblNom =Label(fenetre,text="Entrer Nom",font=("Arial",14),
                   bg="#808080",foreground="#FFFFFF")
lblNom.place(x=16,y=140,width=150)
txtNom = Entry(fenetre,bd=4,font=("Arial",12))
txtNom.place(x=200,y=140,width=180)

#Numero
lblNum =Label(fenetre,text="Entrer Numéro",font=("Arial",14),
                   bg="#808080",foreground="#FFFFFF")
lblNum.place(x=6,y=200,width=200)
txtNum = Entry(fenetre,bd=4,font=("Arial",12))
txtNum.place(x=200,y=200,width=180)

#Bouton Inserer
btnIns=Button(fenetre,text="Insérer",font=("Arial",14),bg="white",fg="black", command=Inserer)
btnIns.place(x=40,y=280,width=100)

#Bouton Supprimer
btnSuppr=Button(fenetre,text="Supprimer",font=("Arial",14),bg="white",fg="black",command=Supprimer)
btnSuppr.place(x=180,y=280,width=100)

#Bouton Modifier
btnMod=Button(fenetre,text="Modifier",font=("Arial",14),bg="white",fg="black",command=Modifier)
btnMod.place(x=320,y=280,width=100)

#Bouton Afficher
btnAff=Button(fenetre,text="Afficher",font=("Arial",14),bg="white",fg="black",command=Afficher)
btnAff.place(x=460,y=280,width=100)

#Table
table = ttk.Treeview(fenetre,columns=(1,2,3),height=3,show="headings")
table.place(x=600,y=80,width=450,height=300)

#Entete
table.heading(1,text="ID")
table.heading(2,text="NOM")
table.heading(3,text="NUMERO")
#Dimension
table.column(1,width=50)
table.column(2,width=250)
table.column(3,width=150)

#Base de donnees
maBase = mysql.connector.connect(host="localhost",user="root",password="",database="Personne")
mConnect = maBase.cursor()
mConnect.execute("SELECT * FROM tb_Personne")
for ligne in mConnect:
    table.insert('',END,values=ligne)

maBase.close()

table.bind("<Double-1>", OnDoubleClick)


#ouverture de la fenetre:
fenetre.mainloop()