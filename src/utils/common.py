def save_to_file(content, file_path):
    """
    Save content to a file.
    """
    with open(file_path, "w") as file:
        file.write(content)
