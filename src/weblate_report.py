from wlc import Weblate
from translation_stat import Translation_stat

api_url = "https://hosted.weblate.org/api/"
access_token = "wlu_Gakg1VFGNjjo9rzCctEWM8KAkTLCaKLusAiu"
project_name = "IO"
project_slug = 'io'
app = "weblate/io"


lang_stat = Translation_stat()

translation_stat = {}

# Create the Weblate API client
weblate = Weblate(url=api_url, key=access_token)

# List components for the project
components = weblate.list_components(f'projects/{project_slug}/components/')

for component in components:
    component_name = component['name']
    component_slug = component['slug']   # This is the correct part for URL
    print(f"Component: {component_name}")

    # Build the component path
    component_path = f"{project_slug}/{component_slug}"
    print(component_path)

    # List translations for the component
    # try:
    #     translations = weblate.list_translations(f'components/{component_path}/translations/')
    #     for translation in translations:
    #         lang_stat.add_lang_stat(translation['language_code'], translation['translated_percent'])
    #         print(f"  Language: {translation['language_code']}")
    #         print(f"    Translated: {translation['translated_percent']:.2f}%")
    #         print(f"    Fuzzy: {translation['fuzzy_percent']:.2f}%")
    #         print(f"    Failing Checks: {translation['failing_checks']}")
    #         print()
    # except Exception as e:
    #     print(f"⚠️ Could not fetch translations for component {component_name}: {e}")

print(lang_stat.lang_stat)