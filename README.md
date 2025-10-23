# 📝 Analyse des sentiments

## Description

Ce projet permet d’effectuer une **analyse de sentiments** sur du texte ou des fichiers CSV contenant des commentaires ou avis.  
Il utilise **TextBlob** pour calculer la **polarité** et la **subjectivité**, et fournit une **interprétation simple** : Positive, Negative ou Neutral.

L’application est développée avec **Streamlit**, ce qui permet une **interface interactive** directement dans le navigateur.

---

## Fonctionnalités principales

- 📝 Analyse de texte **en direct** : calcule polarité, subjectivité et sentiment.  
- 📂 Analyse de fichiers Excel : traitement des colonnes `reviewText`.  
- 📊 Visualisation des résultats avec un **diagramme en barres** (positif, neutre, négatif).  
- 💾 Téléchargement des données analysées au format CSV.  
- 🧹 Nettoyage du texte via la librairie `cleantext`.  

---

## Technologies utilisées
-**Python** : Langage principal 
-**TextBlob** : Analyse de sentiment 
-**Pandas** : Manipulation de données 
-**Streamlit** : Interface interactive 
-**cleantext** : Nettoyage du texte 
-**Matplotlib / Seaborn** : Visualisation des données 
