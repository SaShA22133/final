import pyautogui, random,  time, keyboard
answer = random.randint(1,101)
popit = 1

num = int(input(" Привет! Если угадаешь случайное число то можешь посмотреть ютуб "))
while num != answer:
    popit = popit + 1
    if num > answer:
        print("загаданное число меньше", num)
    elif num < answer:
         print("загаданное число больше", num)
    print("попытка номер",popit)
    num = int(input(" попробуйте еща раз угадать число "))
    
   
print("вы угадали число", answer, "за",popit, "попыток"  )
num = input(" молодец! А теперь что бы ты хотел посмотреть в ютубе? ")
pyautogui.moveTo(1250, 10)

pyautogui.click()
time.sleep(1)
pyautogui.click()
pyautogui.click()
time.sleep(2)

keyboard.write('https://www.youtube.com/')
pyautogui.hotkey("enter")
pyautogui.moveTo(850, 100)
time.sleep(4)
pyautogui.click()
keyboard.write(num)
pyautogui.hotkey("enter")


