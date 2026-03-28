# RAG Chatbot – Recommandation d’événements culturels

## Objectif du projet

Ce projet vise à développer un assistant intelligent capable de répondre aux questions des utilisateurs concernant des événements culturels à venir.

Le système repose sur une architecture RAG combinant :
- une recherche sémantique via un index vectoriel (FAISS)
- un modèle de génération de texte (Mistral)
- une orchestration via LangChain

Les données utilisées proviennent de l’API OpenAgenda.

---


## Structure du projet

rag-events-chatbot/

├── app/
├── data/
│   ├── collect_events.py
│   ├── vector_store.py
│
├── scripts/
│   ├── build_vector_db.py
│
├── notebooks/
├── tests/
│   ├── test_collect_events.py
│   ├── test_faiss.py
│
├── rag/
│   ├── chatbot.py
│   ├── prompt.py
│   ├── evaluate.py
│
├── faiss_index/        
├── main.py
├── requirements.txt
├── test_imports.py
├── README.md
├── .gitignore

---

## Installation complète (reproductible)

Cloner le dépôt :
git clone https://github.com/sjbl69/RAG-EVENTS-CHATBOT.git
cd RAG-EVENTS-CHATBOT

Créer un environnement virtuel :
python -m venv env

Activer l’environnement :
Windows :
env\Scripts\activate

Mac / Linux :
source env/bin/activate

Installer les dépendances :
pip install --upgrade pip
pip install -r requirements.txt

---

## Configuration

Créer un fichier .env à la racine du projet :

MISTRAL_API_KEY=your_api_key_here

Ne jamais versionner ce fichier.

---

## Vérification de l’environnement

python test_imports.py

Résultat attendu :
FAISS OK
LangChain OK
Mistral OK
Sentence-Transformers OK
FastAPI OK

---

## IMPORTANT — Index FAISS

Le dossier faiss_index/ n’est pas versionné.

Il doit être reconstruit avant d’utiliser le chatbot.

---

## Workflow complet

1. Collecte des événements :
python data/collect_events.py

2. Nettoyage des données :
python data/clean_events.py

3. Construction de l’index vectoriel (FAISS) :
python scripts/build_vector_db.py

→ crée le dossier faiss_index/

4. Lancement du chatbot :
python main.py

---

## Fonctionnement

1. L’utilisateur pose une question
2. FAISS récupère les événements pertinents
3. Les résultats sont injectés dans un prompt
4. Mistral génère une réponse naturelle et contextualisée

---

## Exemple

Question :
Quels événements à Paris ?

Réponse :
Recommandations d’événements avec date et lieu

---

## Technologies utilisées

Python 3.12
LangChain
FAISS (faiss-cpu)
Mistral AI
Sentence Transformers
FastAPI
Uvicorn

---

## Auteur

Projet réalisé dans le cadre d’une formation en Data Science et Intelligence Artificielle.
