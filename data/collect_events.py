import requests
from typing import List, Dict


def fetch_events(limit: int = 100) -> List[Dict]:
    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/evenements-publics-openagenda/records"

    params = {
        "limit": limit
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        raise Exception(f"Erreur API : {response.status_code}")

    data = response.json()
    return data.get("results", [])


def clean_events(events: List[Dict]) -> List[Dict]:
    clean_data = []

    for event in events:
        try:
            title = event.get("title_fr") or event.get("title")
            description = event.get("description_fr") or event.get("description")
            city = event.get("location_city") or "Non précisée"
            date = event.get("firstdate_begin") or "Date inconnue"

            if not title or not description:
                continue

            text = f"""
Titre : {title}
Description : {description}
Ville : {city}
Date : {date}
"""

            clean_data.append({
                "text": text.strip(),
                "metadata": {
                    "title": title,
                    "city": city,
                    "date": date
                }
            })

        except Exception:
            continue

    return clean_data


def pipeline():
    events = fetch_events()

    print(f"DEBUG : {len(events)} événements bruts récupérés")

    clean_data = clean_events(events)

    return clean_data


if __name__ == "__main__":
    data = pipeline()

    print(f"\n{len(data)} événements propres\n")

    if data:
        print("Exemple :\n")
        print(data[0])