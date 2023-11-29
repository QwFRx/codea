# калькулятор, принимающий 2 числа от юзера и принимающий выбор действия

n1 = int(input())
n2 = int(input())
oper = input("Введите знак для выбора действия (+/-/:/*): ")
def summ(n1, n2):
    return n1 + n2
def minus(n1, n2):
    return n1 - n2
def delenie(n1, n2):
    return n1 / n2
def ymnojenie(n1, n2):
    return n1 * n2
def calc(n1, n2, oper):
    if oper == "+":
        print(summ(n1, n2))
    if oper == "-":
        print(minus(n1, n2))
    if oper == ":":
        print(delenie(n1, n2))
    if oper == "*":
        print(ymnojenie(n1, n2))



calc(n1, n2, oper)