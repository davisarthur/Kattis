'''
Davis Arthur
5/12/2021
WFF'n Proof
'''

def process(s):
    ops1 = []
    ops2 = []
    logical_vars = []
    for i in range(len(s)):
        if s[i] == 'N':
            ops1.append(s[i])
        elif s[i] == 'K' or s[i] == 'A' or s[i] == 'C' or s[i] == 'E':
            ops2.append(s[i])
        elif s[i] == 'p' or s[i] == 'q' or s[i] == 'r' or s[i] == 's' or s[i] == 't':
            logical_vars.append(s[i])
    return ops1, ops2, logical_vars

'''
Create the largest WFF'n Proof string using the characters in s
'''
def construct(ops1, ops2, logical_vars):

    if len(logical_vars) == 0:
        print("no WFF possible")
        return
    
    # add all N's to first logical variable
    Nstr = ""
    for _ in range(len(ops1)):
        Nstr += "N"
    logical_vars[0] = Nstr + logical_vars[0]

    # determine the maximum number of two operand operators to be used
    numops = min(len(logical_vars) - 1, len(ops2))
    if numops == 0:
        print(logical_vars[0])
        return
    
    output = ""
    for i in range(numops):
        output += ops2[i]
        output += logical_vars[i]
    output += logical_vars[numops]
    print(output)

input_string = input()
while input_string != "0":
    ops1, ops2, logical_vars = process(input_string)
    construct(ops1, ops2, logical_vars)
    input_string = input()
