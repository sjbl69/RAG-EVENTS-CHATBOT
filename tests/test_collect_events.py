import pytest
from data.collect_events import fetch_events, clean_events


#  Fixture 

@pytest.fixture
def events():
    return fetch_events()


@pytest.fixture
def cleaned_events(events):
    return clean_events(events)


#  Test récupération API

def test_fetch_events_returns_list(events):
    assert isinstance(events, list)
    assert len(events) > 0


#  Test structure brute

def test_fetch_events_has_expected_keys(events):
    sample = events[0]

    assert "title_fr" in sample or "title" in sample
    assert "description_fr" in sample or "description" in sample


#  Test nettoyage

def test_clean_events_returns_list(cleaned_events):
    assert isinstance(cleaned_events, list)
    assert len(cleaned_events) > 0


#  Test structure RAG

def test_clean_events_structure(cleaned_events):
    sample = cleaned_events[0]

    assert "text" in sample
    assert "metadata" in sample


#  Test contenu metadata

def test_metadata_content(cleaned_events):
    sample = cleaned_events[0]["metadata"]

    assert "title" in sample
    assert "city" in sample
    assert "date" in sample


#  Test qualité du texte

def test_text_not_empty(cleaned_events):
    assert cleaned_events[0]["text"] != ""