
for i in range(99,1, -1):
    print(str(i) + ' bottles of beer on the wall,')
    print(str(i) + ' bottles of beer,')
    print('Take one down, \nPass it around,')
    if i > 2:
        print(str(i - 1) + ' bottles of beer on the wall,\n')
    else:
        print(str(i - 1) + ' bottle of beer on the wall,\n')
    i = i - 1

if i == 1:
    print(str(i) + ' bottle of beer on the wall,')
    print(str(i) + ' bottle of beer,')
    print('Take one down, \nPass it around,')
    print('No more bottles of beer on the wall!')
