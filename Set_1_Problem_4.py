def bigram(sentence):
    ngram_dictionary = {}
    for c3, c2, c1 in zip(sentence,  '*' + sentence, '*' + '*' + sentence):
        if (c1, c2, c3) in ngram_dictionary:
            ngram_dictionary[(c1, c2, c3)] = ngram_dictionary[(c1, c2, c3)] + 1
        else:
            ngram_dictionary[(c1, c2, c3)] = 1
    print(ngram_dictionary)



bigram("foo bar baz baf")


