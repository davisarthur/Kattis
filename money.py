'''
Davis Arthur
5/12/2020
Money Matters - Kattis
'''

firstline = [int(i) for i in input().split()]
original = firstline[0]
remaining = firstline[1]
owed = []
for i in range(original):
    owed.append(int(input()))

partition = []
for i in range(remaining):
    friends = [int(i) for i in input().split()]

    if len(partition) == 0:
        partition.append(set(friends))
        continue

    membership = []
    for friend in friends:
        for j in range(len(partition)):
            if friend in partition[j] and j not in membership:
                membership.append(j)

    if len(membership) == 0:
        partition.append(set(friends))
        continue

    else:
        sorted(membership, reverse = True)
        first = membership[-1]
        partition[first] = partition[first] | {friends[0], friends[1]}
        for i in range(len(membership) - 1):
            partition[first] = partition[first] | partition[membership[i]]
            partition.pop(membership[i])

possible = True
for group in partition:
    total = 0
    for person in group:
        total += owed[person]
    if total != 0:
        possible = False
        break

if possible:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
