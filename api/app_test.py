from app import process_query


def test_knows_about_dinosaurs():
    assert process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 \
million years ago"

def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"

def test_process_query_name():
    assert process_query("What is your name?") == "15mahomes"

