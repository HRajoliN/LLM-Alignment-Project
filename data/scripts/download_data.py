# Script to download data.
def download_data(url, save_path):
    import requests

    response = requests.get(url)
    with open(save_path, "wb") as file:
        file.write(response.content)
    print(f"Data downloaded to {save_path}")
