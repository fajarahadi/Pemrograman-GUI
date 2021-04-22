#menggunakan variabel
angka = 10

# param 1 = maks
for i in range(angka):
  print('Angka ke :')
  print(i)

#param 2 = min,maks (increment)
for i in range(angka, 20):
  print('Angka ke :')
  print(i)

#param 3 = min, maks, lompatan +(decre)
#param 3 = maks, min, lompatan -(incre)
for i in range(angka, 20, -2):
  print('Angka ke :')
  print(i)

#array
array = [1,2,3,4,5]

for i in array:
  print(i, end = ' ')
