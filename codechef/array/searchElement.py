# Search an element in an array
# You are given an array A of size N and an element X. 
# Your task is to find whether the array A contains the element X or not.

# DIFFICULTY: BASIC

def solve(N, X, A):
  for i in range(N):
       if(A[i] == X):
           return "YES"
           
  return "NO"

