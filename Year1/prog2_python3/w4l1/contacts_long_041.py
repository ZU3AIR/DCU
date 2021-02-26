import sys

def main():
    contact_list = {}
    names = []
    number = []
    email = []
    arg1 = sys.argv[1]
    with open(arg1) as file_1:
        file_1 = file_1.read().split()
    for char in file_1:
        if char.isalpha():
            names.append(char)
        elif "@" in char:
            email.append(char)
        else:
            number.append(char)
    i = 0
    while i < len(names):
        contact_list[names[i]] = (number[i], email[i])
        i += 1

    file_2 = sys.stdin.read().strip().split()
    for n in file_2:
        if n not in contact_list:
           print("Name: {}".format(n))
            print("No such contact")
        else:
            print("Name: {}".format(n))
            print("Phone: {}".format(contact_list[n][0]))
            print("Email: {}".format(contact_list[n][1]))

if __name__ == '__main__':
    main()
