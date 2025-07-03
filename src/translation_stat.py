class Translation_stat:

    def __init__(self):
        self.lang_stat = {}
        self.x = 10

    def add_lang_stat(self, lang_code, stat):
        lang_stat = self.lang_stat[lang_code]
        lang_stat.append(stat)

    def get_lang_stat(self, lang_code):
        return self.lang_stat[lang_code]
