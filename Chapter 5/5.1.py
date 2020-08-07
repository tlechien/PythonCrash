if __name__ == '__main__':
    word1 = "bar"
    word2 = "foo"
    word3 = "wiz"
    print("Simple strings comparisons. True. False. True.")
    print(word1 == "bar", word1 == word2, word2 == 'foo')
    word4 = word1
    print("Copy, same reference. True, False.")
    print(word4 == word1, word1 != word4)