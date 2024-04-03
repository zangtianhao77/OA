def check_brackets(s):
    stack = []
    output = list(s)
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                output[i] = '?'
    
    for idx in stack:
        output[idx] = 'x'
    
    for k in range(len(output)):
        if output[k] != '?' and output[k] != 'x':
            output[k] = ' '

    return ''.join(output)

##test

test_cases = [
    "bge)))))))))",
    "((IIII))))))",
    "()()()()(uuu",
    "))))UUUU((()",
]

for test in test_cases:
    result = check_brackets(test)
    print(test)
    print(result)