from BD_config import connect
import getpass

def creer_compte():
    prenom = input("Votre Prenom: ")
    nom = input("Votre Nom: ")
    mail = input("Entrer un e-mail: ")
    sold = float(input("Entrez votre solde: "))
    password = getpass.getpass("Votre mot de passe: ")
    date = input("Date de création: ")
    bd = connect()
    cur = bd.cursor()
    cur.execute("""INSERT INTO comptes(Prenom, Nom, E_Mail, Password_client, Solde, Creation) VALUES(%s, %s, %s, %s, %s, %s);""", (prenom, nom, mail, password, sold, date))
    bd.commit()
    print("Compte créé avec succès!")
    bd.close()
def voir_comptes():
    bd = connect()
    cur = bd.cursor()
    cur.execute("""SELECT * FROM comptes;""")
    compte = cur.fetchall()
    for i in compte:
        print(f"ID: {i[0]}, Prenom: {i[1]}, Nom: {i[2]}, E-Mail: {i[3]}, Mot de Passe: {i[4]}, Solde: {i[6]}, Date_de_création: {i[5]}")
    cur.close()
    bd.close()
def depot():
    bd = connect()
    id_compte = int(input("Identifiant du compte: "))
    montant = float(input("Montant à déposer(€): "))
    cur = bd.cursor()
    cur.execute("""UPDATE comptes SET Solde = Solde + %s WHERE id = %s;""", (montant, id_compte))
    bd.commit()
    print("Votre solde a été mis à jour avec succès!")
    bd.close()
def retrait():
    bd = connect()
    id_compte = int(input("Identifiant du compte: "))
    montant = float(input("Montant à déposer(€): "))
    cur = bd.cursor()
    cur.execute("""SELECT Solde FROM comptes WHERE id=%s;""", (id_compte,))
    result = cur.fetchone()
    if result and result[0]>=montant:
        cur.execute("""UPDATE comptes SET Solde = Solde - %s WHERE id = %s;""", (montant, id_compte,))
        bd.commit()
        print(f"Retrait de {montant}€ effectué avec succés!")
    else:
        print("Solde insuffisant!")
    bd.close()
def consulter_sold():
    bd = connect()
    id_compte = int(input("Identifiant du compte: "))
    cur = bd.cursor()
    cur.execute("""SELECT Prenom, Nom, Solde FROM comptes WHERE id=%s;""", [id_compte])
    result = cur.fetchone()
    if result:
        prenom, nom, solde = result
        print(f"Propriétaire : {prenom} {nom}, Solde actuel: {solde}€")
    else:
        print("Compte introuvable!")
    cur.close()
    bd.close()

