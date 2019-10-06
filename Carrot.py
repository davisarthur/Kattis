import sys

line = sys.stdin.read()
if line != None:
    numbers = line.split()
    print(str(numbers[1]))
