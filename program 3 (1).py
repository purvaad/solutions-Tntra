#Biggest and smallest number in an array using for loop

arr = [1, 2, 3, 4, 5]
min = arr[0]
max = arr[0]

for i in range(len(arr)):
    if arr[i]  < min : min = arr[i]
if arr[i] > max : max = arr[i]

print("Maximum is: ", max)
print("Minimum is: ", min)