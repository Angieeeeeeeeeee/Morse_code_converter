from convert import Convert

convert = Convert()


def converter():
    morse_or_alphabet = input("if morse -> alphabet type 1 else type 2:\n")
    if morse_or_alphabet == "1":
        want_to_convert_code = input("Plz type you want to morse code:\n")
        print(convert.change_morse(want_to_convert_code))
    else:
        want_to_convert_code = input("Plz type you want to alphabet code:\n")
        print(convert.change_alphabet(want_to_convert_code))


converter()


