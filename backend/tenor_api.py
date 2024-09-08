import requests

def upload_to_tenor(gif_path: str):
    url = "https://api.tenor.com/v1/gifs"
    api_key = "YOUR_TENOR_API_KEY"
    files = {"file": open(gif_path, "rb")}
    params = {"key": api_key}
    response = requests.post(url, files=files, params=params)
    return response.json()
