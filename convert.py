import morse_code_dict

morse_dict = morse_code_dict.morse_dict


class Convert:
    def __init__(self):
        self.changed_string_list = []

    def change_alphabet(self, string):
        upper_string = string.upper()
        list(upper_string)
        for letter in list(upper_string):
            self.changed_string_list.append(morse_dict[letter])
        changed_string = " ".join(self.changed_string_list)
        return changed_string

    def change_morse(self, morse_codes):
        morse_list = morse_codes.split()
        for morse in morse_list:
            for key_alphabet, value_morse in morse_dict.items():
                if value_morse == morse:
                    self.changed_string_list.append(key_alphabet)
        changed_string = "".join(self.changed_string_list)
        return changed_string


