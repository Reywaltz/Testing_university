import re

def prepare_input(s: str) -> str:
    words = s.strip().split()
    tmp = " ".join(words)
    pattern = re.compile(",+")
    z = re.sub(pattern=pattern, repl="", string=tmp)
    return "". join(z)


def sentence_transform(s: str) -> str:
    words = s.split(" ")
    res_lst = []
    for word in words:
        if len(word) != 1:
            tmp = word[-1] + word[0:-1].lower()
            res_lst.append(remove_leters(tmp))
        else:
            res_lst.append(remove_leters(word))
    return res_lst


def remove_leters(sentence: str) -> str:
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