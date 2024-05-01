from colorama import Fore, Back, Style

#Главная часть №1
def l_print(list):
    for num in range(len(list)):
        print(str(num + 1) + ".", list[num])

def d_print(text: str | list, divisions: str):
    divisions = list(divisions)
    num_of_len_division = 0

    if "\n" in text:
        div_text = list(text.split("\n"))
    else:
        div_text = text

    match div_text:
        case []:
            num_of_len_division = 0

        case str(div_text):
            if len(div_text) >= 40:
                num_of_len_division = int(len(div_text) + 5)
            else:
                num_of_len_division = 40

        case list(div_text):
            if len(max(div_text, key = len)) >= 40:
                num_of_len_division = len(str(max(div_text, key = len))) - str(max(div_text, key = len)).count("\x1b")*4
            else:
                num_of_len_division = 40

        case _:
            print("Error - ID: 1 - Incorrect type of text")

    match len(divisions):
        case 4:
            for i in range(int(divisions[0])):
                print("")
            for i in range(num_of_len_division):
                print("=", end = "") 
            print("")
            for i in range(int(divisions[1])):
                print("")

            if text == str(text):
                print(text)
            elif text == list(text):
                l_print(text)
            else:
                print("Error - ID: 1 - Incorrect type of text")

            for i in range(int(divisions[2])):
                print("")
            for i in range(num_of_len_division):
                print("=", end = "")
            print("")
            for i in range(int(divisions[3])):
                print("")

        case 2:
            if divisions[0] != 0:
                for i in range(int(divisions[0])):
                    print("")

            if text == str(text) and text != "":
                print(text)
            elif text == list(text) and text != []:
                l_print(text)
            elif text == [] or text == "":
                pass
            else:
                print("Error - ID: 1 - Incorrect type of text")

            for i in range(int(divisions[1])):
                print("")
        case _:
            print("Error - ID: 2 - Incorrect division setting. Commands starts with '/'")


#Команды. Перемещено из-за циклических импортов (я дегенерат, простите)
        
def help():
    d_print((Style.BRIGHT + 'Выберите один из выше доступных пунктов. ' + Style.RESET_ALL + "\nНо, также, Вы в любой момент можете воспользоваться такими командами как:" + Fore.BLUE + \
    "\n" \
    "\n /help" + Style.RESET_ALL + " - помощь" + Fore.BLUE + \
    "\n /back" + Style.RESET_ALL + " - вернуться" + Fore.BLUE + \
    "\n /exit" + Style.RESET_ALL + " - выход" \
), "1110")

def history_for_back():
    return

def back():
    return

def command(text):
    match text[0]:
        case "/":
            match text:
                case "/help":
                    help()
                    empty_dialog()
                case "/exit":
                    exit()
                case "/back":
                    back()
                    empty_dialog()
                case _:
                    d_print("Error - ID: 4 - Unkown command")
                    empty_dialog()
        case _:
            return int(text)
        
#help()

#Главная часть №2
def dialog(text: str, choice_list: list, permission: bool, divisions_list: str, divisions_perm: str):
    permission_dialog_list = ["Да", "Нет"]
    num_choice = 0

    if text != "" or text != " ":
        d_print(text, "00")
    else:
        pass

    d_print(choice_list, divisions_list)

    num_choice = input("> ")
    command(num_choice)
        
    if permission == True:
                print("Вы уверены?")
                d_print(permission_dialog_list, divisions_perm)
    else:
        return num_choice

    permission_num_choice = input("> ")
    command(permission_num_choice)

    if permission_num_choice == 1:
        return num_choice
    
def empty_dialog():
    dialog("", [], False, "10", "00")
    
#d_print(["Прива)", "Негр", "Сам негр"], "1111")
#num_choice = 0; dialog("Ты балбес?", ["Да", "Нет"], False, num_choice, "22", "00")