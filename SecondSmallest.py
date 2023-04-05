num1,num2,num3 = map(int,input().split())
if num1 < num2 and num1 < num3:
    smallest = num1
elif num2 < num1 and num2 < num3:
    smallest = num2
else:
    smallest = num3

# Find the second smallest number
if smallest == num1:
    if num2 < num3:
        second_smallest = num2
    else:
        second_smallest = num3
elif smallest == num2:
    if num1 < num3:
        second_smallest = num1
    else:
        second_smallest = num3
else:
    if num1 < num2:
        second_smallest = num1
    else:
        second_smallest = num2

# Print the second smallest number
print(second_smallest)
