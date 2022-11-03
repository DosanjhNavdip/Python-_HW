def swap_list(input):
    middleindex = int((len(input)-1)/2)
    lastindex = len(input)-1
    input[middleindex],input[lastindex] = input[lastindex],input[middleindex]
    return input
