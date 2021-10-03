import os
import time
import pyautogui

print('░██████╗████████╗██████╗░██╗░░░██╗░█████╗░░██╗░░░░░░░██╗███╗░░░███╗███╗░░░███╗███████╗██████╗░')
print('██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗░██║░░██╗░░██║████╗░████║████╗░████║██╔════╝██╔══██╗')
print('╚█████╗░░░░██║░░░██████╔╝╚██╗░██╔╝███████║░╚██╗████╗██╔╝██╔████╔██║██╔████╔██║█████╗░░██████╔╝')
print('░╚═══██╗░░░██║░░░██╔═══╝░░╚████╔╝░██╔══██║░░████╔═████║░██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗')
print('██████╔╝░░░██║░░░██║░░░░░░░╚██╔╝░░██║░░██║░░╚██╔╝░╚██╔╝░██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║')
print('╚═════╝░░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝')

language = int(input("""
Language:
[1] - English
[2] - Русский
[3] - Выход / Exit
[4] - Установить Библиотеки / Install Libraries
"""))

if language == 1:
    # The user is asked this such as (Message text, How many messages per second and How many messages)
    print('Write a text for spam (in English only)')
    text = input()
    print('How many messages per second? Example: 0.0000000000001')
    interval = input()
    print('How many times to write a message?')
    number = int(input())

    # How long to wait
    wait = number

    # Timer
    print('After you write 1, you will have 5 seconds to prepare')
    GO = int(input("""
    GO:
    [1] - Start Spam
    [2] - Exiting the program
    """))
    if GO == 1:
        print("Time's up")
        time.sleep(5)
        print('Start')

        # Base
        for i in range(number):
            pyautogui.typewrite(text, interval)
            pyautogui.hotkey('enter', interval)
            print('Left:', wait)
            wait -= 1
        print('Left: 0')
        print('Spam has completed its work')
    if GO == 2:
        exit()

if language == 2:
    # У пользователя спрашивают данный такие как (Текст сообщения, Сколько сообщений в секунду и Сколько сообщение)
    print('Напиши текст для спама (Только на англиском)')
    text = input()
    print('Сколько сообщение в секунду? Пример: 0.0000000000001')
    interval = input()
    print('Сколько раз написать собщение?')
    number = int(input())

    # Сколько осталось ждать
    wait = number

    # Таймер
    print('После того как ты напишишь 1 у тебя будет 5 секунд на подготовку')
    GO = int(input("""
    GO:
    [1] - Начать спам
    [2] - Выход из программы
    """))

    if GO == 1:
        print('Время пошло')
        time.sleep(5)
        print('Старт')

        # Основа
        for i in range(number):
            pyautogui.typewrite(text, interval)
            pyautogui.hotkey('enter', interval)
            print('Осталось:', wait)
            wait -= 1
        print('Осталось: 0')
        print('Спам завершил свою работу')
    if GO == 2:
        exit()
if language == 3:
    exit()

if language == 4:
    os.system("python -m pip install requests pyautogui")
    os.system("python -m pip install requests time")
    print('Готово / Done')
    exit()
# By LukkyPvP_ (Даня Наумов) Version: 0.1.0
