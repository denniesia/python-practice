from typing import List
def double_every_second_digit(value: str):
    digits = [int(d) for d in value]
    for i in range(len(digits) - 2, -1, -2):
        doubled = digits[i] * 2
        if doubled > 9:
            doubled -= 9
        digits[i] = doubled

    return digits


def check_validity(digits: List[int]):
    total_sum = sum(digits)
    return total_sum % 10 == 0

def luhn_validator(card_number):
    if isinstance(card_number, int):
        card_number = str(card_number)

    if not card_number.isdigit():
       return "Invalid input — not a number"

    card_number = card_number.replace(' ', '')


    process_digits = double_every_second_digit(card_number)

    if check_validity(process_digits):
        return 'The number is valid'

    return 'The number is NOT valid'




