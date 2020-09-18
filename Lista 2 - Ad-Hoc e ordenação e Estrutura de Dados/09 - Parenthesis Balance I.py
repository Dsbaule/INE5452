def test():
    expression = input()

    count = 0
    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            if count == 0:
                print('incorrect')
                return
            count -= 1
    
    if count == 0:
        print('correct')
    else:
        print('incorrect')

try:
    while True:
        test()
except EOFError:
    i = 0