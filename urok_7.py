# 6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца,
# т.е. функцию двух аргументов. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.



def print_operation_table(operation, rows=6, columns=6):
    print('   ', end=' ')
    for i in range(1, columns + 1):
        print(str(i).rjust(4), end=' ')
        continue
    print()

    print('_'*23)
        

    for i in range(1, columns + 1):
        print(i, '|', end=' ')
        for j in range(1, rows + 1):
            print(str(operation(i, j)).rjust(4), end=' ')
        print()
print_operation_table(lambda x,y: x**y, 4,4)








# Задача про Винни пуха
# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

# list = ["пара-ра-рам рам-пам-папам па-ра-па-дам"]

# def bear(string: str):
#     for idx in range(0, list + 1):
#         if 


def bear(poem):
    phrase = poem.lower().split()
    f = lambda el: sum(1 for letter in el if letter in 'аоэуяюеёиы')
    tmp = f(phrase[0])
    if all([f(el) == tmp for el in phrase]):
        return True
    return False


print(bear('пара-ра-рам рам-пам-папам па-ра-па-дам'))
print(bear('пара-ра-рам рам-пум-пупам па-ре-по-дам'))
print(bear('пара-ра-рам рам-пуум-пупам па-ре-по-дам'))
print(bear('Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па'))
print(bear('Пам-парам-пурум Пум-пурум-карам'))



























