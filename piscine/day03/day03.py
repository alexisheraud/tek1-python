def my_putchar(c):
    print(c, end="")

def my_print_alpha():
    i= ord('a')
    while i <= ord('z'):
        print(chr(i))
        i += 1

def my_print_revalpha():
    i= ord('z')
    while i >= ord('a'):
        print(chr(i))
        i -= 1

def my_print_digits():
    i= ord('0')
    while i <= ord('9'):
        print(chr(i))
        i += 1

def my_isneg(n):
    if (n < 0):
        print('N')
    else:
        print('P')

def my_put_nbr(nb):
    if nb < 0:
        my_putchar('-')
        nb = -nb
    if nb >= 10:
        my_put_nbr(nb // 10)
    my_putchar(chr(nb % 10 + ord('0')))