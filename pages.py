from colorama import init
from colorama import Fore, Back, Style
from art import tprint
from layout import d_print, dialog, error
from commands import back
init()

version = "0.3.3 Alpha"

def page_start():
    d_print("", "10none")
    tprint("CMDepot")
    d_print(("Добро пожаловать. Вы запустили мультимедийное консольное приложение " + (Fore.RED + Style.BRIGHT + 'CMDepot') + Style.RESET_ALL + " версии " + \
            (Fore.GREEN + Back.BLACK + Style.BRIGHT + version) + Style.RESET_ALL + ". \nПри любых ошибках в работе пишите на" + \
            (Style.BRIGHT + Fore.BLUE + " GitHub (github.com/BSBaSrv/CMDepot)") + Style.RESET_ALL + " проекта. \nДля навигации можно использовать команды " + Fore.WHITE + \
            Back.BLACK + Style.BRIGHT + Fore.WHITE + "(подробнее /help)" + Style.RESET_ALL), 
            "111069none"
    )

#ID: 1
def start_list():
    from commands import history_data, history_for_back
    history_data = history_for_back(1, history_data)
    start_list = ["Магазин программ", "О программе"]
    number_choice = dialog("", start_list, False, "10none", "00none")
    
    match str(number_choice):
        case "1":
            page_depot()
        case "2":
            page_about()
        case _:
            error(3)
        
def page_depot():
    d_print(Style.BRIGHT + "Извините. " + Style.RESET_ALL + "Это вкладка ещё не готова", "111078none")
    back(True)

def page_about():
    d_print((Fore.RED + Style.BRIGHT + "CMDepot." + Style.RESET_ALL + " Версия - " + Fore.GREEN + Back.BLACK + Style.BRIGHT + version + Style.RESET_ALL + \
            ". " + Style.BRIGHT + "Исходный код программы открыт. " + Style.RESET_ALL + "Найти можно на " + Style.BRIGHT + Fore.BLUE + "GitHub (github.com/BSBaSrv/CMDepot)." + \
            Style.RESET_ALL + "\nЗа плохой код простите."), "111078none"
    )
    back(True)