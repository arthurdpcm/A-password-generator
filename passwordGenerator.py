#V2
# Second version of my password generator
import PySimpleGUI as sg
import random
import os.path

########################

# Creating file if it doesn't exists
if(os.path.isfile('passwords.txt') != True):
  f = open("passwords.txt", "w")
  f.close()

# Storing what is written in file
f = open("passwords.txt", "r")
otherPasswords = f.readlines()
f.close()

# Opened with "a" to append the new password
f = open("passwords.txt", "a")
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

def writeFile(website, email, password):
  # # Opened with "a" to append the new password
  f = open("passwords.txt", "a")

  # Creating what is gonna be written
  #If otherPassowords is empty will return False, so do not need \n before to skip line
  if(bool(otherPasswords) == False):
    write = ["Website: ", website, "\nEmail: " , email, "\nPassword: ", password]
    
  else:
    write = ["\n\nWebsite: ", website, "\nEmail: " , email, "\nPassword: ", password]

  # Writing in .txt file
  f.writelines(write)

def generatePassword():
  uppercaseLetters = [] 
  lowercaseLetters = []
  specialChars = []

  # How many chars of each type you want in your password
  uppercasesAmount = random.randint(2,5)
  for i in range(uppercasesAmount):
    uppercaseLetters.append(chr(random.randint(65,90))) # Uppercase letters ASCII format

  lowercasesAmount = random.randint(3,7)
  for i in range(lowercasesAmount):
    lowercaseLetters.append(chr(random.randint(97,122))) # Lowercase letters ASCII format

  specialAmount = random.randint(1,2)
  for i in range(specialAmount):
    specialChars.append(chr(random.randint(33,38))) # Special chars ASCII format

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

  return password

########################## PySimpleGUI

sg.theme('DarkAmber')

layout = [
      [sg.Text('Password Manager')],
      [sg.Button('Old account'), sg.Button('New account')]
    ]

layoutError = [
      [sg.Text('Error, try again.')],
      [sg.Button('Close')]
    ]
layoutOldAccount = [
      [sg.Text('Old Account')],
      [sg.Text('Website', size =(15, 1)), sg.InputText()], #values[0]
      [sg.Text('Email', size =(15, 1)), sg.InputText()], #values[1]
      [sg.Text('Password', size =(15, 1)), sg.InputText()], #values[2]
      [sg.Submit('Store'), sg.Button('Cancel')] # event == 'Store'
    ]
layoutNewAccount = [
      [sg.Text('New Account')],
      [sg.Text('Website', size =(15, 1)), sg.InputText()],
      [sg.Text('Email', size =(15, 1)), sg.InputText()],
      [sg.Submit('Generate Password'), sg.Button('Cancel')]
    ]

layoutMissingInfo = [
    [sg.Text('Missing Info!')],
    [sg.Button('Close')]
]


window = sg.Window('Password Manager', layout=layout, size=(300, 300))
events, values = window.Read()
try:

  # Old account
  if events == 'Old account':
    window.close()
    window = sg.Window('Password Manager', layout=layoutOldAccount)
    events, values = window.Read()
    website = values[0]
    email = values[1]
    password = values[2]

    if events == 'Store':
      window.close()

      if(website and email and password):
        window = sg.Window('Password Manager', layout=[
          [sg.Text('Website:', size =(15, 1)), sg.Text(website)],
          [sg.Text('Email:', size =(15, 1)), sg.Text(email)],
          [sg.Text('Password:', size =(15, 1)), sg.Text(password)],
          [sg.Button('Close')]
        ] )
        events, values = window.Read()
        writeFile(website, email, password)
        print('Your account is now registered on passwords.txt')
      else:
        window.close()
        window = sg.Window('Password Manager', layout=layoutMissingInfo)
        events, values = window.Read()
        


  # New account
  elif events == 'New account':
    window.close()
    window = sg.Window('Password Manager', layout=layoutNewAccount)
    events, values = window.Read()
    website = values[0]
    email = values[1]

    if events == 'Generate Password':
      password = generatePassword()
      window.close()
      window = sg.Window('Password Manager', layout=[
        [sg.Text('Website:', size =(15, 1)), sg.Text(website)],
        [sg.Text('Email:', size =(15, 1)), sg.Text(email)],
        [sg.Text('Password:', size =(15, 1)), sg.Text(password)],
        [sg.Button('Close')]
      ] )
      events, values = window.Read()
      if(website and email and password):
        writeFile(website, email, password)
        print('Your account is now registered on passwords.txt')
      else:
        window.close()
        window = sg.Window('Password Manager', layout=layoutMissingInfo)
        events, values = window.Read()
      

except:
  window.close()
  window = sg.Window('Password Manager', layout=layoutError)
  events, values = window.Read()
  if events == 'Close':
    window.close()


