import unittest
from src.translation_stat import Translation_stat

class Test_translation_stat(unittest.TestCase):

    def setUp(self):
        self.stat = Translation_stat()

    def test_add_stat(self):
        expected_result = {"en": [56, 45], "fr": [98, 0]}

        self.stat.add_lang_stat("en", 56)
        self.stat.add_lang_stat("en", 45)
        self.stat.add_lang_stat("fr", 98)
        self.stat.add_lang_stat("fr", 0)

        for lang in ["en", "fr"]:
            for value in self.stat.get_lang_stat(lang):
                self.assertIn(value, expected_result[lang])


