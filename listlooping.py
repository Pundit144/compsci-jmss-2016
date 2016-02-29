# write a program to read in 10 values from the keyboard and append them to a list.
my_list = [1,2,3,5,7,8,9,10,11,13,15,17,18,19,20]

print(my_list)

notNum = True
while notNum:
    try:
        c = input ("What number of the list you want")
        c = int(c)
        notNum=False
    except ValueError:
        print("A whole number please, not",c)

c=c-1

try:
    x = my_list[c]
except IndexError:
    print("Out of Range, X is now 15th Number")
    x = my_list[14]

print ("The number you selected was",x)

divideQuestion=True
while divideQuestion:
    try:
        d = input ("What number do you want to divide this by")
        d = int(d)
        answer = x/d
        divideQuestion=False
    except ValueError:
        print("A whole number please, not",d)
        divideQuestion=True
    except ZeroDivisionError:
        print("Sorry you can't divide by Zero")

print (answer)