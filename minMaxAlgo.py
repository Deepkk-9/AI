count = int(input("Enter the number of values : "))

def is_power_of_2(count):
    return count > 2 and (count & count -1) == 0

countCheck = is_power_of_2(count)

def minMaxCal(count):
    lis = [int(input()) for i in range(count)]
    print("===================================\n{0}".format(lis), end="\n\n")
    newList = []

    c=0
    while(len(lis) > 1):
        for i in range(0, len(lis), 2):
            newSubList = lis[i:i+2]
            newList.append(newSubList)

        print(newList, end="\n\n")
        if c%2 == 0:
            lis = [max(i) for i in newList]
            print(lis, "--> Maximization\n")
        else:
            lis = [min(i) for i in newList]
            print(lis, "--> Minimization\n")

        c = c+1 
        newList = []
        newSubList = []
    
    print(lis, "--> Final Answer")

if (countCheck == True):
    minMaxCal(count)
else:
    print("Enter valid value and try again")