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

```
rag-events-chatbot/
│
├── app/
│
├── data/
│   ├── collect_events.py
│   ├── vector_store.py
│
├── scripts/
│   ├── build_vector_db.py
│
├── notebooks/
│
├── tests/
│   ├── test_collect_events.py
│   ├── test_faiss.py
│
├── rag/
│   ├── chatbot.py
│   ├── prompt.py
│   ├── evaluate.py
│
├── faiss_index/        (généré, non versionné)
│
├── main.py
├── requirements.txt
├── test_imports.py
├── README.md
├── .gitignore
```

---

## Installation complète (reproductible)

### 1. Cloner le projet

```bash
git clone https://github.com/sjbl69/RAG-EVENTS-CHATBOT.git
cd RAG-EVENTS-CHATBOT
```

---

### 2. Vérifier Python

```bash
python --version
```

Recommandé : Python 3.10+

---

### 3. Créer un environnement virtuel

```bash
python -m venv env
```

---

### 4. Activer l’environnement

Windows :
```bash
env\Scripts\activate
```

Mac / Linux :
```bash
source env/bin/activate
```

---

### 5. Installer les dépendances

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## Configuration

Créer un fichier `.env` à la racine du projet :

```env
MISTRAL_API_KEY=your_api_key_here
```

Ne jamais versionner ce fichier.

---

## Vérification de l’environnement

```bash
python test_imports.py
```

Résultat attendu :

- FAISS OK  
- LangChain OK  
- Mistral OK  
- Sentence-Transformers OK  
- FastAPI OK  

---

## IMPORTANT — Index FAISS

Le dossier `faiss_index/` n’est pas versionné.

Il doit être reconstruit avant d’utiliser le chatbot.

---

## Workflow complet

### 1. Collecte des événements

```bash
python data/collect_events.py
```

---

### 2. Nettoyage des données

```bash
python data/clean_events.py
```

---

### 3. Construction de l’index FAISS

```bash
python scripts/build_vector_db.py
```

 Cela crée le dossier `faiss_index/`

---

### 4. Lancer le chatbot

```bash
python main.py
```

---

## Fonctionnement

1. L’utilisateur pose une question  
2. FAISS récupère les événements pertinents  
3. Les résultats sont injectés dans un prompt  
4. Mistral génère une réponse naturelle  

---

## Exemple

**Question :**
Quels événements à Paris ?

**Réponse :**
Recommandations d’événements avec date et lieu

---

## Technologies utilisées

- Python  
- LangChain  
- FAISS (faiss-cpu)  
- Mistral AI  
- Sentence Transformers  
- FastAPI  
- Uvicorn  

---

## Auteur

Projet réalisé dans le cadre d’une formation en Data Science et Intelligence Artificielle.
