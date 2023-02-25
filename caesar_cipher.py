def encode(message: str, shift: int) -> str:

    shift %= 26
    encoded_message = ""

    for i in message:
        letter_ascii = ord(i)

        if letter_ascii >= 65 and letter_ascii <= 90:
            letter_ascii += shift
            if letter_ascii > 90:
                letter_ascii = 64 + (letter_ascii - 90)
        else:
            letter_ascii += shift
            if letter_ascii > 122:
                letter_ascii = 96 + (letter_ascii - 122)

        encoded_letter = chr(letter_ascii)
        encoded_message += encoded_letter

    return encoded_message


def decode(message, shift) -> str:
    shift %= 26
    decoded_message = ""

    for i in message:
        letter_ascii = ord(i)

        if letter_ascii >= 65 and letter_ascii <= 90:
            letter_ascii -= shift
            if letter_ascii < 65:
                letter_ascii = 91 - (65 - letter_ascii)
        else:
            letter_ascii -= shift
            if letter_ascii < 97:
                letter_ascii = 123 - (97 - letter_ascii)

        decoded_letter = chr(letter_ascii)
        decoded_message += decoded_letter

    return decoded_message
