array1 = [*range(1, 10000001)]
array2 = [*range(10, 100000010, 10)]

# Выполняем умножение элементов массивов
def multiply_vectors(array_1, array_2):
    assert len(array_1) == len(array_2)
    return [array_1[i] * array_2[i] for i in range(len(array_1))]

%%time
result_python = multiply_vectors(array1, array2)