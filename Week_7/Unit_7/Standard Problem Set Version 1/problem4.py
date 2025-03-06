'''
Problem 4: Calculating Groot's Growth
Groot grows according to a pattern similar to the Fibonacci sequence. Given n, find the height of Groot after n months using a recursive method.

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

def fibonacci_growth(n):
    pass
Example Usage:

print(fibonacci_growth(5))
print(fibonacci_growth(8))
Example Output:

5
21
'''

# The solutions I have provided provide a "naive" solution and then an optimized solution using memoization
# the naive solution is O(2^n) because we are making 2 recursive calls for each n, and the optimized solution is O(n)
# The space complexity of the naive solution is O(n) because we are making n recursive calls and the optimized solution is O(1)
# because we are storing the values in a dictionary and not creating a new list each time

# def fibonacci_growth(n):
#     if n <= 0:
#         return 0
#     if n == 1: 
#         return 1
    
#     return fibonacci_growth(n - 1) + fibonacci_growth(n - 2)

def fibonacci_growth(n, memo={0:0,1:1}):
    if n in memo:
        return memo[n]
    
    return fibonacci_growth(n - 1, memo) + fibonacci_growth(n - 2, memo)

print(fibonacci_growth(5))
print(fibonacci_growth(8))