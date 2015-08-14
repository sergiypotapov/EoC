__author__ = 'spotapov'
def count_units(number):
    n=0
    R=0
    bin_num = bin(number)
    print (bin_num)
    for i in bin_num:
        if i == "b":
         print("nothing")
        else:
            i = int(i)
            #print(i)
            if i == 1:
                R = R+1
        n = n +1
    #print(n)
    print("Number of units is", R)
    return(R)
