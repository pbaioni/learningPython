from sys import stdout

#printing list elements
c = ["first", "second", "third"]
for item in c:
    print"list item value:", item

#printing within range 0 - 3
for i in range(4):
    print"range value:", i

#building a string to print in one single line
stringChain = "chainOfCharacters"
for char in stringChain:
    if char in "AEIOUYaeiouy": # vocals
        stdout.write(char)
    else: 
        stdout.write('*')
stdout.write('\n') #line feed
stdout.flush()

#while loop
j=5       
while j >= 0:
    print 'loop countdown:', j
    j=j-1
