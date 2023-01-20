import random
number = int(input('Загадайте число:'))
gadalka = 0
while gadalka != number:
    gadalka = random.randint(number-50, number)
    print(gadalka)
    if gadalka == number:
        print('ПОБЕДА!!!')
        