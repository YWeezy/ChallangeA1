leven = 3

while leven > 0:
    vraag_1 = int(input('38 + 42 = '))

    if vraag_1 == 80:
        print('vraag 1/5 complete')
    else:
        leven -= 1
        print(leven)

    if leven == 0:
        print("Game over")
        break

    vraag_2 = int(input('wat is 453 + 42 = '))

    if vraag_2 == 495:
        print('vraag 2/5 complete')
    else:
        leven -= 1
        print(leven)

    if leven == 0:
        print("Game over")
        break

    vraag_3 = int(input('wat is 5 * 25 + 10 = '))

    if vraag_3 == 10:
        print('vraag 3/5 complete')
    else:
        leven -= 1
        print(leven)

    if leven == 0:
        print("Game over")
        break

    vraag_4 = int(input('wat is (7 + 8) * 10 = '))

    if vraag_4 == 150:
        print('vraag 4/5 complete')
    else:
        leven -= 1
        print(leven)

    if leven == 0:
        print("Game over")
        break

    vraag_5 = int(input('wat is 144 / 12 = '))

    if vraag_5 == 12:
        print('vraag 5/5 complete')
    else:
        leven -= 1
        print(leven)

    if leven == 0:
        print("Game over")
        break

print("challange completed!")
