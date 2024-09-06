# Função de alta ordem
def add(x, y):
    return x + y


def apply_operation(operation, x, y):
    return operation(x, y)


result = apply_operation(add, 5, 3)
