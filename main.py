# TODO
"""
Ввести предложение, состоящее из слов, разделенных запятой или
пробелами. Вывести слова предложения предварительно преобразовав их
следующим образом:
• перенести последнюю букву в начало слова;
• удалить из слова повторные вхождения каждой буквы.
"""


def sentence_transform(s: str) -> str:
    words = s.split(" ")
    res_lst = []
    for word in words:
        if word[-1] != ',':
            tmp = word[-1] + word[:-1]
            # tmp = remove_repeated(tmp)
            res_lst.append(tmp)
        else:
            tmp = word[-2] + word[:-2:] + ','
            # tmp = remove_repeated(tmp)
            res_lst.append(tmp)
    return (" ".join(res_lst))


def undo_transform(s: str) -> str:
    words = s.split(" ")
    res_lst = []
    for word in words:
        if word[-1] != ',':
            tmp = word[1:] + word[0]
            res_lst.append(tmp)
        else:
            tmp = word[1:-1] + word[0] + ','
            res_lst.append(tmp)
    return (" ".join(res_lst))


def remove_leters(sentence):
    words = sentence.split(" ")
    res_lst = []
    for word in words:
        word = remove_repeated(word)
        res_lst.append(word)
    return " ".join(res_lst)


def remove_repeated(word: str) -> str:
    dct = {}
    for char in word:
        if char in dct:
            dct[char] += 1
        else:
            dct[char] = 1
    for char in dct.keys():
        if dct[char] > 1:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    sentence = "Сложное предложение – это предложение, состоящее из двух и более простых Георгий"

    transformed_sentence = sentence_transform(sentence)

    print(transformed_sentence)
    print(undo_transform(transformed_sentence))
    print(remove_leters(transformed_sentence))
