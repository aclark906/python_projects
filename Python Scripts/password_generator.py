import random
LOWER_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '1234567890'
SPECIAL = '~!@#$%^&*()_+.'

all_chars = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
def generatePassword(length):
    if length < 12:
        length = 12
    all_chars_str = ''.join(all_chars)
    # all_chars_list = list(all_chars)
    one_num = random.choices(list(NUMBERS), k = 1)
    one_upper = random.choices(list(UPPER_LETTERS), k = 1)
    one_lower = random.choices(list(LOWER_LETTERS), k = 1)
    one_char = random.choices(list(SPECIAL), k = 1)
    required_elems = one_num + one_upper + one_lower + one_char
    rest = random.choices(all_chars_str, k = length - 4)
    combined = required_elems + rest
    random.shuffle(combined)
    return ''.join(combined)

  


assert len(generatePassword(8)) == 12

 

pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in LOWER_LETTERS:

        hasLowercase = True

    if character in UPPER_LETTERS:

        hasUppercase = True

    if character in NUMBERS:

        hasNumber = True

    if character in SPECIAL:

        hasSpecial = True

assert hasLowercase == True and hasUppercase == True and hasNumber == True and hasSpecial == True