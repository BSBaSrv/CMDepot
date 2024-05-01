from colorama import init
init()
from colorama import Fore, Back, Style
from art import tprint
from layout import d_print, dialog
from commands import history_data, history_for_back, back

version = '0.3 Alpha'

def page_start():
    d_print("", "10")
    tprint("CMDepot")
    d_print(("Добро пожаловать. Вы запустили мультимедийное консольное приложение " + (Fore.RED + Style.BRIGHT + 'CMDepot') + Style.RESET_ALL + " версии " + \
            (Fore.WHITE + Back.BLACK + Style.BRIGHT + version) + Style.RESET_ALL + ". \nПри любых ошибках в работе пишите на" + \
            (Style.BRIGHT + ' GitHub (github.com/BSBaSrv)') + Style.RESET_ALL + " проекта"), "1110"
    )

#Function ID: 1
def start_list(history_data):
    history_data = history_for_back(1, history_data)
    start_list = ["Магазин программ", "О программе"]
    number_choice = dialog("", start_list, False, "10", "00")
    
    match number_choice:
        case "1":
            page_depot()
        case "2":
            page_about()
        case _:
            d_print("Error - ID: 3 - Incorrect answer", "10")
            return
        
def page_depot():
    return

def page_about():
    d_print((Fore.RED + Style.BRIGHT + "CMDepot." + Style.RESET_ALL + " Версия - " + Fore.WHITE + Back.BLACK + Style.BRIGHT + version + ". Исходный код программы открыт. " + Style.RESET_ALL + \
            "Найди можно на " + Style.BRIGHT + "GitHub (github.com/BSBaSrv)." + Style.RESET_ALL + "\nЗарание извиняюсь за плохой код."), "1110"
    )
    back(history_data)
    return