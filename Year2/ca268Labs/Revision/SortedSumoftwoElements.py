def sum_to_k(list, number): #this is the list and the number that two numbers from the list has to equal too.
    
    i = 0         #we start off first number on the list
    b = len(list) - 1   #and the second number will start off last number on the list
    while i < len(list) - 1:  #this is too iterate through the numbers on the list
        if i == b:  #two numbers cannot be the same
            return False
        elif list[i] + list[b] == number:  #if the two numbers from the list are equal to the number given in the function then return True
            return True
        elif list[i] + list[b] < number:   #if the two numbers from the list added together are less than the number given in the function then the first number should go up one
            i += 1
        elif list[i] + list[b] > number:   #if the two numbers from the list added together are more than the number given in the function then the last number should go down one
            b -= 1
    return False