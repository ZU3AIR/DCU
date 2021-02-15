def check_brackets(line):
    olist = ["[","{","("] 
    clist = ["]","}",")"] 
    
    slist = [] 
    for i in line: 
        if i in olist: 
            slist.append(i) 
        elif i in clist: 
            pos = clist.index(i) 
            if ((len(slist) > 0) and
                (olist[pos] == slist[len(slist)-1])): 
                slist.pop()
            else: 
                return "False"
    if len(slist) == 0: 
        return "True"
    else: 
        return "False"