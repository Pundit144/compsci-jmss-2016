# write a program that reads in 10 numbers, then prints the sum of those

try:
    a = input ("Please enter your first number")
    b = input ("Please enter your second number")
    c = input ("Please enter your third number")
    d = input ("Please enter your fourth number")
    e = input ("Please enter your fifth number")
    f = input ("Please enter your sixth number")
    g = input ("Please enter your seventh number")
    h = input ("Please enter your eighth number")
    i = input ("Please enter your ninth number")
    j = input ("Please enter your last number")
    a = int (a)
    b = int (b)
    c = int (c)
    d = int (d)
    e = int (e)
    f = int (f)
    g = int (g)
    h = int (h)
    i = int (i)
    j = int (j)
    print (a+b+c+d+e+f+g+h+i+j)
except IndexError:
    print ("Please enter an integer, and now because you dont know what a number is, start again")


