import random
answer = random.randint(1,101)
popit = 1

num = int(input(" угадайте число "))
while num != answer:
    popit = popit + 1
    if num > answer:
        print("загаданное число меньше", num)
    elif num < answer:
         print("загаданное число больше", num)
    print("попытка номер",popit)
    num = int(input(" попробуйте еща раз угадать число "))
print("вы угадали число", answer, "за",popit, "попыток"  )
