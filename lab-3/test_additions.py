from internal.additions import additions
import pytest

def test_empty_input():
    test_input = ''
    assert additions.prepare_input(test_input) == []

def test_prepare_input():
    test_input = 'Тестовая    \t\nстрока!'
    assert additions.prepare_input(test_input) == ['Тестовая', 'строка']


@pytest.mark.dependency()
def test_remove_repeated():
    test_words = 'aaaaaaaaa'.lower()
    assert additions.remove_repeated(test_words) == 'a'


@pytest.mark.dependency(depends=["test_remove_repeated"])
def test_sentence_transform():
    test_sentence = ['сложное', 'предложение', 'совокупность']
    test_result = ['есложн', 'епрдложни', 'ьсовкупнт']
    assert additions.sentence_transform(test_sentence) == test_result
