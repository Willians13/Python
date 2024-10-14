def fatorial(num, show = False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show == True:
        for a in range(num,1,-1):
            print(f'{a} X ',end='')
        print(f'1 = ', end='')
    print(f)

fatorial(4, True)
fatorial(4)