with open('loh.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            # print(word)
            for letter in word.split():
                print(letter)