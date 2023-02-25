from caesar_cipher import *

def launch():
    print("Let's encrypt!")

    valid_game = True

    while valid_game:

        choice = input(
            "Type 'encode' to encrypt, 'decode' to decrypt or 'stop' to stop the program: ")

        if choice == "stop":
            valid_game = False
            continue
        elif choice != "encode" and choice != "decode":
            print("You entered invalid function, try again! \n")
            continue

        valid_message = False
        while not valid_message:
            message = input("Type your message: ")

            if message.isalpha() == True:
                valid_message = True
            else:
                print("\nInvalid message number, try again!")

        valid_shift = False
        while not valid_shift:
            try:
                shift = input("Type your shift number: ")
                shift = int(shift)
                valid_shift = True
            except:
                print("\nInvalid shift number, try again!")

        if choice == 'encode':
            encoded_message = encode(message, shift)
            print(f"Encoded message: {encoded_message} \n")
        elif choice == 'decode':
            decoded_message = decode(message, shift)
            print(f"Decoded message: {decoded_message} \n")
