# Davis Arthur
# Kattis — Beat the Spread!
# 4-27-2020

output = ""
num = int(input())
for i in range(num):
    if i != 0:
        output = output + "\n"
    data = input().split()
    s = int(data[0])
    d = int(data[1])
    w = (s + d) / 2
    l = (s - d) / 2
    if w < 0 or l < 0:
        output = output + "impossible"
        continue
    if abs(w - int(w)) > 0.00001 or abs(l - int(l)) > 0.00001:
        output = output + "impossible"
        continue
    output = output + str(int(w)) + " " + str(int(l))

print(output)
