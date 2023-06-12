def multiply_strings(s1, s2):
    # Reverse the strings
    s1 = s1[::-1]
    s2 = s2[::-1]

    # Initialize the result list with 0's
    result = [0] * (len(s1) + len(s2))

    # Perform multiplication digit by digit
    for i in range(len(s1)):
        for j in range(len(s2)):
            # Convert the digits to integers
            digit1 = int(s1[i])
            digit2 = int(s2[j])

            # Multiply the digits and add to the current position
            product = digit1 * digit2 + result[i + j]

            # Update the result and carry
            result[i + j] = product % 10
            result[i + j + 1] += product // 10

    # Remove leading zeros from the result
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Reverse the result and convert to string
    result = ''.join(str(digit) for digit in result[::-1])

    return result

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the two strings
    s1, s2 = input().split()

    # Multiply the strings
    product = multiply_strings(s1, s2)

    # Print the product
    print(product)
