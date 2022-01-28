import mysql.connector as msc 

bdd = msc.connect(user='loic',password='trombinoscope', host='localhost', port='8081', database='trombinoscope')
cursor=bdd.cursor()

qui=3

query = "SELECT statut, genre, nom, prenom, photo FROM personnes NATURAL JOIN statuts NATURAL JOIN genres WHERE personnes.id_genre = genres.id_genre AND personnes.id_statut = statut.id_statut"
cursor.execute(query)
#toujours fermer ce qui est ouvert
for enregistrement in cursor :
    print(enregistrement [0])
    print(enregistrement [1])

cursor.close()
bdd.close()