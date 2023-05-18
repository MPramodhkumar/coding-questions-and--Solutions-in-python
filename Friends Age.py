def count_friend_requests(ages):
    total_requests = 0
    age_count = [0] * 121  # Initialize age_count array with zeros

    # Count the frequency of each age
    for age in ages:
        age_count[age] += 1

    # Iterate through each age and check the conditions for friend requests
    for age_A in ages:
        for age_B in range(1, 121):
            if age_B <= 0.5 * age_A + 7:
                continue
            if age_B > 100 and age_A < 100:
                continue
            if age_B > age_A:
                continue

            # Increment the total_requests count if conditions are met
            total_requests += age_count[age_B]

            # If age_A == age_B, decrement the count as A won't send request to themselves
            if age_A == age_B:
                total_requests -= 1

    return total_requests


# Read the input
N = int(input())
ages = list(map(int, input().split()))

# Count the total friend requests and print the result
total_requests = count_friend_requests(ages)
print(total_requests)
