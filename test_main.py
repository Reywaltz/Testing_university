from main import sentence_transform, undo_transform

def test_func_1():
    sentence = "Сложное предложение – это предложение, состоящее из двух и более простых Георгий"
    transformed = sentence_transform(sentence)
    assert sentence == undo_transform(transformed)
