def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return "Imposible realizar el factorial de un número negativo"
    else:
        return num * factorial(num - 1)

def main():
    print(factorial(8))

main()
