import unittest
from src.weblate_rest_api import Weblate_rest_api
from language_code import language_code
import sys


class Test_weblate_rest_api(unittest.TestCase):

    def test_language_selector(self):
        o = Weblate_rest_api
        print(o.language_selector(self))
