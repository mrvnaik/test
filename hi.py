import sys


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return b/a


def main(args):
    a = int(args[2])
    b = int(args[3])
    if(args[1] == 'add'):
        res = add(a, b)
        print(f'{a}+{b}={res}')
    if(args[1] == 'sub'):
        res = sub(a, b)
        print(f'{a}-{b}={res}')
    if(args[1] == 'mul'):
        res = mul(a, b)
        print(f'{a}*{b}={res}')
    if(args[1] == 'div'):
        res = div(a, b)
        print(f'{b}/{a}={res}')


if __name__ == "__main__":
    main(sys.argv)
