import requests
from datetime import datetime

class Weblate_rest_api:

    def __init__(self):
        # base url
        self.url = url = "https://hosted.weblate.org/api/projects/"
        self.header = headers = {
                            "Authorization": "Token wlu_Gakg1VFGNjjo9rzCctEWM8KAkTLCaKLusAiu"}
        # self.response = None

    def get_language_translation(self):
        return requests.get(self.url+"io/languages/", headers=self.header)

    def json_response(self, response):
        # Check response status and return result in json
        if response.status_code == 200:
            print("OK")
        else:
            print(f"Error: {response.status_code} - {response.text}")

        return response.json()

    def show_translation_stats(self, json_result):
        for language in json_result:
            print(f"language: {language["name"]} translated: {language["translated_percent"]}")

    def export_csv(self, json_result):
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d_%H%M%S")
        with open(f"export_{formatted_now}.csv", mode="w", encoding="UTF-8", newline='') as f:
            f.writelines(f"Weblate Report date:, {now.strftime("%Y-%m-%d")}\n\n")
            f.writelines("language,translated\n")
            for language in json_result:
                f.writelines(f"{language["name"]},{language["translated_percent"]}\n")


if __name__ == "__main__":
    api = Weblate_rest_api()
    response = api.get_language_translation()
    response = api.json_response(response)
    api.show_translation_stats(response)
    api.export_csv(response)


