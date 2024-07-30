def replace(text: str):
    chars = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
    for c in chars:
        text = text.replace(c, "")
    return text


class WordsFinder:
    def __init__(self, *files):
        self.__files = files

    def get_all_words(self):
        all_words  = {}
        for f in self.__files:
            words = []
            with open(f, "r", encoding="utf-8") as file:
                for line in file:
                    line = replace(line.lower())
                    for w in line.split(" "):
                        #if not words.__contains__(w):
                        words.append(w)
            all_words [f] = words
        return all_words

    def find(self, text: str):
        found = {}
        all_words = self.get_all_words()
        for k, v in all_words.items():
            for i in enumerate(v):
                if text.lower() == i[1]:
                    found[k] = i[0] + 1
                    break
        return found

    def count(self, text: str):
        c = {}
        all_words = self.get_all_words()
        for k, v in all_words.items():
            con = 0
            for i in enumerate(v):
                if text.lower() == i[1]:
                    con += 1
            if con > 0:
                c[k] = con
        return c

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего