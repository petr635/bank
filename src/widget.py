from datetime import datetime

from src import masks


def mask_account_card(account_card: str) -> str:
    """Функция общей маскировки карты и счета"""
    account_card_list = account_card.split()

    # номер счёта 20-ти значный
    # номер карты 16-ти значный
    if len(account_card_list[-1]) == 20:
        mask = masks.get_mask_account(int(account_card_list[-1]))
    elif len(account_card_list[-1]) == 16:
        mask = masks.get_mask_card_number(int(account_card_list[-1]))
    else:
        return ""

    account_card_list[-1] = mask
    return " ".join(account_card_list)


def get_data(day_str: str) -> str:
    """Функция преобразования даты. Входной аргумент: 2018-07-11T02:26:18.671407. Выход функции: 11.07.2018"""
    dt = datetime.strptime("2018-07-11T02:26:18.671407", "%Y-%m-%dT%H:%M:%S.%f")
    return dt.strftime("%d.%m.%Y")
