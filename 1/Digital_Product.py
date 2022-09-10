import sys

#x = int(sys.argv[1])
x = int(sys.stdin.readlines()[0].lstrip())
temp = 1

while x > 9:
    for idx, char in enumerate(list(str(x))):
        if char != "0":
            temp = temp * int(char)
    x = temp
    temp = 1

print(x)
