l, c = [int(x) for x in input().split()]

puzzle = list()
for i in range(l + 1):
    puzzle.append(input().split())

sum_rows = [int(x.pop(-1)) for x in puzzle[:-1]]
sum_columns = [int(x) for x in puzzle.pop(-1)]

variables = set()
for row in puzzle:
    variables.update(row)

values = dict()
while len(values) < len(variables):
    # Horizontal
    for row in range(l):

        unknown = set()
        numUnknown = 0
        curSum = 0

        for variable in puzzle[row]:
            value = values.get(variable, None)
            if value is None:
                unknown.add(variable)
                if len(unknown) > 1:
                    break
                numUnknown += 1
            else:
                curSum += value

        if len(unknown) == 1:            
            values[unknown.pop()] = (sum_rows[row] - curSum)//numUnknown
    
    # Vertical
    for column in range(c):

        unknown = set()
        numUnknown = 0
        curSum = 0

        for row in puzzle:
            variable = row[column]

            value = values.get(variable, None)
            if value is None:
                unknown.add(variable)
                if len(unknown) > 1:
                    break
                numUnknown += 1
            else:
                curSum += value

        if len(unknown) == 1:            
            values[unknown.pop()] = (sum_columns[column] - curSum)//numUnknown

variables = list(variables)
variables.sort()
for variable in variables:
    print(variable + ' ' + str(values[variable]))