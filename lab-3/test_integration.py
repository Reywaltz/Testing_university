from internal.additions import additions

def test_integration():
    test_str = 'Привет, \t мир!'
    test_input = additions.prepare_input(test_str)
    res = additions.sentence_transform(test_input)
    assert res == ['тприве', 'рми']
