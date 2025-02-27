import json
import requests


class Actividad_1:
    def __init__(self):
        self.ruta_static = "src/pad/static/"

    def leer_api(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Error {response.status_code} al acceder a la API"}

    def escribir_json(self, data, filename="output.json"):  # Aquí estaba el error
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

actividad = Actividad_1()

tender_id = 12345  
url = f"https://tenders.guru/api/es/tenders/{tender_id}"

datos_json = actividad.leer_api(url)

print(actividad.ruta_static)
print(json.dumps(datos_json, indent=4))

# Guardar los datos en un archivo JSON
actividad.escribir_json(datos_json)

