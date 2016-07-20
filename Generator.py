import random 

class Generator(object):

    def __init__(self, length = 8, letters_allowed = True, numbers_allowed = True, caps_letters_allowed = True, special_characters_allowed = True, min_num_of_letters = 0, min_num_of_numbers = 0, min_num_of_caps_letters = 0, min_num_of_special_characters = 0, letters = "qwertyuiopasdfghjklzxcvbnm", uppercase_letters = "QWERTYUIOPASDFGHJKLZXCVBNM", numbers = "0123456789", simbols = "!@#$%^&*()-_=+[]{};:\"\\|,<.>/?\"'`", allowed_chars = ""):
       self.length = length

       self.numbers_allowed = numbers_allowed
       self.letters_allowed = letters_allowed
       self.caps_letters_allowed = caps_letters_allowed
       self.special_characters_allowed = special_characters_allowed

       self.numbers_required = min_num_of_numbers
       self.letters_required = min_num_of_letters
       self.caps_letters_required = min_num_of_caps_letters
       self.special_characters_required = min_num_of_special_characters
       
       self.letters = letters
       self.uppercase_letters = uppercase_letters
       self.numbers = numbers
       self.simbols = simbols
       self.allowed_chars = list(set(allowed_chars))

    def generate(self):
        #building the set of allowed characters
        allowed_chars = self.allowed_chars

        if not len(allowed_chars) > 0:

            if self.letters_allowed:
                start_index_letters = len(allowed_chars)
                for char in self.letters:
                    allowed_chars.append(char)
                end_index_letters = len(allowed_chars) - 1

            if self.caps_letters_allowed:
                start_index_uppercase_letters = len(allowed_chars)
                for char in self.uppercase_letters:
                    allowed_chars.append(char)
                end_index_uppercase_letters = len(allowed_chars) - 1

            if self.numbers_allowed:
                start_index_numbers = len(allowed_chars)
                for char in self.numbers:
                    allowed_chars.append(char)
                end_index_numbers = len(allowed_chars) - 1

            if self.special_characters_allowed:
                start_index_special_characters = len(allowed_chars)
                for char in self.simbols:
                    allowed_chars.append(char)
                end_index_special_characters = len(allowed_chars) - 1
                
            if len(allowed_chars) == 0:
                return ""

        #Starting to generate the password

        password = ""
        num_of_letters = 0
        num_of_numbers = 0
        num_of_uppercase_letters = 0
        num_of_special_characters = 0

        for i in range(self.length):
            if num_of_letters < self.letters_required:
                char = random.randint(start_index_letters, end_index_letters)
                password = password + (allowed_chars[char])
                num_of_letters += 1
                continue
            if num_of_uppercase_letters < self.caps_letters_required:
                char = random.randint(start_index_uppercase_letters, end_index_uppercase_letters)
                password = password + (allowed_chars[char])
                num_of_uppercase_letters += 1
                continue
            if num_of_numbers < self.numbers_required:
                char = random.randint(start_index_numbers, end_index_numbers)
                password = password + (allowed_chars[char])
                num_of_numbers += 1
                continue
            if num_of_special_characters < self.special_characters_required:
                char = random.randint(start_index_special_characters, end_index_special_characters)
                password = password + (allowed_chars[char])
                num_of_special_characters += 1
                continue

            char = random.randint(0, len(allowed_chars)-1)
            password = password + (allowed_chars[char])

        l = list(password)
        random.shuffle(l)
        return (''.join(l))

if __name__ == "__main__":
    #all simbols
    g = Generator()
    #only numbers
    g1 = Generator(length = 8, letters_allowed = False, numbers_allowed = True, caps_letters_allowed = False, special_characters_allowed = False)
    #only uppercase letters
    g2 = Generator(length = 8, letters_allowed = False, numbers_allowed = False, caps_letters_allowed = True, special_characters_allowed = False)
    #only simbols
    g3 = Generator(length = 8, letters_allowed = False, numbers_allowed = False, caps_letters_allowed = False, special_characters_allowed = True)
    #only simbols and numbers, exactly 4 and 4
    g4 = Generator(length = 8, letters_allowed = False, numbers_allowed = True, caps_letters_allowed = False, special_characters_allowed = True, min_num_of_letters = 0, min_num_of_numbers = 4, min_num_of_caps_letters = 0, min_num_of_special_characters = 4)
    #no simbols
    g5 = Generator(length = 8, letters_allowed = True, numbers_allowed = True, caps_letters_allowed = True, special_characters_allowed = False)
    #only a and b
    g6 = Generator(length = 8, letters_allowed = True, numbers_allowed = True, caps_letters_allowed = True, special_characters_allowed = False, allowed_chars = "ab")

    print(g6.generate())
