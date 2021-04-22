try:
    a = int(input('masukkan nilai a: '))
    b = int(input('masukkan nilai b: '))
    c = a / b
    print(f'{a} / {b} = {c}')

except ZeroDivisionError as e:
    print('Error : tidak boleh dibagi 0')

f = ''

try:
    f = open('contoh.txt', 'r')
    lines = f.readlines()
    for line in lines:
        print(line, end='\n')

except IOError as e:
    print('Error : File Hilang')

finally:
    if f:
        f.close()
