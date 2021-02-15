def get_odd_list():
    n = input()
    oddlist = []#       add input and create a list to store odds
    while int(n) != -1:#    stops if -1 is encounterd
    	if int(n) % 2 != 0:
    		oddlist.append(int(n))
    	n = input()
    return(oddlist)