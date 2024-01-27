# def deco(func):
#     def inner():
#         print("running inner() ")
#         func()

#     return inner


# @deco
# def target():
#     print("running target()")


# target()

####################################################


registry = []


def register(func):
    print("running register (%s)" % func)
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print("running f2()")


@register
def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry -->", registry)
    f1()
    f2()
    f3()


if __name__ == "main":
    main()