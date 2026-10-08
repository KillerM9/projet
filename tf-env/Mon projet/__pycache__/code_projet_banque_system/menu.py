from Test_ADN import *

def menu():
    while True:
        print("\n\t\tHOSPITAL MANAGEMENT SYSTEM\t\t\t\n")
        MENU = ("""
                1. Enregistrer les informations
                2. Afficher les données
                3. Analyse-Graphique 
                4. Gène en commun
                5. Modification des informations 
                6. Supprimer une donnée
                7. Quitter.""")
        print(MENU)
        
        choix_menu = input("Choisissez une option dans le menu: ")

        if choix_menu =='1':
            info_enregistrer()
        elif choix_menu == '2':
            afficher_db()
        elif choix_menu == '3':
            sequence_genetique()
        elif choix_menu == '4':
            common_gene()
        elif choix_menu == '5':
            modication_colonne()
        elif choix_menu == '6':
            del_data()
        elif choix_menu == '7':
            print('EXITING....')
            break
        else:
            print('CHOIX INVALIDE ---> ENTRER UN CHOIX VALIDE!')
