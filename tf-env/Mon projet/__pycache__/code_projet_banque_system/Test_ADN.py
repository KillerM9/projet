from DB_test_ADN import connect
import json
from dna_features_viewer import GraphicFeature, GraphicRecord
import matplotlib.pyplot as plt
import getpass
import time
import matplotlib.animation as animation  
    
def info_enregistrer():
    prenom = input("Prenom : ")
    nom = input("Nom : ")
    age = (input("L'âge : "))
    taille = (input("La taille : "))
    couleur_yeux = input("Couleur de yeux : ")
    sequence = input("La séquence nucléotique : ")
    gene_data = {'genes': {}}
    print('Entrer les coordonnées des 10 genes')
    for i in range(1, 11):
        print(f"\nPour le gene{i}: ")
        debut = int(input(f"Debut de gene{i} : "))
        fin = int(input(f"Fin de gene{i} : "))
        gene_data['genes'][f'genes{i}'] = (debut, fin)
        genes_json = json.dumps(gene_data)
    group_blood = input("Le groupe sanguin : ")
    db = connect()
    cur = db.cursor()
    time.sleep(5)
    req = "INSERT INTO Informations(Prenom,Nom,Âge,Taille,Couleur_yeux,Gènes,Séquence_génétique,Groupe_Sanguin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    var=(prenom,nom,age,taille,couleur_yeux,genes_json,sequence,group_blood)
    cur.execute(req,var)
    db.commit()
    print("Information enregistrer avec succès!")
    db.close()

def afficher_db():
    db = connect()
    cur = db.cursor()
    time.sleep(5)
    cur.execute("SELECT * FROM Informations;")
    resultat = cur.fetchall()
    print("\n\t\t\t===CONTENU DE LA BASE DE DONNÉES===\t\t\t\n")
    for i in resultat:
        print(f"ID: {i[0]} \nPrenom: {i[1]}, \nNom: {i[2]}, \nAge: {i[3]}, \nTaille: {i[4]},  \nListe des gènes: {i[5]},  \nSequence nucléotique: {i[6]},  \nGroupe sanguin: {i[7]}, \nCouleur des yeux: {i[8]}")
    cur.close()
    db.close()

def sequence_genetique():
        while True:
            menu="""
                1. Résultats graphics pour deux sujets (X et Y)
                2. Résultat graphic du sujet (X ou Y)
                3. Quitter."""
            print(menu)
            choix = input("Entrer une option : ")
            if choix == '1':           
                print("\n\t\t\tRésultat Graphique du sujet X\t\t\t\n")
                id_x = input("Identifiant du Sujet-X : ")
                db = connect()
                cur = db.cursor()
                cur.execute("SELECT Gènes,Séquence_génétique,Prenom FROM Informations WHERE id_info= %s;", (id_x,))#Selection d'un identifiant dans la base de données 
                resultat_x= cur.fetchone()
                #vérification de l'id
                if resultat_x is None:
                    print("Erreur : Aucun individu trouvé avec l'identifiant X.")
                else:
                    donnees_genes_x = json.loads(resultat_x[0])
                    dictionnaire_coord_x = donnees_genes_x['genes']
                    sequence_gene_x = resultat_x[1]
                    prenom_x = resultat_x[2]
                    features_gene_x= [] #Création de la liste des genes du sujet x
                    for gene_x, coordonnees in dictionnaire_coord_x.items():
                        coordonnees_tuple = tuple(coordonnees)
                        debut = coordonnees_tuple[0]
                        fin = coordonnees_tuple[1]
                        features_gene_x.append(GraphicFeature(start=debut, end=fin, strand=+1, color='#ffcccc', label=gene_x))
                    record = GraphicRecord(sequence=sequence_gene_x, features=features_gene_x)
                    fig, ax = plt.subplots(figsize=(10,3))
                    record.plot_sequence(ax)
                    record.plot(ax=ax)
                    plt.title(f"Carte Génétique - {prenom_x} (Sujet-X)")
                    #Analyse graphique du sujet Y
                    print("\n\t\t\tRésultat Graphique du sujet Y\t\t\t\n")
                    id_y = input("Identifiant du Sujet-Y : ")
                    db = connect()
                    cur = db.cursor()
                    cur.execute("SELECT Gènes,Séquence_génétique,Prenom FROM Informations WHERE id_info= %s;", (id_y,))#Selection d'un identifiant dans la base de données 
                    resultat_x= cur.fetchone()
                    resultat_y= cur.fetchone()
                    #vérification de l'id du sujet y
                    if resultat_y is None:
                        print("Erreur : Aucun individu trouvé avec l'identifiant Y.")
                    else:
                        donnees_genes_y = json.loads(resultat_y[0])
                        dictionnaire_coord_y = donnees_genes_y['genes']
                        sequence_gene_y = resultat_y[1]
                        prenom_y= resultat_y[2]
                        features_gene_y= []#Création de la liste des genes du sujet y
                        for gene_y, coordonnees in dictionnaire_coord_y.items():
                            coordonnees_tuple = tuple(coordonnees)
                            debut = coordonnees_tuple[0]
                            fin = coordonnees_tuple[1]
                            features_gene_y.append(GraphicFeature(start=debut, end=fin, strand=+1, color='#ffcccc', label=gene_y))
                        record = GraphicRecord(sequence=sequence_gene_y, features=features_gene_y)
                        fig, ax = plt.subplots(figsize=(10,3))
                        record.plot_sequence(ax)
                        record.plot(ax=ax)
                        plt.title(f"Carte Génétique - {prenom_y} (Sujet-Y)")
                plt.show()        
            elif choix == '2':
                print("\n\t\t\tRésultat Graphique du sujet \t\t\t\n")
                id_x = input("Identifiant du Sujet : ")
                db = connect()
                cur = db.cursor()
                cur.execute("SELECT Gènes,Séquence_génétique,Prenom, Nom FROM Informations WHERE id_info= %s;", (id_x,))#Selection d'un identifiant dans la base de données 
                resultat= cur.fetchone()
                #vérification de l'id
                if resultat is None:
                    print("Erreur : Cet identifiant n'existe pas.")
                else:
                    donnees_genes = json.loads(resultat[0])
                    dictionnaire_coord = donnees_genes['genes']
                    sequence_gene = resultat[1]
                    prenom = resultat[2]
                    nom = resultat[3]
                    features_gene = [] #Création de la liste des genes du sujet x
                    for gene, coordonnees in dictionnaire_coord.items():
                        coordonnees_tuple = tuple(coordonnees)
                        debut = coordonnees_tuple[0]
                        fin = coordonnees_tuple[1]
                        features_gene.append(GraphicFeature(start=debut, end=fin, strand=+1, color='#ffcccc', label=gene))
                    record = GraphicRecord(sequence=sequence_gene, features=features_gene)
                    fig, ax = plt.subplots(figsize=(10,3))
                    record.plot_sequence(ax)
                    record.plot(ax=ax)
                    plt.title(f"Carte Génétique de- {prenom} {nom}")
                plt.show()
            elif choix == '3': 
                print("EXITING...")
                time.sleep(5)
                break
            else:
                print(":) --> Choix Invalide....")
                
def common_gene():
    db = connect()
    cur = db.cursor()
    individu_x = input("Identifiant X: ")
    cur.execute("SELECT Prenom, Nom, Gènes, Séquence_génétique FROM Informations WHERE id_info= %s ;", (individu_x,))
    result_x = cur.fetchone()
    #Vérification de l'id du sujet x
    if result_x is None:
        print(f"Erreur : L'identifiant {individu_x} n'existe pas dans la base de données")
        return   
    individu_y = input("Identifiant Y: ") 
    cur.execute("SELECT Prenom, Nom, Gènes, Séquence_génétique FROM Informations WHERE id_info= %s ;", (individu_y,))
    result_y = cur.fetchone() 
    #Vérification de l'id du sujet y
    if result_y is None:
        print(f"Erreur : L'identifiant {individu_y} n'existe pas dans la base de données")
        return        
    cur.close()
    db.close()
    #Reccuperation des sequences dans la base de données
    sequence_gene_x = result_x[3]     
    sequence_gene_y = result_y[3]
    #Création de la liste des genes du sujet x
    dictionnaire_coord_x = json.loads(result_x[2])['genes']
    list_genes_x = []    
    for genes, coordonnee in dictionnaire_coord_x.items():
        debut = int(coordonnee[0])
        fin = int(coordonnee[1])
        fragment_adn_x =sequence_gene_x[debut:fin]
        list_genes_x.append(fragment_adn_x)  
    #Création de la liste des genes du sujet y
    dictionnaire_coord_y = json.loads(result_y[2])['genes']
    list_genes_y = []     
    for genes, coordonnee in dictionnaire_coord_y.items():
        debut = int(coordonnee[0])
        fin = int(coordonnee[1])
        fragment_adn_y =sequence_gene_y[debut:fin]
        list_genes_y.append(fragment_adn_y) 
    #Affichage des listes de genes des deux sujets 
    print(f"Séquence X : {list_genes_x}")
    print(f"Séquence Y : {list_genes_y}")
    #Initialisation de la variable nombre_de_genes_en_commun  
    print("\n===Gènes en commun des deux sujets===\n")        
    nombre_de_genes_en_commun=0      
    for fragment_adn_x in list_genes_x:#Boucle sur la liste des genes du sujet x
        if fragment_adn_x in list_genes_y:#Comparaison des genes de la liste des genes du sujer x dans la liste du sujet y
                print(f'Genes en commun trouvé (Séquence): {fragment_adn_x}')#Affichage des genes identiques depuis les deux listes
                nombre_de_genes_en_commun += 1 
    pourcentage = (nombre_de_genes_en_commun/10.0)*100
    print("\n===Pourcentage de gènes en commun===\n")
    print(f"{result_x[0]} {result_x[1]} et {result_y[0]} {result_y[1]} ont {pourcentage}% de genes en commun")#Affichage du pourcentage de genes en commun

def del_data():
    id_info = input("Entrez l'identifiant : ")
    db = connect()
    cur = db.cursor()
    print(f"\nVérification du mot de passe de l'administrateur\n")
    password_admin = getpass.getpass("Confirmer le mot passe admin: ")
    if password_admin == 'admin@hospitalmanagement':
        time.sleep(5)
        cur.execute(""" DELETE FROM Informations WHERE id_info= %s LIMIT 1;""", (id_info,))  
        db.commit()
        print(f"les informations de l'id {id_info} ont été supprimé de la base de données!")
    else:
        print("Mot de passe invalide...!")
    db.close()      
def modication_colonne():
        id_modif = input("Entrez l'identifiant dont vous volez modifier les informations : ")       
        while True: #boucle sur la mis à jour des informations   
            print("\n\t\t\tFAIRE UNE MODIFICATION DE DONNÉES\n")
            colonne_modif = """ 
                                1. Modifier le Prenom
                                2. Modifier le Nom
                                3. Modifier l'Âge
                                4. Modifier la Taille
                                5. Modifier les Gènes
                                6. Modifier la Séquence génétique
                                7. Modifier Groupe Sanguin 
                                8. Modifier la Couleur des yeux
                                9. Quitter la modification."""
            print(colonne_modif)
            choix = input("Entrez une option de modification: ")
            if choix == '1':
                prenom = input("Nouveau Prenom : ")
                db = connect()
                cur = db.cursor()
                time.sleep(5)
                cur.execute("""UPDATE  Informations SET Prenom = %s WHERE id_info=%s""",(prenom,id_modif))#mettre à jour le prenom
                db.commit()
                print(f"Modification éffectué avec succès!")
                cur.close()
                db.close()
            elif choix == '2':
                nom = input("Nouveau Nom : ")
                db = connect()
                cur = db.cursor()
                time.sleep(5)
                cur.execute("""UPDATE  Informations SET Nom = %s WHERE id_info=%s""",(nom,id_modif))#mettre à jour le nom
                db.commit()
                print(f"Modification éffectué avec succès!")
                cur.close()
                db.close()
            elif choix == '3':
                age = input("Nouvel Âge : ")
                db = connect()
                cur = db.cursor() 
                time.sleep(5)               
                cur.execute("""UPDATE  Informations SET Âge = %s WHERE id_info=%s""",(age,id_modif))#mettre à jour l'age
                db.commit()
                print("Modification éffectué avec succès!")
                cur.close()
                db.close()             
            elif choix == '4':
                db = connect()
                cur = db.cursor()
                taille = input("Nouvelle Taille : ")
                time.sleep(5)
                cur.execute("""UPDATE  Informations SET Taille = %s WHERE id_info=%s""",(taille,id_modif))#mettre à jour la taille
                db.commit()
                print("Modification éffectué avec succès!")
                cur.close()
                db.close()
            elif choix == '5':
                gene_data = {'genes': {}}
                print('Entrer les coordonnées des 10 genes')
                for i in range(1, 11):
                    print(f"\nPour le gene{i}: ")
                    debut = int(input(f"Debut de gene{i} : "))
                    fin = int(input(f"Fin de gene{i} : "))
                    gene_data['genes'][f'genes{i}'] = (debut, fin)
                    genes_json = json.dumps(gene_data)
                db = connect()
                cur = db.cursor()
                time.sleep(5)                    
                cur.execute("""UPDATE  Informations SET Gènes = %s WHERE id_info=%s""",(genes_json,id_modif))#mettre à jour les gènes
                db.commit()
                print("Modification éffectué avec succès!")
                cur.close()
                db.close()
            elif choix == '6':
                sequence = input("La nouvelle séquence génétique : ")
                db = connect()
                cur = db.cursor()
                time.sleep(5)                
                cur.execute("""UPDATE  Informations SET Séquence_génétique = %s WHERE id_info=%s""",(sequence,id_modif))#mette à jour le séquence génétique
                db.commit()
                print("Modification éffectué avec succès!")
                cur.close()
                db.close()
            elif choix == '7':
                group_blood = input("Nouveau Groupe Sanguin : ") 
                db = connect()
                cur = db.cursor()
                time.sleep(5) 
                cur.execute("""UPDATE  Informations SET Groupe_Sanguin = %s WHERE id_info=%s""",(group_blood,id_modif))#mettre à jour le groupe sanguin
                db.commit()                
                print("Modification éffectué avec succès!")
                cur.close()
                db.close()
            elif choix == '8':
                couleur_yeux = input("La couleur des yeux : ")
                db = connect()
                cur = db.cursor() 
                time.sleep(5)               
                cur.execute("""UPDATE  Informations SET Couleur_yeux = %s WHERE id_info=%s""",(couleur_yeux,id_modif))#mettre à jour la couleur des yeux
                db.commit()
                print("Modification éffectué avec succès!")
                cur.close()
                db.close()
            elif choix == '9':#sortie de l'option
                time.sleep(5)
                print("Modification terminé...!")
                break
            else: 
                print("CHOIX INVALIDE, RÉESSAYER...!")

