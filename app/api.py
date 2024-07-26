import requests

API_URL = "https://the-one-api.dev/v2/movie"

def fetch_movies(movie_name, api_key):
    if not api_key:
        raise Exception("API_KEY não configurada")

    url = f"{API_URL}?name={movie_name}"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Erro na API externa: {response.status_code}, {response.text}")

    return response.json()

