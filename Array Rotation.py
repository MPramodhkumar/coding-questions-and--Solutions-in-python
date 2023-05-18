def right_rotate(arr, k):
    n = len(arr)
    if k > n:
        k = k % n
    arr = arr[-k:] + arr[:-k]
    return arr


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    rotated_array = right_rotate(A, K)
    for num in rotated_array:
        print(num, end=" ")
    print()

    
    
    #2
def reverse_Left_Right_Alg(arr, i, j):
while i < j:
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    i += 1
    j -= 1


def printA(arr, n):
    for i in range(n):
        print(arr[i], end=" ")


def main():
    t = int(input())
    while t > 0:
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        # reverseRightAlg(arr, n - k, n - 1)
        # reverseRightAlg(arr, 0, n - k - 1)
        # reverseRightAlg(arr, 0, n - 1)
        reverse_Left_Right_Alg(arr, n - k, n - 1)
        reverse_Left_Right_Alg(arr, 0, n - k - 1)
        reverse_Left_Right_Alg(arr, 0, n - 1)
        # printArr(arr, n)
        printA(arr, n)
        t = t - 1


if __name__ == "__main__":
    main()
