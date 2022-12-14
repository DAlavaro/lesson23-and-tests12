# У вас есть список улиц streets. 
# Нужно написать функцию get_tuples, 
# которая вернет список пар (<название улицы>, <индекс в исходном массиве>), 
# индекс должен начинаться с единицы. 
# В качестве аргумента функция принимает список улиц - список 
# строк, в результате должна вывести список кортежей. 


streets = ['ленина', 'советская', 'краснооктябрьская', 'первомайская']


def enumirate(input_arr):
    n = 1
    for elem in input_arr:
        yield elem, n
        n += 1


def get_tuples(input_arr):
    return list(enumirate(input_arr))


if __name__ == "__main__":
    print(get_tuples(streets))
