class WordsFinder: # зададим класс
    def __init__(self, *file_names): # приним. неограни. кол-во и запис. в арг. file_names
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}  # зададим пустой словарь
        # список символов пунктуации для удаления
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:  # переберем все файлы
            with open(file_name, 'r', encoding='utf-8') as file:
                # чтение содерж. файла и перевод в ниж. регистр
                text = file.read().lower()
                # удалим пунктуацию из текста
                for p in punctuation:
                    text = text.replace(p, '')
                # разобьем текст на слова
                words = text.split()
                # сохр. список слов в словарь
                all_words[file_name] = words
        return all_words

    def find(self, word):
        # искомое слово в ниж. регистр
        word = word.lower()
        # получим словаря всех слов
        all_words = self.get_all_words()
        result = {}
        # переберем файлы и списков слов
        for file_name, words in all_words.items():
            if word in words: # сохр. позицию первого вхождения слова
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        # Приведение искомого слова к нижнему регистру
        word = word.lower()
        # получим словарь всех слов
        all_words = self.get_all_words()
        result = {}
        # переберем файлы и списка слов
        for file_name, words in all_words.items():
            result[file_name] = words.count(word) # сохр. количества вхождений слова
        return result

# пример
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

