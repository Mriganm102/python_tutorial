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