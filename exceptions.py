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

c=c+1

try:
    x = my_list[c]
except IndexError:
    print("Out of Range, X is now 4th Value")
    x = my_list[14]

print ("The number you selected was",x)
