import phrases

def test_basic_functionality():
    '''It should contain the set of values without duplication'''
    sentence = "Hello cruel world"
    expected = set([
        "Hello", "Hello cruel", "Hello cruel world",
        "cruel", "cruel world",
        "world"
    ])

    assert expected == set(phrases.generate_phrases(sentence))
