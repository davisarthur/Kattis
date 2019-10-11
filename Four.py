# Davis Arthur
# 10-10-2019

def convert(operand):
    if operand == 0:
        return " + "
    if operand == 1:
        return " - "
    if operand == 2:
        return " * "
    if operand == 3:
        return " // "

# variables
operandSets = []
answerEqs = []

# generate all operand combinations
for i in range(4):

    for j in range(4):

        for k in range(4):

            operand = [i, j, k]
            operandSets.append(operand)

# generate equations
for set in operandSets:

    equation = "4"

    for operand in set:
        equation = equation + convert(operand) + "4"

    answer = str(eval(equation))

    equation = equation + " = " + str(answer)
    equation = equation.replace("//", "/")

    answerEq = (answer, equation)
    answerEqs.append(answerEq)

# take in input from Kattis
numInput = int(input())
importantInput = []
for i in range(numInput):
    importantInput.append(str(input()))

for num in importantInput:
    output = "no solution"
    for solution in answerEqs:
        if num == solution[0]:
            output = solution[1]
            break
    print(output)
