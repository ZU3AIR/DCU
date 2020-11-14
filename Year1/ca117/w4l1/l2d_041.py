import sys

def l2d(file):
    dic = {}
    animal = []
    number = []
    file = file.read().strip().split()
    for char in file:
        if char.isalpha():
            animal.append(char)
        else:
            number.append(char)
    i = 0
    while i < len(animal):
        dic[animal[i]] = number[i]
        i += 1
    return dic
