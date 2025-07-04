class Translation_stat:

    def __init__(self):
        self.lang_stat = {}


    def add_lang_stat(self, lang_code, stat):
        try:
            stat_list = self.lang_stat[lang_code]
            stat_list.append(stat)
            self.lang_stat[lang_code] = stat_list
        except KeyError:
            stat_list = [stat]
            self.lang_stat[lang_code] = stat_list

    def get_lang_stat(self, lang_code):
        return self.lang_stat[lang_code]
