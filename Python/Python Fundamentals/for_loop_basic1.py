for i in range(151): #prints all integers from 0-150
    print(i)

for i in range(5 , 1001, 5): #prints all the multiples of 5 from 5 to 1,000
    print(i)

for i in range(0, 101): #prints integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0 #add odd integers from 0 to 500,000, and print the final sum.
for i in range(500000): 
    if i % 2 != 0:
        sum = sum + i
print(sum)

for i in range(2018, 0, -4): #prints positive numbers starting at 2018, counting down by fours.
    print(i)

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2 
highNum = 73
mult = 7
for i in range(lowNum, highNum):
    if i % mult == 0:
        print(i)