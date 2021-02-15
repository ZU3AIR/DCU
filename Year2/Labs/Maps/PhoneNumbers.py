Dict = {}

print("Enter a name and number, or a name and ? to query (!! to exit)")

inp = input()

while inp != "!!":
    n, q = inp.split()

    if n not in Dict and q != "?":
        Dict[n] = q
    
    elif n in Dict and q != "?":
        Dict[n] = q

    elif q == "?" and n in Dict:
        print('{} has number {}'.format(n, Dict[n]))

    else:
        print("Sorry, there is no " + n)
    
    inp = input()

print("Bye")