"""
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least ten tests. Have at least five tests evaluate to True and
another five tests evaluate to False.
"""
if __name__ == '__main__':
    word1 = "bar"
    word2 = "foo"
    word3 = "wiz"
    print("Simple strings comparisons. True. False. True.")
    print(word1 == "bar", word1 == word2, word2 == 'foo')
    word4 = word1
    print("Copy, same reference. True, False.")
    print(word4 == word1, word1 != word4)