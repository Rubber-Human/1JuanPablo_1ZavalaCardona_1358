def suma_lista(list):
    if len(list) == 0:
        return 0
    else:
        return list.pop() + suma_lista(list)


def main():
    lst = [1,89,3,25]
    print(suma_lista(lst))

main()
