# from masks import get_mask_account, get_mask_card_number
import masks
from datetime import datetime

def mask_account_card(account: str) -> str:
    """Функция общей маскировки карты и счета"""
    # get_mask_account()
    # get_mask_card_number()
    # Примеры входных данных:
    #
    # Maestro 1596837868705199
    # Счет 64686473678894779589
    # MasterCard 7158300734726758
    # Счет 35383033474447895560
    # Visa Classic 6831982476737658
    # Visa Platinum 8990922113665229
    # Visa Gold 5999414228426353
    # Счет 73654108430135874305
    masks.
    pass


def get_data(day_str: str) -> str:
    """Функция преобразования даты. Входной аргумент: 2018-07-11T02:26:18.671407. Выход функции: 11.07.2018"""
    dt = datetime.strptime('2018-07-11T02:26:18.671407', '%Y-%m-%dT%H:%M:%S.%f')
    return dt.strftime('%d.%m.%Y')