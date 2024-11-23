from src.preprocessing.cleaning import clean_text

def test_clean_text():
    assert clean_text("Hello!!!") == "hello"
