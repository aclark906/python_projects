def ordinalSuffix(number):  
    if number == 0 or number in range(4,21):
        return (str(number) + 'th')
    elif str(number).endswith('1') and number != 11:
        return (str(number) + 'st')
    elif str(number).endswith('2') and number != 12:
        return (str(number) + 'nd')
    else:
        return (str(number) + 'rd')


assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'
    