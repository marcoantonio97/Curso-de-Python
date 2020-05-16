def maior(* num):
    cont = mai = 0
    for v in num:
        print(f'{v} ', end='')
        if cont == 0:
            mai = v
        else:
            if v > mai:
                mai = v
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')
    print('='*30)


maior(4, 5, 2, 7, 9, 1, 0, 3, 5, 4)
maior(5, 2, 8, 5)
maior(3, 1, 7)
maior(0, 1)
maior(6)
maior()
