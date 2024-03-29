# -*- coding: utf-8 -*-
"""TEST.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YYS7lfq8veBvxbPXq26Piuq3wsMDXi09

**Volet théorique **

**1-Présenter le DNMA en quelques mots:**

Le DNMA, ou Dotation Nationale de Moyens d'Action, est un dispositif de financement alloué par le ministère de l'Éducation nationale en France. Cette dotation vise à soutenir les établissements scolaires dans leur fonctionnement et leurs projets pédagogiques en fournissant des moyens supplémentaires.
*est un dispositif de suivi de fréquentation reposant sur une solution de marquage externe.
*Mesures hebdomadaires par établissement croisées par les appareils (types d'appareils, navigateurs, systèmes d'exploitation).

**2-Définir le terme UAI:**
L'UAI, ou Unité Administrative Immatriculée, est un identifiant unique attribué à chaque établissement scolaire en France. Il s'agit d'un code alphanumérique qui permet d'identifier de manière unique chaque établissement dans les systèmes d'information et les bases de données administratives.
*On appelle ce code unique "UAI" pour "Unité Administrative Immatriculée" : il se compose d'un ensemble de 7 chiffres et d’une lettre.


Les trois premiers chiffres correspondent au numéro du département.


Pour plus de fiabilité, ce code sert d'identifiant unique pour le compte de votre établissement scolaire.

**3-Analyser le jeu de données :
a. Présenter ce qu'il inclut comme données
**UAI**: identifiant unique attribué à chaque établissement scolaire.

**Visites_ordinateurs** le nombre d'utilisateurs uniques qui ont accédé à des ordinateurs sur une période donnée.

**utilisateurs_ordinateurs** la durée totale pendant laquelle des ordinateurs ont été utilisés.
Exprimée en heures, minutes ou secondes

**Visites_smartphone**: Nombre de visites effectuées depuis un smartphone.

**Utilisateurs_smartphone :**Nombre d'utilisateurs distincts ayant utilisé un smartphone.

**Durée_smartphone :** Durée totale d'utilisation des smartphones, exprimée en heures, minutes et secondes.

**Visites_tablette :** Nombre de visites effectuées depuis une tablette.

**Utilisateurs_tablette :** Nombre d'utilisateurs distincts ayant utilisé une tablette.

**Durée_tablette :** Durée totale d'utilisation des tablettes, exprimée en heures, minutes et secondes.

**Visites_autreAppareil :** Nombre de visites effectuées depuis un autre type d'appareil mobile (autre que smartphone ou tablette).

**Utilisateurs_autreAppareil :* *Nombre d'utilisateurs distincts ayant utilisé un autre type d'appareil mobile.

**Durée_autreAppareil :** Durée totale d'utilisation des autres types d'appareils mobiles, exprimée en heures, minutes et secondes.

**Visites_android à Durée_android :** Nombre de visites, utilisateurs et durée d'utilisation pour le système d'exploitation Android.

**Visites_ios à Durée_ios :**  Nombre de visites, utilisateurs et durée d'utilisation pour le système d'exploitation iOS (Apple).

**Visites_windows à Durée_windows :** Nombre de visites, utilisateurs et durée d'utilisation pour le système d'exploitation Windows Mobile.

**Visites_macos à Durée_macos :**Nombre de visites, utilisateurs et durée d'utilisation pour le système d'exploitation macOS (Apple).

**Visites_chromeos à Durée_chromeos :** Nombre de visites, utilisateurs et durée d'utilisation pour le système d'exploitation Chrome OS (Google).

**Visites_linux à Durée_linux :**Nombre de visites, utilisateurs et durée d'utilisation pour le système d'exploitation Linux.

**Visites_autreOS à Durée_autreOS :** Nombre de visites, utilisateurs et durée d'utilisation pour d'autres systèmes d'exploitation mobiles non spécifiés.

**Visites_chromeMobile à Durée_chromeMobile :** Nombre de visites, utilisateurs et durée d'utilisation pour le navigateur Chrome sur mobile.

**Visites_safari à Durée_safari :** Nombre de visites, utilisateurs et durée d'utilisation pour le navigateur Safari sur mobile.

**Visites_firefox à Durée_firefox :** Nombre de visites, utilisateurs et durée d'utilisation pour le navigateur Firefox sur mobile.

**Visites_edge à Durée_edge :**Nombre de visites, utilisateurs et durée d'utilisation pour le navigateur Edge sur mobile.

**Visites_samsungBrowser à Durée_samsungBrowser :** Nombre de visites, utilisateurs et durée d'utilisation pour le navigateur Samsung Internet sur mobile.

**Visites_opera à Durée_opera :**Nombre de visites, utilisateurs et durée d'utilisation pour le navigateur Opera sur mobile.
**Visites_miuiBrowser à Durée_miuiBrowser:**

 Nombre de visites, utilisateurs et durée d'utilisation pour le navigateur MIUI Browser sur mobile.

 **Visites_autreNavigateur à Durée_autreNavigateur :**Nombre de visites, utilisateurs et durée d'utilisation pour d'autres navigateurs mobiles non spécifiés.

**b. Déterminer les 3 catégories de colonnes selon leur nature.**

**Colonnes de mesure**

Exemples :

Visites_smartphone, Utilisateurs_tablette, Durée_chrome, etc.

**Colonnes de dimension :**

Exemples :

Systèmes d'exploitation : Android, iOS, Windows, macOS, etc.
Navigateurs : Chrome, Safari, Firefox, Edge, etc.

**Colonnes de temps ou de date :**

Exemples :
Date de la visite, Durée_ios, etc.

**3-c)Spécifier les métriques et dimensions que vous avez à disposition**

**Métriques :**

**Visites :**

Nombre de visites effectuées depuis différents types d'appareils (smartphones, tablettes, autres) et différents systèmes d'exploitation (Android, iOS, Windows).

**Utilisateurs :**

Nombre d'utilisateurs uniques ayant effectué des visites depuis différents types d'appareils et différents systèmes d'exploitation.

**Durée :**

Durée totale d'utilisation, mesurée en heures, minutes et secondes, pour différents types d'appareils et différents systèmes d'exploitation.

Dimensions:

**Types d'appareils :**

Smartphone, tablette, autre appareil mobile.

**Systèmes d'exploitation (OS) :**

Android, iOS, Windows, macOS, Linux, Chrome OS, etc.

**Navigateurs :**

Chrome, Safari, Firefox, Edge, Samsung Internet, Opera, Huawei Browser, MIUI Browser, etc.

**Date :**

Date des visites.

**Volet pratique :
Partie 1 - Dev**

---
"""

import requests
import pandas as pd

# URL de l'API
url = "https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-dnma-par-uai-appareils&rows=10000"

# Faire une requête GET pour récupérer les données
response = requests.get(url)

# Vérifier si la requête a réussi (code de statut 200)
if response.status_code == 200:
    # Extraire les données JSON de la réponse
    data = response.json()

    # Extraire les enregistrements de données
    records = data.get("records", [])

    # Initialiser une liste pour stocker les données
    data_list = []

    # Parcourir les enregistrements et extraire les valeurs
    for record in records:
        fields = record.get("fields", {})
        data_list.append(fields)

    # Créer un dataframe pandas à partir des données
    df = pd.DataFrame(data_list)

    # Afficher les premières lignes du dataframe
    print(df.head())

else:
    print("La requête n'a pas abouti. Code de statut :", response.status_code)

import requests
import pandas as pd

# Fonction pour récupérer les données à partir de l'API et les agréger selon la granularité spécifiée
def agréger_par_granularité(uai, granularité):
    # URL de l'API
    url = "https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-dnma-par-uai-appareils&rows=10000"

    # Faire une requête GET pour récupérer les données
    response = requests.get(url)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Extraire les données JSON de la réponse
        data = response.json()

        # Extraire les enregistrements de données
        records = data.get("records", [])

        # Initialiser une liste pour stocker les données filtrées par UAI
        uai_data = []

        # Parcourir les enregistrements et filtrer les données pour l'UAI spécifié
        for record in records:
            fields = record.get("fields", {})
            if fields.get("uai") == uai:
                uai_data.append(fields)

        # Créer un dataframe pandas à partir des données filtrées
        df = pd.DataFrame(uai_data)

        # Convertir la colonne 'date' en format de date si ce n'est pas déjà fait
        df['debutsemaine'] = pd.to_datetime(df['debutsemaine'])

        # Agréger les données selon la granularité spécifiée
        if granularité == "Année":
            df_agrégé = df.groupby(df['debutsemaine'].dt.year).sum()
        elif granularité == "Mois":
            df_agrégé = df.groupby([df['debutsemaine'].dt.year, df['debutsemaine'].dt.month]).sum()
        elif granularité == "Semaine":
            df_agrégé = df.groupby([df['debutsemaine'].dt.year, df['debutsemaine'].dt.isocalendar().week]).sum()
        else:
            raise ValueError("Granularité non valide. Veuillez choisir parmi 'Année', 'Mois' ou 'Semaine'.")

        return df_agrégé

    else:
        print("La requête n'a pas abouti. Code de statut :", response.status_code)
        return None

# Fonction pour afficher les résultats agrégés dans un tableau
def afficher_tableau(df):
    print(df)

# Fonction principale
def main():
    # Demander à l'utilisateur de saisir l'UAI et la granularité
    uai = input("Entrez l'UAI : ")
    granularité = input("Entrez la granularité (Année/Mois/Semaine) : ")

    # Agréger les données selon la granularité spécifiée
    df_agrégé = agréger_par_granularité(uai, granularité)

    if df_agrégé is not None:
        # Afficher les résultats dans un tableau
        print("Résultats agrégés pour l'UAI", uai, "par", granularité, ":\n")
        afficher_tableau(df_agrégé)

# Appeler la fonction principale
if __name__ == "__main__":
    main()

import requests
import pandas as pd

# Fonction pour récupérer les données à partir de l'API et les agréger selon la granularité spécifiée
def agréger_par_granularité(uai, granularité):
    # URL de l'API
    url = "https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-dnma-par-uai-appareils&rows=10000"

    # Faire une requête GET pour récupérer les données
    response = requests.get(url)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Extraire les données JSON de la réponse
        data = response.json()

        # Extraire les enregistrements de données
        records = data.get("records", [])

        # Initialiser une liste pour stocker les données filtrées par UAI
        uai_data = []

        # Parcourir les enregistrements et filtrer les données pour l'UAI spécifié
        for record in records:
            fields = record.get("fields", {})
            if fields.get("uai") == uai:
                uai_data.append(fields)

        # Créer un dataframe pandas à partir des données filtrées
        df = pd.DataFrame(uai_data)

        # Convertir la colonne 'date' en format de date si ce n'est pas déjà fait
        df['debutsemaine'] = pd.to_datetime(df['debutsemaine'])

        # Agréger les données selon la granularité spécifiée
        if granularité == "Année":
            df_agrégé = df.groupby(df['debutsemaine'].dt.year).sum()
        elif granularité == "Mois":
            df_agrégé = df.groupby([df['debutsemaine'].dt.year, df['debutsemaine'].dt.month]).sum()
        elif granularité == "Semaine":
            df_agrégé = df.groupby([df['debutsemaine'].dt.year, df['debutsemaine'].dt.isocalendar().week]).sum()
        else:
            raise ValueError("Granularité non valide. Veuillez choisir parmi 'Année', 'Mois' ou 'Semaine'.")

        return df_agrégé

    else:
        print("La requête n'a pas abouti. Code de statut :", response.status_code)
        return None

# Fonction pour afficher les résultats agrégés dans un tableau
def afficher_tableau(df):
    print(df)

# Fonction principale
def main():
    # Demander à l'utilisateur de saisir l'UAI et la granularité
    uai = input("Entrez l'UAI : ")
    granularité = input("Entrez la granularité (Année/Mois/Semaine) : ")

    # Agréger les données selon la granularité spécifiée
    df_agrégé = agréger_par_granularité(uai, granularité)

    if df_agrégé is not None:
        # Afficher les résultats dans un tableau
        print("Résultats agrégés pour l'UAI", uai, "par", granularité, ":\n")
        afficher_tableau(df_agrégé)

# Appeler la fonction principale
if __name__ == "__main__":
    main()

"""**2-**"""

import requests

# Fonction pour récupérer les premières lignes des données à partir de l'API
def récupérer_premières_lignes(uai):
    # URL de l'API avec filtre UAI
    url = f"https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-dnma-par-uai-appareils&rows=5&q=uai:{uai}"

    # Faire une requête GET pour récupérer les données
    response = requests.get(url)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Extraire les données JSON de la réponse
        data = response.json()

        # Extraire les enregistrements de données
        records = data.get("records", [])

        # Afficher les premières lignes des données
        for record in records:
            fields = record.get("fields", {})
            print(fields)

    else:
        print("La requête n'a pas abouti. Code de statut :", response.status_code)

# Appeler la fonction pour afficher les premières lignes des données
uai = input("Entrez l'UAI : ")
récupérer_premières_lignes(uai)

import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fonction pour récupérer les données à partir de l'API
def récupérer_données(uai):
    # URL de l'API avec filtre UAI
    url = f"https://data.education.gouv.fr/api/records/1.0/search/?dataset=fr-en-dnma-par-uai-appareils&rows=10000&facet=debutsemaine&refine.uai={uai}"

    # Faire une requête GET pour récupérer les données
    response = requests.get(url)

    # Vérifier si la requête a réussi (code de statut 200)
    if response.status_code == 200:
        # Extraire les données JSON de la réponse
        data = response.json()

        # Extraire les enregistrements de données
        records = data.get("records", [])

        # Initialiser une liste pour stocker les données
        data_list = []

        # Parcourir les enregistrements et extraire les valeurs
        for record in records:
            fields = record.get("fields", {})
            data_list.append(fields)

        # Créer un dataframe pandas à partir des données
        df = pd.DataFrame(data_list)

        # Convertir la colonne 'debutsemaine' en format de date si ce n'est pas déjà fait
        df['debutsemaine'] = pd.to_datetime(df['debutsemaine'])

        return df

    else:
        print("La requête n'a pas abouti. Code de statut :", response.status_code)
        return None

# Fonction pour générer le graphique
def générer_graphique(df, année):
    # Filtrer les données pour l'année spécifiée
    df = df[df['debutsemaine'].dt.year == année]

    # Groupement des données par mois et calcul du nombre total de visites pour chaque appareil
    df_grouped = df.groupby(df['debutsemaine'].dt.month).sum()[['visites_tablette', 'visites_smartphone', 'visites_ordinateur']]

    # Création du graphique
    plt.figure(figsize=(10, 6))
    df_grouped.plot(kind='line', marker='o')
    plt.title(f"Évolution mensuelle du nombre de visites par appareil ({année})")
    plt.xlabel("Mois")
    plt.ylabel("Nombre de visites")
    plt.xticks(range(1, 13), ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])
    plt.grid(True)
    plt.tight_layout()
    plt.legend(title='Appareil', loc='upper left')
    plt.show()

# Fonction principale
def main():
    # Demander à l'utilisateur de saisir l'UAI et l'année
    uai = input("Entrez l'UAI : ")
    année = int(input("Entrez l'année : "))

    # Récupérer les données pour l'UAI spécifié
    df = récupérer_données(uai)

    if df is not None:
        # Générer le graphique
        générer_graphique(df, année)

# Appeler la fonction principale
if __name__ == "__main__":
    main()

"""**3-**

"""

