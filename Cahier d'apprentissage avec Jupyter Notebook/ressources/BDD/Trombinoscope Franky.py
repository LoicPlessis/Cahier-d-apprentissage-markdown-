from fileinput import FileInput
from tkinter.constants import COMMAND
import mysql.connector
import tkinter as tk
from tkinter.messagebox import *
from PIL import Image, ImageTk


      

#Connection à la bdd via MySQL
cnx = mysql.connector.connect(user='fratboy', password='J\'adorelepoulet29!',
                              host='127.0.0.1', port= '8081',
                              database='trombinoscope')
cursor = cnx.cursor()
#requête SQL
quiery = "SELECT nom,prenom,photo,id_personne,id_genre,id_statut FROM personnes NATURAL JOIN genre NATURAL JOIN statut WHERE personnes.id_genre=genre.id_genre AND personnes.id_statut=statut.id_statut"
cursor.execute(quiery)

resultat = cursor.fetchall()
cursor.close
cnx.close()

#Définition de la fenêtre
fenetre = tk.Tk() 
fenetre.title("Trombinoscope - ISEN/SIMPLON  - BREST")
fenetre.geometry("700x700")
fenetre.minsize(200,200)
fenetre.maxsize(700,700)
fenetre['bg']="#ff6947" #couleur


#parcours de la bdd (s'éxecute qu'on clique sur le bouton rechercher)
def affiche():
    v= entree.get()
    v=v.lower()
    for rec in result:
        #on vérifie que le nom ou le prénom est dans le tableau
        if (v == rec[1].lower() or v == rec[0].lower()): 
        #on charge l'image et on la convertit pour être utilisable
            i= Image.open(rec[2]+".png")
            photo=ImageTk.PhotoImage(i.resize((200,267)))
            illustration.configure(image=photo)
        #on effectue un test sur l'id_statut pour connaître le statut de la personne
            if rec[5]==1:
                statut='Enseignant'
            if rec[5]==2:
                statut='Chargé de projet'
            if rec[5]==3:
                statut='Apprenant P1'
            if rec[5]==4:
                statut='Apprenant P2'
            #info.configure pour changer l'image affichée, fenetre.mainloop pour rafraîchir la fenêtre
            info.configure(text='Prénom : '+rec[1]+'\n Nom : '+rec[0]+'\n Statut : '+statut)
            fenetre.mainloop()

def getEntry():
    v = entree.get()
    return(v)


i= Image.open('init'+".jpg")
photo=ImageTk.PhotoImage(i.resize((200,267)))
illustration=tk.Label(fenetre,image=photo,padx=0, pady=20)
illustration.pack()
info=tk.Label(fenetre,text="En attente")
info.pack()

p=tk.PanedWindow(fenetre,orient=tk.HORIZONTAL)
value = tk.StringVar() 
value.set("Entrer le prénom")
entree = tk.Entry(fenetre, width=50)
entree.pack()

bouton=tk.Button(fenetre, text="Chercher", command=affiche, padx=20, pady=0,)
# bouton_p=tk.Button(fenetre, text="Précédent", command=prec, padx=20, pady=0,)
# bouton_s=tk.Button(fenetre, text="Suivant", command=suiv, padx=20, pady=0,)
p.add(entree)
p.add(bouton)
p.pack()

def alert():
    showinfo('Auteurs','Maïna LE DEM \n Franky TANGUY')
menubar = tk.Menu(fenetre)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Quitter", command=fenetre.quit)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="A propos", command=alert)
menubar.add_cascade(label="Aide", menu=menu2)

fenetre.config(menu=menubar)


fenetre.mainloop()