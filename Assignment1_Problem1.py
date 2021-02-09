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

import Assignment1_Problem1