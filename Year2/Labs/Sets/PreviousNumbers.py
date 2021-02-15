print("Enter numbers (-1 to end): ", end="")
values = int(input())
numbers = []
while values != -1:
    numbers.append(values)
    values = int(input())
special = {}
for n in numbers:
    if n not in special:
        special[n] = 1
    else:
        special[n] += 1
past = []
for n in numbers:
    if n not in past:
        past.append(n)
    elif special[n] > 1:
        print((str(n) + " "), end="")
print()