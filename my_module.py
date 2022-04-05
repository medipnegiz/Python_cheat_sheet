def fonksiyonum(a):
    while True:
        if a % 2 == 0:
            return print(f'{a} sayinin karesi:', a**2)
            break
        else:
            a = a + 1
fonksiyonum(5)