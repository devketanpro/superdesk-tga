from unittest.mock import patch

from tga.signal_hooks import generate_doi


@patch("tga.signal_hooks._generate_short_unique_id")
def test_generate_doi_existing_doi(mock_generate_short_unique_id):
    item = {"extra": {"doi": "existing_doi"}}
    updates = {}
    generate_doi(None, item, updates)
    assert item["extra"]["doi"] == "existing_doi"
    assert "extra" not in updates

    item = {"extra": {}}
    updates = {}
    generate_doi(None, item, updates)
    assert item["extra"]["doi"] is not None
    assert item["extra"]["doi"] == updates["extra"]["doi"]


@patch("tga.signal_hooks._generate_short_unique_id")
def test_generate_doi_new_doi(mock_generate_short_unique_id):
    item = {"extra": {}}
    updates = {}
    generate_doi(None, item, updates)
    assert item["extra"]["doi"] is not None
    assert item["extra"]["doi"] == updates["extra"]["doi"]
