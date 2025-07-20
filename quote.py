# ---
# ⚠️ ¡Atención!: Las categorias de la API quotes ahora son premium
#    por esa razon comente los parametros de "category"
#
# Para mas información visita:
# https://api-ninjas.com/api/quotes
# ---

import requests

API_URL = "https://api.api-ninjas.com/v1/quotes"
# QUOTE_CATEGORY = "inspirational"


def generate_quote(api_key):
    # params = {"category": QUOTE_CATEGORY}
    headers = {"X-api-key": api_key}
    response = requests.get(API_URL, headers=headers)  # params es premium
    quote_obj = response.json()[0]
    print(f"Código de estado {response.status_code}")
    print(f"Contenido json {response.json()}")
    if response.status_code == requests.codes.ok:
        return f"{quote_obj['quote']} -- {quote_obj['author']}"
    return "¡Solo hazlo! -- Shia LaBeouf"
