def generate_phrases(sentence):
    '''
    Generate every sub-phrase of a sentence.

    Take every possible ordered subset of words from the sentence. For example
    >>> list(generate_phrases("The quick brown fox"))
    [
        "The",
        "The quick",
        "The quick brown",
        "The quick brown fox",
        "quick",
        "quick brown",
        "quick brown fox",
        "brown",
        "brown fox",
        "fox"
    ]

    Yields
    -------
    str
        The next phrase from the sentence
    '''
    phrase_frontier = []
    # For each word, fist yield the word
    # Then append it to each phrase in the "phrase frontier" and yield a phrase
    for word in sentence.split():
        yield word
        for ix, _ in enumerate(phrase_frontier):
            phrase_frontier[ix] += " " + word
            yield phrase_frontier[ix]
        phrase_frontier.append(word)
