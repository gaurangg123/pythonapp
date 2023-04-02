def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print (mean)

def isGreater(a,b):
    if(a>b):
        print("The first number is greater")
    else:
        print("second number is greater or equal")  

a = 9
b = 8
if (a>b):
    print("first number is greater")
else:
    print("second number is greater or equal")

calculateGmean(a,b)
# gmean1 = (a*b)/(a+b)
# print (gmean1) 
# c = 8
# d = 7 
# calculateGmean(c,d)
# gmean2 = (c*d)/(c+d)
# print (gmean2)
