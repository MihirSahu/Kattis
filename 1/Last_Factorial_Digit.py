import sys


def factorial(x):

    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))

num_cases = int(sys.stdin.readline().rstrip())

for i in range(num_cases):
    x = int(sys.stdin.readline().rstrip())
    if x >= 5:
        print(0)
    else:
        print(str(factorial(x))[-1])
