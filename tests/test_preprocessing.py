from src.preprocessing.cleaning import DataCleaning

def test_clean_text():
    # Testing basic cleaning: punctuation removal and lowercasing
    assert DataCleaning.clean_text("Hello!!!") == "hello"
    assert DataCleaning.clean_text("Python   is    GREAT!!!") == "python is great"
    assert DataCleaning.clean_text("12345!!") == "12345"
    assert DataCleaning.clean_text("   Mixed CASE with @#$ Special!   ") == "mixed case with special"
