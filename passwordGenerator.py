#V1
# First version of my password generator
import random
import os.path

uppercaseLetters = [] 
lowercaseLetters = []
specialChars = []

website = input("What is the site you are creating this account? ")
email = input("What is your email account? ")

# Creating file if it doesn't exists
if(os.path.isfile('passwords.txt') != True):
  f = open("passwords.txt", "w")
  f.close()

# Storing what is written in file
f = open("passwords.txt", "r")
otherPasswords = f.readlines()
f.close()


# How many chars of each type you want in your password
uppercasesAmount = int(input("How many uppercases chars you want? "))
for i in range(uppercasesAmount):
  uppercaseLetters.append(chr(random.randint(65,90))) # Uppercase letters ASCII format

lowercasesAmount = int(input("How many lowercases chars you want? "))
for i in range(lowercasesAmount):
  lowercaseLetters.append(chr(random.randint(97,122))) # Lowercase letters ASCII format

specialAmount = int(input("How many special chars you want? "))
for i in range(specialAmount):
  specialChars.append(chr(random.randint(33,38))) # Special chars ASCII format


# Turn to string those random chars

def uppercaseLettersString(array):
  uppercaseString = ''
  for i in range(len(array)):
    uppercaseString += array[i]
  return uppercaseString

def lowercaseLettersString(array):
  lowercaseString = ''
  for i in range(len(array)):
    lowercaseString += array[i]
  return lowercaseString

def  specialCharsString(array):
  specialString = ''
  for i in range(len(array)):
    specialString += array[i]
  return specialString


#Shuffle chars
raw = list(uppercaseLettersString(uppercaseLetters) + lowercaseLettersString(lowercaseLetters) + specialCharsString(specialChars))
random.shuffle(raw)
password = ''.join(raw)

#Just to debug
# account = {
#   "website": website,
#   "email": email,
#   "password": password
# }
# print(account)

# Opened with "a" to append the new password
f = open("passwords.txt", "a")

# Creating what is gonna be written

#If otherPassowords is empty will return False, so do not need \n before to skip line
if(bool(otherPasswords) == False):
   write = ["Website: ", website, "\nEmail: " , email, "\nPassword: ", password]
else:
  write = ["\n\nWebsite: ", website, "\nEmail: " , email, "\nPassword: ", password]

# Writing in .txt file
f.writelines(write)

#Console print
print("New account on",website,"!\nEmail: ",email,"\nPassword:", password)
