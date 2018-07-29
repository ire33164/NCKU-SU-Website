from random import randint
from random import choice
import bcrypt
import string

word_list = string.ascii_lowercase + string.ascii_uppercase


print("----generate AccountData-----")
f1 = open('accounts.data', 'w')
f2 = open('passwd.data', 'w')
data_sum = int(input('input number (0=skip): '))
ID_list = []

for i in range(data_sum):
  ID = chr(randint(0, 25)+65) + ''.join([chr(randint(0, 9)+48) for i in range(8)])
  ID_list.append(ID)
  passwd = ''.join([chr(randint(48, 112)) for i in range(10)])
  permission = randint(0, 1)
  username = ''.join([chr(randint(65, 91)) for i in range(4)])

  f1.write('{}\t{}\t{}\t{}null\tnull\n'.format(ID, bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'), permission, username))
  f2.write('ID: {} passwd: {}\n'.format(ID, passwd))

f1.close()
f2.close()

##########################################################################3
print("----generate articles-----")
f = open('articles.data', 'w')
#data_sum = int(input('input number (0=skip): '))
for i in range(data_sum):
  title = ''.join(choice(string.ascii_uppercase) for i in range(6))
  content = ''.join([choice(word_list) for i in range(300)])
  f.write('null\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(title, content, randint(0, 1), 'null', 'null', choice(ID_list)))
f.close()

###########################################################################
print("----generate proposals-----")
f = open('proposals.data', 'w')
#data_sum = int(input('input number (0=skip): '))
for i in range(data_sum):
  content = ''.join([choice(word_list) for i in range(300)])
  title = ''.join(choice(string.ascii_uppercase) for i in range(6))
  deadline = ['{}-{}-{}'.format(randint(1000, 2000), randint(1, 12), randint(1, 25)) for i in range(5)]
  voter = randint(50, 100)
  f.write('null\t{}\t{}\t{}\t{}\tfalse\tnull\tnull\t{}\t{}\n'.format(title, content, randint(50, 100), randint(12, 30), choice(ID_list), randint(1, data_sum)))
f.close()

###########################################################################
print("----generate tags-----")
f = open('tags.data', 'w')
#data_sum = int(input('input number (0=skip): '))
for i in range(data_sum):
  f.write('null\t{}\n'.format(''.join(choice(word_list) for i in range(5))))
f.close()

###########################################################################
print("----generate polls-----")
f = open('polls.data', 'w')
for i in range(data_sum):
    f.write("null\t{}\tnull\tnull\t{}\t{}\n".format(randint(0, 1), randint(1, data_sum), choice(ID_list)))
f.close()

###########################################################################
print("----generate discusses-----")
f = open('discusses.data', 'w')
for i in range(data_sum):
    f.write("null\t{}\tnull\tnull\t{}\t{}\n".format(''.join(choice(word_list) for _ in range(50)), choice(ID_list), randint(1, data_sum)))
f.close()

###########################################################################
print("----generate articleTag-----")
f = open('articleTags.data', 'w')
for i in range(data_sum):
    f.write("null\tnull\t{}\t{}\n".format(randint(1, data_sum), randint(1, data_sum)))
f.close()

###########################################################################
print("----generate collection-----")
f = open('collections.data', 'w')
for i in range(data_sum):
    f.write("null\tnull\t{}\t{}\n".format(choice(ID_list), randint(1, data_sum)))
f.close()

###########################################################################
print("----generate proposalAgree-----")
f = open('proposalAgrees.data', 'w')
for i in range(data_sum):
    f.write("null\tnull\t{}\t{}\n".format(randint(1, data_sum), choice(ID_list)))
f.close()

###########################################################################
print("----generate proposalClasses-----")
f = open('proposalClasses.data', 'w')
for i in range(data_sum):
    f.write("null\t{}\n".format(''.join(choice(word_list) for _ in range(5))))
f.close()

###########################################################################
print("----generate proposalTag-----")
f = open('proposalTags.data', 'w')
for i in range(data_sum):
    f.write("null\tnull\t{}\t{}\n".format(randint(1, data_sum), randint(1, data_sum)))
f.close()

###########################################################################
print("----generate replies-----")
f = open('replies.data', 'w')
for i in range(data_sum):
    f.write("null\t{}\tnull\tnull\t{}\t{}\n".format(''.join(choice(word_list) for _ in range(50)), randint(1, data_sum), choice(ID_list)))
f.close()
