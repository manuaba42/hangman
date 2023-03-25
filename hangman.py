import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

arr_list = ['federal', 'liberal', 'democrate']

rando = random.choice(arr_list)
arr = []
for i in rando:
    arr.append("_")

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)

# newarr = []
num = len(stages)
condi = True
while condi == True:
    letter = input("Guess a letter: ")

    for index, i in enumerate(rando):
        if i == letter:
            # print('Right')
            arr[index] = letter
            # newarr.append(letter)
        # else:
            # print("Wrong")
            # newarr.append("_")

    if letter not in rando:
        num = num - 1
    if num-1 == 0:
        print("You Lose")
        condi = False

    print(" ".join(arr))
    print(stages[num-1])
    if "".join(arr) == rando:
        # print(rando)
        print("Well Done!!")
        condi = False
