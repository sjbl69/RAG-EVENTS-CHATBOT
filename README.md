#  RAG Chatbot – Recommandation d’événements culturels

##  Objectif du projet

Ce projet vise à développer un assistant intelligent capable de répondre aux questions des utilisateurs concernant des événements culturels à venir.

Le système reposera sur une architecture RAG (Retrieval-Augmented Generation) combinant :
- une recherche sémantique via un index vectoriel (FAISS)
- un modèle de génération de texte (Mistral)
- une orchestration via LangChain

Les données utilisées proviendront de l’API OpenAgenda.

---

## 📁 Structure du projet

Le projet est actuellement organisé comme suit :

```
rag-events-chatbot/

├── app/                # (prévu) API REST avec FastAPI
├── data/               # (prévu) données d’événements
├── scripts/            # (prévu) scripts de traitement (ingestion, nettoyage, indexation)
├── notebooks/          # (prévu) exploration et tests
├── tests/              # (prévu) tests unitaires

├── env/                # environnement virtuel local principal (non versionné)
├── test_env/           # environnement de test pour vérifier la reproductibilité

├── test_imports.py     # script de validation des dépendances
├── requirements.txt    # liste des dépendances du projet
├── README.md           # documentation
├── .gitignore
```

### Remarques importantes

* Les dossiers `app`, `data`, `scripts`, `tests` et `notebooks` sont **présents mais encore vides** à ce stade.
* Ils correspondent à la **structure cible du projet**, qui sera progressivement remplie dans les prochaines étapes (pipeline RAG, API, etc.).
* Les dossiers `env/` et `test_env/` sont des environnements virtuels locaux utilisés uniquement pour le développement et les tests. Ils ne doivent pas être versionnés.
* La reproductibilité de l’environnement a été validée en recréant un environnement vierge (`test_env`) et en exécutant :

  ```
  pip install -r requirements.txt
  ```

  sans erreur de dépendances.

---

##  Installation complète (reproductible)

1. Cloner le dépôt

git clone https://github.com/sjbl69/RAG-EVENTS-CHATBOT.git  
cd RAG-EVENTS-CHATBOT  

---

2. Vérifier la version de Python

python --version  

Version requise : Python 3.8 ou supérieur (recommandé : Python 3.12)

---

3. Créer un environnement virtuel

python -m venv env  

---

4. Activer l’environnement

Windows (PowerShell / CMD) :  
env\Scripts\activate  

Mac / Linux :  
source env/bin/activate  

Vous devez voir (env) apparaître dans le terminal

---

5. Installer les dépendances

pip install --upgrade pip  
pip install -r requirements.txt  

---

##  Configuration

Créer un fichier .env à la racine du projet :

MISTRAL_API_KEY=your_api_key_here  

Ne jamais versionner ce fichier.

---

##  Vérification de l’environnement

Lancer le script :

python test_imports.py  

Ce script vérifie que toutes les dépendances essentielles sont correctement installées.

Code de sortie :
0 → succès  
1 → échec  

Résultat attendu :

FAISS OK  
LangChain OK  
Mistral OK  
Sentence-Transformers OK  
FastAPI OK  

---

##  État actuel du projet

Ce dépôt correspond à la mise en place de l’environnement de développement reproductible.

Les fonctionnalités suivantes ne sont pas encore implémentées :
- récupération des données OpenAgenda  
- construction de l’index FAISS  
- pipeline RAG complet  
- API FastAPI  

---

##  Tests

Les tests unitaires seront ajoutés dans le dossier :

tests/

Ils permettront de valider :
- la récupération des données  
- la vectorisation  
- la génération de réponses  

---

##  Technologies utilisées

- Python 3.12  
- LangChain  
- LangChain Community  
- FAISS (faiss-cpu)  
- Mistral AI  
- Sentence Transformers (HuggingFace)  
- FastAPI  
- Uvicorn  

---

##  Auteur

Projet réalisé dans le cadre d’une formation en Data Science et Intelligence Artificielle.
