def clean_text(text):
    import re
    return re.sub(r"[^a-zA-Z0-9\s]", "", text).strip().lower()
