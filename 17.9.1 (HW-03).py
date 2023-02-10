num = input('Введите числа через пробел: ')
any_num = int(input('Введите любое число: '))

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in num:
    print("\nНеобходимо ввести числа через ПРОБЕЛ")
    num = input('Введите числа через пробел: ')
if not is_int(num):
    print('\nНеобходимо ввести целые числа\n')
    print("error")
else:
    num = num.split()

list_num = [int(item) for item in num]

def sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = sort(L[:middle])
        right = sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_num = sort(list_num)

def binary(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary(array, element, left, middle - 1)
        else:
            return binary(array, element, middle + 1, right)
    except IndexError:
        return 'Необходимо ввести число МЕНЬШЕ'
print(f'Упорядоченный писок: {list_num}')

if not binary(list_num, any_num, 0, len(list_num)):
    rI = min(list_num, key=lambda x: (abs(x - any_num), x))
    ind = list_num.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < any_num:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, номер позиции: {ind}
Ближайший больший элемент: {list_num[max_ind]} номер позиции: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, номер позиции: {list_num.index(rI)}
В списке нет меньшего элемента''')
    elif rI > any_num:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, номер позиции: {list_num.index(rI)}
Ближайший меньший элемент: {list_num[min_ind]} номер позиции: {min_ind}''')
    elif list_num.index(rI) == 0:
        print(f'Номер позиции введенного элемента: {list_num.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary(list_num, any_num, 0, len(list_num))}')