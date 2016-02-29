# copy the code from sum1.py into this file, THEN:
# change your program so it keeps reading numbers until it gets a -1, then prints the sum of all numbers read

i = 0
string = ""

while i<90000:
    num = input ("please enter a number")
    if num == "-1":
        i = 90001
    else:
        string += num
        i = i+1
        print ("here are your current numbers",string)

print ("I don't know to get addition of string numbers")