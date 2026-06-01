# Food Waste Analytics Dashboard

Projet de Data Analytics appliqué à l’analyse du gaspillage alimentaire mondial à partir des données du Programme des Nations Unies pour l’Environnement (UNEP).

---

#  Contexte

Le gaspillage alimentaire représente un enjeu majeur à l'échelle mondiale.

Chaque année, des millions de tonnes de nourriture sont perdues ou gaspillées dans les ménages, les commerces et les services alimentaires. Ces pertes ont des impacts importants sur :

* l'économie ;
* l'environnement ;
* la sécurité alimentaire ;
* la gestion des ressources naturelles.

L'analyse des données permet de mieux comprendre ce phénomène et d'identifier les zones où des actions de réduction du gaspillage sont nécessaires.

---

# Problématique

Comment exploiter les données du gaspillage alimentaire mondial afin de :

* identifier les pays les plus touchés ;
* comparer les régions du monde ;
* analyser les principales sources de gaspillage ;
* produire des indicateurs pertinents ;
* faciliter la prise de décision grâce à la visualisation des données ?

---

# Dataset utilisé

## UNEP Food Waste Index Dataset

Source : Programme des Nations Unies pour l’Environnement (UNEP)

Le dataset contient notamment :

* les estimations du gaspillage alimentaire total par habitant ;
* les estimations du gaspillage des ménages ;
* les estimations du gaspillage dans les commerces ;
* les estimations du gaspillage dans les services alimentaires ;
* les régions géographiques ;
* le niveau de confiance des estimations.

---

#  Objectifs du projet

Les objectifs principaux de ce projet sont :

* collecter et préparer les données ;
* nettoyer et transformer les données ;
* réaliser une analyse exploratoire (EDA) ;
* identifier les principaux indicateurs du gaspillage alimentaire ;
* créer des visualisations pertinentes ;
* développer un dashboard interactif avec Streamlit ;
* produire des analyses exploitables pour la compréhension du phénomène.

---

#  Analyses réalisées

## Nettoyage des données

* Vérification des valeurs manquantes
* Suppression des doublons
* Vérification des types de données
* Contrôle de la qualité des données

## Analyse exploratoire (EDA)

* Top 10 des pays les plus gaspilleurs
* Analyse du gaspillage par région
* Distribution des variables numériques
* Analyse des corrélations
* Comparaison des différentes sources de gaspillage alimentaire

## Analyse métier

* Identification des régions les plus concernées
* Comparaison entre ménages, commerces et services alimentaires
* Mise en évidence des disparités entre pays
* Analyse des indicateurs clés du gaspillage alimentaire

---

#  KPI suivis

Le projet met en avant plusieurs indicateurs clés :

* Gaspillage alimentaire moyen par habitant
* Top pays les plus gaspilleurs
* Répartition du gaspillage par région
* Contribution des ménages au gaspillage total
* Contribution des commerces au gaspillage total
* Contribution des services alimentaires au gaspillage total

---

# Dashboard Streamlit

Le dashboard permet :

* d'explorer les données de manière interactive ;
* de filtrer les résultats par région ;
* de visualiser les principaux indicateurs ;
* de comparer les pays ;
* d'analyser les différentes sources de gaspillage alimentaire.

---

# Technologies utilisées

## Analyse de données

* Python
* Pandas
* NumPy

## Visualisation

* Matplotlib
* Seaborn
* Plotly

## Dashboard

* Streamlit

## Notebooks

* Jupyter Notebook

## Développement

* Git
* GitHub
* VS Code

---

# Structure du projet

```bash
food-waste-ai/
│
├── data/
│   ├── raw/
│   └── clean/
│
├── notebooks/
│   ├── 01_acquisition_des_donnees.ipynb
│   ├── 02_nettoyage_des_donnees.ipynb
│   ├── 03_visualisation.ipynb
│   └── 04_EDA.ipynb
│
├── app/
│   └── dashboard_streamlit.py
│
├── reports/
│
├── images/
│
├── README.md
│
└── requirements.txt
```

---

# 📋 Résultats principaux

Les analyses réalisées montrent :

* une forte disparité du gaspillage alimentaire entre les pays ;
* des différences importantes entre les régions du monde ;
* une contribution significative du gaspillage domestique au gaspillage total ;
* plusieurs régions nécessitant une attention particulière dans les politiques de réduction du gaspillage.

---

# 🔮 Perspectives

Les prochaines améliorations prévues sont :

* enrichissement du dashboard ;
* ajout de filtres avancés ;
* intégration de nouvelles visualisations interactives ;
* comparaison entre plusieurs sources de données ;
* génération automatique de rapports analytiques.

---

# 🎓 Compétences développées

À travers ce projet, j'ai renforcé mes compétences en :

* Data Cleaning
* Analyse Exploratoire des Données (EDA)
* Data Visualization
* KPI & Reporting
* Dashboarding avec Streamlit
* Manipulation de données avec Pandas
* Analyse de données décisionnelle
* Gestion de projet Data avec Git et GitHub

---

# 👩🏽‍💻 Auteur

**Barakissa Koné**

Étudiante en Master Big Data & Intelligence Artificielle.

Passionnée par la Data Science, l'analyse de données et l'utilisation des technologies numériques pour résoudre des problématiques concrètes à impact social et environnemental.
