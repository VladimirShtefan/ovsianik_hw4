def mask_account_card(info: str) - > str:
    """Функция принимает строку с типом карты/счета и номер и возвращает строку с замаскированным номером"""

    def get_mask_card_number(card_number: str) -> str:
        """Функция маскирует номер карты в формате XXXX XX** **** XXXX"""
        card_number = card_number.replace(" ", "")
        if len (card_number) != 16:
            raise ValueError("Номер карты  должен состоять из 16 цифр")
         return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"