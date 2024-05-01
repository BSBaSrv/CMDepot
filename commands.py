from colorama import init
init()
from colorama import Fore, Back, Style
from layout import d_print, error, empty_dialog

history_data = []
backup_history_data = []

def help():
    d_print((Style.BRIGHT + 'Выберите один из доступных выше пунктов. ' + Style.RESET_ALL + "\nНо, также, Вы в любой момент можете воспользоваться такими командами как:" + Fore.BLUE + \
    "\n" \
    "\n /help" + Style.RESET_ALL + " - помощь" + Fore.BLUE + \
    "\n /back" + Style.RESET_ALL + " - вернуться" + Fore.BLUE + \
    "\n /exit" + Style.RESET_ALL + " - выход" \
), "111058")
    back(True)

def history_for_back(id: str | int, history_data: list):
    history_data.append(id) 
    return history_data

def back(service_status: bool):
    from commands import backup_history_data, history_data
    from pages import start_list

    match service_status:
        case False:
            match len(history_data):
                case 1:
                    error(7)
                case 0:
                    if len(backup_history_data) != 0:
                        match backup_history_data[-1]:
                            case 1:
                                start_list()
                            case _:
                                error(5)
                case _:
                    if history_data[-1] == history_data[-2]:
                        error(7)
                    else:
                        match history_data[-1]:
                            case 1:
                                start_list()
                                del history_data[-1]
                                backup_history_data.append(1)
                            case _:
                                error(5)
        case True:
            match len(history_data):
                case 0:
                    if len(backup_history_data) != 0:
                        match backup_history_data[-1]:
                            case 1:
                                start_list()
                            case _:
                                error(5)
                case _:
                    match history_data[-1]:
                        case 1:
                            start_list()
                        case _:
                            error(5)

def command(text):
    match text[0]:
        case "/":
            match text:
                case "/help":
                    help()
                    back(True)
                case "/exit":
                    exit()
                case "/back":
                    back(False)
                case _:
                    error(3)
                    back(True)
        case _:
            return text