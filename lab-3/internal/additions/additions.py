from typing import List
from string import punctuation


def prepare_input(s: str) -> List[str]:
    """Метод преобразования входной строки

    :param s: Входная строка
    :type s: str
    :return: Отформатированная строка
    :rtype: str
    """
    s = s.replace('\n', ' ').replace('\t', '').replace('\r', '').replace(',', ' ') # noqa
    words = s.strip().split()

    for index, word in enumerate(words):
        words[index] = word.translate(str.maketrans('', '', punctuation))
    return words


def sentence_transform(words: List[str]) -> List[str]:
    """Метод преобразования предложения в слова

    :param words: Отформатированный список слов
    :type words: List[str]
    :return: Преобразованные слова
    :rtype: List[str]
    """
    res_lst = []
    for word in words:
        if word == '':
            continue
        if len(word) != 1:
            tmp = word[-1] + word[0:-1].lower()
            new_word = remove_repeated(tmp)
            if new_word == '':
                continue
            res_lst.append(new_word)
        else:
            res_lst.append(remove_repeated(word))
    return res_lst


def remove_repeated(word: str) -> str:
    """Функция удаления повторяющихся букв

    :param word: Слово
    :type word: str
    :return: Слово без повторяющихся букв
    :rtype: str
    """
    return ''.join(sorted(set(word), key=word.index))
