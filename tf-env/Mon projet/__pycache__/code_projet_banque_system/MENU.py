from Account_operations import creer_compte, voir_comptes, depot, retrait, consulter_sold

def menu():
    while True:
        print("\n Bank Management System")
        choix_menu = ("""
                1. Créer un compte
                2. Voir les Comptes
                3. Faire un dépôt
                4. Faire un retrait
                5. Consulter le solde
                6. Quitter""")
        print(choix_menu)

        choix = input("Faites un choix : ")

        if  choix == '1':
            creer_compte()
        elif choix == '2':
            voir_comptes()
        elif choix == '3':
            depot()
        elif choix == '4':
            retrait()
        elif choix == '5': 
            consulter_sold()
        elif choix == '6':
            print('EXITING SYSTEM...!')
            break
        else:
            print("CHOIX INVALIDE! --> ENTRER UN CHOIX VALIDE!")  