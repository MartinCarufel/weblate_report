import requests
from datetime import datetime
import yaml
from language_code import language_code

class Weblate_rest_api:

    def __init__(self):
        # base url
        self.url = url = "https://hosted.weblate.org/api/projects/"
        self.header = headers = {
                            "Authorization": "Token wlu_Gakg1VFGNjjo9rzCctEWM8KAkTLCaKLusAiu"}
        # self.supported_language = ['en', 'bg', 'fr', 'da', 'de', 'el', 'hu', 'it', 'nb_NO', 'pt',
        #                            'es', 'sv', 'ja', 'ko', 'tr', 'pl', 'ru']
        self.supported_language = self.language_selector()
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
            print(f"language: {language["name"]} ({language["code"]}) translated: {language["translated_percent"]}")

    def export_csv(self, json_result, show_app_percent=False):
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d_%H%M%S")
        with open(f"export_csv_{formatted_now}.csv", mode="w", encoding="UTF-8", newline='') as f:
            f.writelines(f"Weblate Report date:, {now.strftime("%Y-%m-%d")}\n\n")
            if show_app_percent == True:
                f.writelines("language,translated (%),Approved words (%)\n")
            else:
                f.writelines("language,translated (%)\n")
            for language in json_result:
                if language["code"] in self.supported_language:
                    if show_app_percent == True:
                        f.writelines(f"{language["name"]},{language["translated_percent"]},{language["approved_words_percent"]}\n")
                    else:
                        f.writelines(
                            f"{language["name"]},{language["translated_percent"]}\n")

    def pretty_text_report(self, json_result):
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d_%H%M%S")
        with open(f"export_txt_{formatted_now}.txt", mode="w", encoding="UTF-8", newline='') as f:
            f.writelines(f"Weblate Report date: {now.strftime("%Y-%m-%d")}\n\n")
            for language in json_result:
                if language["code"] in self.supported_language:
                    f.writelines(f"{language["name"]} ({language["code"]}) - Translation score(%): {language["translated_percent"]}\n")


    def language_selector(self):
        with open(r"C:\Users\u120230\github\weblate_report\supp_lang.yaml", mode='r') as f:
            lang_selector = yaml.safe_load(f)
            # print(lang_selector)

        support_lang = []
        for lang, switch in lang_selector["support language"].items():
            # print(f"L: {lang}  --  {switch}")
            if switch:
                support_lang.append(language_code[lang])

        return support_lang


if __name__ == "__main__":
    api = Weblate_rest_api()
    response = api.get_language_translation()
    response = api.json_response(response)
    api.show_translation_stats(response)
    api.export_csv(response, True)
    api.pretty_text_report(response)


