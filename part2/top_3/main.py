# Вам нужно написать функцию top3, 
# которая на вход принимает строку и 
# возвращает 3 наиболее повторяющихся элемента из входной строки. 


def generator(input_str):
    dict_s = {}
    for i in input_str:
        if i in dict_s:
            dict_s[i] += 1
        else:
            dict_s[i] = 1
    yield dict_s



def top3(input_str):
    dict_1 = list(generator(input_str))[0]
    sorted_d = sorted(dict_1.items(), key=lambda x: x[1],reverse=True)[0:3]
    return [i[0] for i in sorted_d]









if __name__ == "__main__":
    print(top3('11111111222222223333333344444444555555'))
