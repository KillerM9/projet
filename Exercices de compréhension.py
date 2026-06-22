from math import *
# On considère la liste 
l = [9, 10, 11, 20.5, 0, 12.0, -5, -8.3e1]

def rec_moy(l): # fonc rec_moy
    print("la moyenne est :", (sum(l)/len(l)).__round__(2)) #Afficher la moyenne de la liste
def rec_variance(l): # fonc rec_variance
    global t, var
    t=[i**2 for i in l] # compréhension de liste qui contiendra les carrés des nombres de la prémière liste
    var = sum(t)-(sum(l)/len(l))**2
    print("La variance est :", var.__round__(2)) # Afficher la variance de la liste 
def rec_ecart_type(l):
    t =[i**2 for i in l]
    var = sum(t)-(sum(l)/len(l))**2
    ecart_type= sqrt(var)
    print("L'ecart_type est :", ecart_type.__round__(2))

rec_ecart_type(l)
rec_variance(l)
rec_moy(l)
print('-'*100)
# Exercice 2
# Ecrire une fonction calcul_base10 d'argument n, renvoyant une liste l contenant les restes des divisions euclidiennes successives. La fonctionn vérifiera que n, est un entier avec assert.
n = 1234
def calcul_base10(n):
    q = n/10
    r = n%10
    s = q/10  
    print('le quotient de cette division est :', q)
    print('le reste de cette division est :', r)
    print(f"lorsqu'on divise {q} par 10 :", s)
calcul_base10(n)    
# Ecrire le programme principal demandant à l'utilisateur de saisir un entier n strictement positif et renvoyant la décomposition en base 10 de l'entier n .
"""n_1= int(input("saisi une valeur :"))
def dec_10(n_1):
    assert type(n_1) == int
    L = []
    while n_1> 0:
        q = n_1//10
        r = n_1%10
        L.append(r)
        n_1=q
    L.reverse()
    return L
print('la decomposition en base 10 :', dec_10(n_1))"""
# Ecrire une fonction somcube, d'argument n, renvoyant la somme des cubes des chiffres du nombre entier n. On pourra utiliser la fonction calcul_base10
"""def somcube(n_1):
    som = 0
    l= dec_10(n_1)
    for i in range(len(l)):
        som = som + l[i]**3
    return som
print(f'la somme des cubes des chiffres de {n_1} est :',somcube(n_1)) """
# Ecrire une fonction permettant de trouver tous les nombres entiers strictement inférieur à 1000 et égaux à la somme des cubes des leurs chiffres
"""def nombre_positif():
    L = []
    for i in range(1000):
        if i == somcube(i):
            L.append(i)
    return L
print('la liste des entiers < 1000 et égaux à la somme des cubes des chiffres :', nombre_positif())"""
# Ecrire une fonction somcube2 qui converti l'entier n en une chaine de caractère permettant ainsi la récupération de ses chiffres sous forme de caractère.
# Cette nouvelle fonction renvoie la chaine de caractères ainsi que la somme des cubes des chiffres de l'entier n. On pourra utiliser la fonction 'str' et manipuler les chaines de caractères. 
"""n = int(input('Donner un nombre positif :'))
def somcube2(n):
    som = 0
    ch = str(n)
    M = []
    for let in ch:
        M.append(let)
        som = som + (int(let))**3
    return M, som
print(somcube2(n))"""
#EXO 2
def f():
    global b
    print('d =', d)
    print('Premier print dans la fonction f : b = ', b) 
    a = 3 
    c = 5
    b = b + c 
    print('Deuxième print dans la fonction f : b = ', b)
    print('Troisième print dans la fonction f : a = ', a)
    return None
a = 2 
b = 2
d = 3
print("Print avant l'appel de la fonction f : a= ", a)
print("Print avant l'appel de la fonction f : b= ", b)
f()
print("Print après l'appel de la fonction f : a= ", a)
print("Print après l'appel de la fonction f : b= ", b) 
print('-'*100)
i = 3
j = i
print('Avant modification de i : i, j = ', i, j)
i = 5 
print('Après modification de i : i; j = ', i, j)
print('-'*100)
l1 = [1, 3, 5, 7]
l2 = l1
print('Avant modification de l2 : l1, l2 = ', l1, l2)
l2 [3] = 2
l2[3]=print('Après modification de l2 : l1, l2 = ', l1, l2)
print('-'*100)
l3 = [1, 3, 5, 7]
import copy
l4 = copy.copy(l3)
print('Avant modification de l4 : l3, l4 = ', l3, l4)
l4[3] = 2
print('Après modification de l4 : l3, l4 = ', l3, l4)
print('-'*100)
l1 = [1, 2, [3, 4], 5]
l2 = l1
l3 = copy.copy(l1)
l4 = copy.deepcopy(l1)
l1[0] = 12
l1[2][0]= 30
print('l1 = ', l1)
print('l2 = ', l2)
print('l3 = ', l3)
print('l4 = ', l4)