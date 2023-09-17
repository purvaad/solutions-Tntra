#Problem 2:  Determine whether a given string is Palindrome

string = "anna"

rev_string = reversed(string)
if list(string) == list(rev_string):
    print("true")
else:
    print("false")


string2 = "India"

rev_string2 = reversed(string2)
if list(string2) == list(rev_string2):
    print("true")
else:
    print("false")
