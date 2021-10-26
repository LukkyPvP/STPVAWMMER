import os


def Main():
    try:
        import time
        import pyautogui

        print('░██████╗████████╗██████╗░██╗░░░██╗░█████╗░░██╗░░░░░░░██╗███╗░░░███╗███╗░░░███╗███████╗██████╗░')
        print('██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗░██║░░██╗░░██║████╗░████║████╗░████║██╔════╝██╔══██╗')
        print('╚█████╗░░░░██║░░░██████╔╝╚██╗░██╔╝███████║░╚██╗████╗██╔╝██╔████╔██║██╔████╔██║█████╗░░██████╔╝')
        print('░╚═══██╗░░░██║░░░██╔═══╝░░╚████╔╝░██╔══██║░░████╔═████║░██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗')
        print('██████╔╝░░░██║░░░██║░░░░░░░╚██╔╝░░██║░░██║░░╚██╔╝░╚██╔╝░██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║')
        print('╚═════╝░░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝')

        Menu = int(input("""
Menu:
[1] - English
[2] - Русский
[3] - Выход / Exit
        """))

        if Menu == 1:
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

        if Menu == 2:
            # У пользователя спрашивают Текст сообщения, Сколько сообщений в секунду и Сколько сообщение
            choice = int(input("""
Слово будет англиское или русское?
[1] - Русское
[2] - Английское
            """))
            if choice == 1:
                print('Для начала напиши текст на англиском но не так Hi А вот так Ghbdtn Это значит Привет')
                print('Напиши текст для спама')
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
                    pyautogui.hotkey('Alt', 'Shift')
                    for i in range(number):
                        pyautogui.typewrite(text, interval)
                        pyautogui.hotkey('enter', interval)
                        print('Осталось:', wait)
                        wait -= 1
                    print('Осталось: 0')
                    print('Спам завершил свою работу')
                if GO == 2:
                    exit()
            if choice == 2:
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
        if Menu == 3:
            exit()

    except ModuleNotFoundError:
        print('Нажмите Enter для уствновки модулей')
        input()
        os.system("python -m pip install requests pyautogui")
        os.system("python -m pip install requests time")
        print('Готово / Done')
        exit()


Main()
# By LukkyPvP_ (Даня Наумов) Version: 0.2.0
