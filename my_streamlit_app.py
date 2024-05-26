#code py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Charger les données
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voitures = pd.read_csv(link)

#Filtre par région
selected_region = st.radio("Sélectionner une région :", df_voitures['continent'].unique())

# Filtrer les données en fonction de la région sélectionnée
df_filtered = df_voitures[df_voitures['continent'] == selected_region]

# Identification des colonnes non numériques
colonnes_non_numeriques = df_filtered.select_dtypes(include=['object']).columns


df_voitures_numerique = df_filtered.drop(columns=colonnes_non_numeriques)

# Conversion les colonnes restantes en numérique
df_voitures_numerique = df_voitures_numerique.apply(pd.to_numeric, errors='coerce')

# Supprission des lignes avec des valeurs NaN
df_voitures_nettoyee = df_voitures_numerique.dropna()

# Vérifier les dimensions des données nettoyées
if df_voitures_nettoyee.empty:
    st.warning("La DataFrame nettoyée est vide. Veuillez vérifier vos données.")
else:
    # Calcul de la matrice de corrélation
    correlation_matrix = df_voitures_nettoyee.corr()

    
    st.write("Matrice de Corrélation :")
    st.write(correlation_matrix)

    
    for column in df_voitures_nettoyee.columns:
        plt.figure(figsize=(8, 4))
        sns.histplot(df_voitures_nettoyee[column], kde=True)
        plt.title(f'Distribution de {column}')
        plt.xlabel(column)
        plt.ylabel('Fréquence')
        st.pyplot()

