'''
Max and Second Max
Given an array arr[] of size N of positive integers which may have duplicates.
The task is to find the maximum and second maximum from the array, and both of them should be distinct,
so If no second max exists, then the second max will be -1.

Input Format:
The first line of input contains the number of test cases T.
For each test case, the first line of input contains the size of array N, the next line contains array elements.

Output Format:
For each test case, print the maximum and second maximum from the array.
IF no second max exists, print "-1" for the second max.

User Task:
The task is to complete the function largestAndSecondLargest(),
which should return maximum and second maximum element from the array with
first element as maximum element and second element as second maximum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= T <= 100
1 <= N <= 106
1 <= arr[i] <= 106

Example:
Input:
3
5
1 2 3 4 5
3
2 1 2
2
5 5

Output:
5 4
2 1
5 -1

Explanation:
Testcase 1: From the given array elements, 5 is the largest and 4 is the second largest.
Testcase 2: From the given array elements, 2 is the largest and 1 is the second largest.
Testcase 3: From the given array elements, 5 is the largest and -1 is the second largest.
'''
def largestAndSecondLargest(arr):
    outputList = []
    prevMax = -1
    k=2

    while k!=0:
        max=-1
        for ele in arr:
            if ele != prevMax and ele > max:
                max= ele

        if max != -1:
            arr.remove(max)
        prevMax = max
        outputList.append(max)
        k-=1

    return outputList

def main():

    t = int(input(""))

    while t != 0 :
        n = int(input(""))
        arr = list(map(int, input("").split()))[:n]
        li = largestAndSecondLargest(arr)
        for val in li:
            print(val, end=" ")
        print('')
        t-=1


if __name__ == "__main__":
    main()