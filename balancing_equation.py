import re

def get_elements(term):
    return re.findall(r'[A-Z][a-z]*\d*', term)

def balance_equation(equation):
    reactants, products = equation.split('->')
    reactants = reactants.strip().split('+')
    products = products.strip().split('+')

    elements = set()
    coefficients = {}
    for term in reactants + products:
        for element in get_elements(term):
            elements.add(re.findall(r'[A-Z][a-z]*', element)[0])
            coefficients[element] = 0

    coefficient_values = {}
    for element in elements:
        for term in reactants:
            count = term.count(element)
            if count:
                coefficient_values[element] = len(reactants) / count
                break
        else:
            for term in products:
                count = term.count(element)
                if count:
                    coefficient_values[element] = -len(products) / count
                    break

    matrix = []
    for term in reactants:
        row = []
        for element in elements:
            count = term.count(element)
            row.append(count * coefficient_values[element])
        matrix.append(row)

    for term in products:
        row = []
        for element in elements:
            count = term.count(element)
            row.append(count * coefficient_values[element])
        matrix.append(row)

    matrix.append([1] * len(reactants) + [-1] * len(products))
    matrix = [list(x) for x in zip(*matrix)]

    for i in range(len(matrix) - 1):
        if matrix[i][i] == 0:
            for j in range(i + 1, len(matrix)):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else:
                continue
        for j in range(i + 1, len(matrix)):
            if matrix[j][i] == 0:
                continue
            factor = matrix[i][i] / matrix[j][i]
            for k in range(i, len(matrix[0])):
                matrix[j][k] = matrix[i][k] - matrix[j][k] * factor

    for i in range(len(matrix) - 1, 0, -1):
        if matrix[i][i] == 0:
            continue
        factor = 1 / matrix[i][i]
        for j in range(i - 1, -1, -1):
            if matrix[j][i] == 0:
                continue
            temp = matrix[j][i] * factor
            for k in range(len(matrix[0])):
                matrix[j][k] -= temp * matrix[i][k]

    result = []
    for i, element in enumerate(elements):
        result.append(coefficient_values[element])
        result.append(element)
        result.append(' + ' if i < len(elements) - 1 else ' -> ')
    result.append(str(int(abs(matrix[-1][-1]))))
    return ''.join(str(x) for x in result)

while True:
    equation = input("Enter a chemical equation: ")
    balanced_equation = balance_equation(equation)
    print("Balanced Equation: " + balanced_equation)

    choice = input("Do you want to balance another equation? (Y/N) ").strip().lower()
    if choice != 'y':
        break
