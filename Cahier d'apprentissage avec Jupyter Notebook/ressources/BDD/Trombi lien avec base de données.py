from fileinput import FileInput
import mysql.connector
from tkinter import *
from PIL import *

bdd = mysql.connector.connect(user='Loic',password='trombinoscope', host='localhost', port='8081', database='trombinoscope')
cursor = bdd.cursor()
#quiery = "SELECT nom,prenom,photo,id_personne,id_genre,id_statut FROM personnes NATURAL JOIN genre NATURAL JOIN statut WHERE personnes.id_genre=genre.id_genre AND personnes.id_statut=statut.id_statut"

requete = "SELECT Qualification, genre, nom, prenom, photo FROM personnes NATURAL JOIN statut \
    NATURAL JOIN genre WHERE personnes.id_genre = genre.id_genre AND \
    personnes.id_statut = statut.id_statut ;"
cursor.execute(requete)

for enregistrement in cursor:
    print("\n")
    print(enregistrement[2])
    print(enregistrement[3])
    print(enregistrement[0])
    print(enregistrement[1])






