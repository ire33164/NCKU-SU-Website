from random import randint
from random import choice
import bcrypt
import string

wordList = string.ascii_lowercase + string.ascii_uppercase


print("----generate AccountData-----")
f1 = open('Account_data.txt', 'w')
f2 = open('passwd.txt', 'w')
data_sum = int(input('input number (0=skip): '))
ID_list = []

for i in range(data_sum):
  ID = chr(randint(0, 25)+65) + ''.join([chr(randint(0, 9)+48) for i in range(8)])
  ID_list.append(ID)
  passwd = ''.join([chr(randint(48, 112)) for i in range(10)])
  permission = randint(0, 1)
  username = ''.join([chr(randint(65, 91)) for i in range(4)])

  f1.write('{}\t{}\t{}\t{}\n'.format(ID, bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'), permission, username))
  f2.write('ID: {} passwd: {}\n'.format(ID, passwd))

f1.close()
f2.close()

##########################################################################3
print("----generate Articles-----")
f = open('Article_data.txt', 'w')
#data_sum = int(input('input number (0=skip): '))
for i in range(data_sum):
  attr = randint(0, 1)
  title = ''.join(choice(string.ascii_uppercase) for i in range(6))
  content = ''.join([choice(wordList) for i in range(300)])
  rt = '/path/to/picture'
  f.write('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format('null', attr, title, content, rt, 'null', 'null', choice(ID_list)))
f.close()

###########################################################################
print("----generate Proposal-----")
f = open('Proposal_data.txt', 'w')
#data_sum = int(input('input number (0=skip): '))
for i in range(data_sum):
  content = ''.join([choice(wordList) for i in range(300)])
  title = ''.join(choice(string.ascii_uppercase) for i in range(6))
  deadline = ['{}-{}-{}'.format(randint(1000, 2000), randint(1, 12), randint(1, 25)) for i in range(5)]
  voter = randint(50, 100)
  f.write('null\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\tnull\tnull\t{}\n'.format(content, title, deadline[0], voter, deadline[1], deadline[2], deadline[3], deadline[4], choice(ID_list)))
f.close()

###########################################################################
print("----generate Tag-----")
f = open('Tag_data.txt', 'w')
#data_sum = int(input('input number (0=skip): '))
for i in range(data_sum):
  f.write('null\t{}\t{}\n'.format(''.join(choice(wordList) for i in range(5)), randint(1, data_sum)))
f.close()
