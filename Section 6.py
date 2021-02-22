#Section 6 of Python.org
#Anmol Mrig


def defletter(a):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    vowels1 = []
    consonants = []
    for i in range(0, len(a)):
        if a[i] in vowels:
            vowels1.append(a[i])
        else:
            consonants.append(a[i])
    print("The Number of Vowels are", len(vowels1))
    print("The Number of Consonants are", len(consonants))


a = "hello"
defletter(a)

def reverse_string(e):
    print(e[::-1])
e = "Welcome"
reverse_string(e)

from collections import deque
reversedletters = deque()
reversedletters1 = deque()
def reverse():
    from collections import deque
    string = []
    string1 = ("")
    l = input("What is your word?")
    for letter in l:
        reversedletters.append(letter)
    for i in reversedletters:
        reversedletters1.appendleft(i)
    for x in reversedletters1:
        string.append(x)
    print(string1.join(reversedletters1))
reverse()
def account():
    money1 = []
    money = 0
    for i in range(0, 43):
        money = 19500 + money
        money = 1.07 * money
        money = round(money, 2)
        money1.append(money)
    print(money1)
account()

