# a: int = 5
# b: str = 'строка'
# c: list = [1,2]
#
# def indent(s: str, width: int) -> str:
#     return ' ' * (max(0, width - len(s))) + s
#
#print(indent('123', 123))

# def return1(s: str = ''):
#     return len(s)
# print(return1('кукушка'))
#
#
# def fun2(a: list, b: list):
#     return len(max(a, b))
# print(fun2((1,2,3,4,5), (0,1,2)))

# def fun3(a: list):
#     return a + a.append()
# print (fun3([1,2,7]))


def fun4(x: list) -> int:
    return sum(x)
print(fun4([1,2,3,4]))