# read number of customers and each customers roll
num = int(input())
rolls = input().split()

# convert each roll indicater to an integer
for k in range(num):
    rolls[k] = int(rolls[k])

# count frequency of each dice roll
count = [0] * 6
# keeps the index of the last participant to roll a given number
indexes = [-1] * 6


i = 0
for roll in rolls:
    i = i + 1
    count[roll - 1] = count[roll - 1] + 1
    indexes[roll - 1] = i

# save the highest value roll to only get one roll
save = -1
for j in range(6):
    if count[j] == 1:
        save = j

# print the index of the person with the highest unique roll
if save != -1:
    print(indexes[save])
# if no rolls are unique, print "none"
else:
    print("none")
