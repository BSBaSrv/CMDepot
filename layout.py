from colorama import init
from colorama import Fore, Style
import re
init()

#Вспомогательная часть
def error(num: int):
    from commands import back, history_data
    match num:
        case 1:
            d_print(Fore.RED + "Error - ID: 1 - Incorrect type of text" + Style.RESET_ALL, "10none")
            back(True)
        case 2:
            d_print(Fore.RED + "Error - ID: 2 - Incorrect division setting" + Style.RESET_ALL, "10none")
            back(True)
        case 3:
            d_print(Fore.RED + "Error - ID: 3 - Unkown command" + Style.RESET_ALL, "10none",)
            back(True)
        case 4:
            d_print(Fore.RED + "Error - ID: 4 - You can't choose in EMPTY dialog" + Style.RESET_ALL, "10none")
            back(True)
        case 5:
            d_print(Fore.RED + "Error - ID: 5 - Somthing is wrong... This function never doesn't exist" + Style.RESET_ALL, "10none")
            back(True)
        case 6:
            d_print(Fore.RED + "Error - ID: 6 - This type of division never doesn't exist" + Style.RESET_ALL, "10none")
            back(True)
        case 7:
            d_print(Fore.RED + "Error - ID: 7 - Where to?" + Style.RESET_ALL, "10none")
            back(True)
        case 8:
            d_print(Fore.RED + "Error - ID: 8 - This color never doesn't exist" + Style.RESET_ALL, "10none")
            back(True)
        case _:
            d_print(Fore.RED + "Error - ID: 8 - Error ID doesn't exist" + Style.RESET_ALL, "10none")
            back(True)


#Главная часть
def c_print(text: str, color: str, not_end: bool):
    match not_end:
        case True:
            match color.lower():
                case "red":
                    print(Fore.RED + text + Style.RESET_ALL, end = "")
                case "green":
                    print(Fore.GREEN + text + Style.RESET_ALL, end = "")
                case "yellow":
                    print(Fore.YELLOW + text + Style.RESET_ALL, end = "")
                case "magenta":
                    print(Fore.MAGENTA + text + Style.RESET_ALL, end = "")
                case "cyan":
                    print(Fore.CYAN + text + Style.RESET_ALL, end = "")
                case "white":
                    print(Fore.WHITE + text + Style.RESET_ALL, end = "")
                case _:
                    print(text, end = "")
        case False:
            match color.lower():
                case "red":
                    print(Fore.RED + text + Style.RESET_ALL)
                case "green":
                    print(Fore.GREEN + text + Style.RESET_ALL)
                case "yellow":
                    print(Fore.YELLOW + text + Style.RESET_ALL)
                case "magenta":
                    print(Fore.MAGENTA + text + Style.RESET_ALL)
                case "cyan":
                    print(Fore.CYAN + text + Style.RESET_ALL)
                case "white":
                    print(Fore.WHITE + text + Style.RESET_ALL)
                case _:
                    print(text)

def l_print(list: str):
    for num in range(len(list)):
        print(str(num + 1) + ".", list[num])

def d_print(text: str | list, divisions_settings: str):
    def empty_division(num: int | str):
        if int(num) != 0:
            for n in range(int(num)):
                print("")
        else:
            pass

    def division(type: int, settings: int):
        from math import ceil

        lenght = int(re.sub("\D", "", settings))
        color = re.sub("\d+", "", settings)
        match int(type):
            case 0:
                pass
            case 1:
                for n in range(lenght):
                    print("=", end = "")
                print("")     
            case 2:
                for n in range(lenght):
                    print("-", end = "")
                print("")
            case 3:
                for n in range(lenght):
                    print("_", end = "")
                print("")
            case 4:
                c_print("xX+-", color, True)
                for n in range(ceil((lenght - 8 - 11) / 2)):
                    print("=", end = "")
                c_print("-_xX{=}Xx_-", color, True)
                for n in range(ceil((lenght - 8 - 11) / 2)):
                    print("=", end = "")
                c_print("-+Xx", color, False)
            case 5:
                c_print("(:+>=", color, True)
                for n in range(lenght - 10):
                    print("-", end = "")
                c_print("=<+:)", color, False)
            case 6:
                c_print("):+>=", color, True)
                for n in range(ceil((lenght - 10 - 9) / 2)):
                    print("-", end = "")
                c_print("_xX{=}Xx_", color, True)
                for n in range(ceil((lenght - 10 - 9) / 2)):
                    print("-", end = "")
                c_print("=<+:(", color, False)
            case 7:
                c_print("/>-", color, True)
                for n in range(ceil((lenght - 6 - 9) / 2)):
                    print("=", end = "")
                c_print("_xX{=}Xx_", color, True)
                for n in range(ceil((lenght - 6 - 9) / 2)):
                    print("=", end = "")
                c_print("-<\A"[:-1], color, False)
            case 8:
                c_print("\>-", color, True)
                for n in range(lenght - 6):
                    print("=", end = "")
                c_print("-</", color, False)
            case 9:
                c_print("|>-<", color, True)
                for n in range(lenght - 8):
                    print("=", end = "")
                c_print(">-<|", color, False)
            case _:
                error(6)

    divisions = list(re.sub("\D", "", divisions_settings))
    div_lenght = 0

    if "\n" in text:
        div_text = list(text.split("\n"))
    else:
        div_text = text

    match div_text:
        case []:
            div_lenght = 0

        case str(div_text):
            if len(div_text) >= 40:
                div_lenght = int(len(div_text) + 5)
            else:
                div_lenght = 40

        case list(div_text):
            if len(max(div_text, key = len)) >= 40:
                div_lenght = len(str(max(div_text, key = len))) - str(max(div_text, key = len)).count("\x1b")*4
            else:
                div_lenght = 40
        case _:
            error(1)

    divisions_settings = str(div_lenght) + re.sub("\d+", "", divisions_settings)

    match len(divisions) - 2:
        case 4:
            empty_division(int(divisions[0]))
            division(divisions[-2], divisions_settings)
            empty_division(int(divisions[1]))

            if text == str(text):
                print(text)
            elif text == list(text):
                l_print(text)
            else:
                error(1)

            empty_division(int(divisions[2]))
            division(divisions[-1], divisions_settings)
            empty_division(int(divisions[3]))
        case 0:
            empty_division(divisions[0])

            if text == str(text) and text != "":
                print(text)
            elif text == list(text) and text != []:
                l_print(text)
            elif text == [] or text == "":
                pass
            else:
                error(1)

            empty_division(divisions[1])
        case _:
            error(2)

def dialog(text: str, choice_list: list, permission: bool, divisions_list: str, divisions_perm: str):

    from commands import command
    permission_dialog_list = ["Да", "Нет"]
    num_choice = 0

    if text != "" or text != " ":
        d_print(text, "00none")
    else:
        pass

    d_print(choice_list, divisions_list)

    num_choice = input(Fore.RED + "> " + Style.RESET_ALL)
    num_choice = num_choice.strip()
    command(num_choice)
        
    if permission == True:
                print("Вы уверены?")
                d_print(permission_dialog_list, divisions_perm)
    else:
        return num_choice

    permission_num_choice = input(Fore.RED + "> " + Style.RESET_ALL)
    permission_num_choice = permission_num_choice.strip()
    command(permission_num_choice)

    if permission_num_choice == 1:
        return num_choice
    
def empty_dialog():
    num_or_not = dialog("", [], False, "10none", "00none")

    if num_or_not != "":
        error(4)