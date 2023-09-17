# Program to count occurrences of a given character in a string.


string = input("Enter your string: ")
char = input("Enter the character you want to count from string: ")

count = 0
for i in range(len(string)):
    if(string[i]== char):
        count = count + 1

print("Total count of",char, "in" ,string, ":", count)
