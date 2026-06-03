# Find maximum in an Array
# Given a list of N integers, representing height of mountains. Find the height of the tallest mountain.

# Input:
# First line will contain T, number of testcases. Then the testcases follow.
# The first line in each testcase contains one integer, N.
# The following line contains N space separated integers: the height of each mountains.

# DIFFICULTY: BASIC

t = int(input()) # number of testcases

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    h = float('-inf')
    for i in range(n):
        if(a[i] > h):
            h = a[i]
    print(h)