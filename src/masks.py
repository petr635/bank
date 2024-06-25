def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера карты. Входной аргумент: 7000792289606361. Выход функции: 7000 79** **** 6361"""
    numbers = []
    numbers.append(str(card_number)[:4])
    numbers.append(str(card_number)[4:6] + "**")
    numbers.append("****")
    numbers.append(str(card_number)[-4:])
    return " ".join(numbers)


def get_mask_account(account_number: int) -> str:
    """Функция маскировки номера счета. Входной аргумент: 73654108430135874305. Выход функции: **4305"""
    return f"**{account_number % 10000}"
