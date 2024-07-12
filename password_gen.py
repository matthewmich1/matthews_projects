import random

password_length = int(input('Passowrd length: '))
while password_length < 4:
  print('password length must be at least 4 characters.')
  password_length = int(input('Passowrd length: '))

char = ['-_/\.,!%$','abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','0123456789']

password = ''
symb = False
low_a = False
upp_a = False
num = False

while symb == False and low_a == False and upp_a == False and num == False:

  for i in range(password_length):
    ind = random.randint(0,3)
    password = password + random.choice(list(char[ind])) #create password
    #check if password is valid
    if ind == 0:
      symb = True
    if ind == 1:
      low_a = True
    if ind == 2:
      upp_a = True
    if ind == 3:
      num = True

print(password)
