import mysql.connector as msc 

bdd = msc.connect(user='root',password='root', host='localhost', port='8081', database='base1')
cursor=bdd.cursor()

qui=3

query = "SELECT nom, prenom FROM utilisateurs WHERE id_utilisateur ="+str(qui)+";"
cursor.execute(query)
#toujours fermer ce qui est ouvert
for enregistrement in cursor :
    print(enregistrement [0])
    print(enregistrement [1])

cursor.close()
bdd.close()