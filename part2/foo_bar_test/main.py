# Вам дана обычная функция foo, перепишите ее на лямбду функцию.



foo = lambda x: (i ** 2 for i in range(x))

if __name__ == "__main__":
    print([x for x in foo(6)])
