
# *    __ __   ___    _  __  _____   __  ___   ___    _  __
# *   / // /  / _ |  / |/ / / ___/  /  |/  /  / _ |  / |/ /
# *  / _  /  / __ | /    / / (_ /  / /|_/ /  / __ | /    /
# * /_//_/  /_/ |_|/_/|_/  \___/  /_/  /_/  /_/ |_|/_/|_/

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
import random

words = ["apple", "banana", "mango", "guava", "orange", "strawberry"]
random_word = random.choice(words)
print(random_word)
dash = ""
for i in random_word:
    i = "_ "
    dash = dash+i
list_of_dash = dash.split()
game_is_end=False
life=6
while not game_is_end:
    letter = input("Guess a letter\n").lower()
    # for i in range(0,len(random_word)):
    #     if letter==random_word[i]:
    #         print("True")

    #     else:
    #         print("False")

    # print(dash)
    # dash.split()
    # list_of_dash=dash.split()
    # print(list_of_dash)

    for i in range(0, len(random_word)):
        if random_word[i]==letter:
            list_of_dash[i]=letter
            print(stages[life])
    
    if letter not in random_word:
        life=life-1
        print(stages[life])
    if life==0:
            print("You loose")
            break
        # print("No match")
    # type: ignore # type: ignoreprint(list_of_dash)
    print(list_of_dash)
    
    if "_" not in list_of_dash:
        game_is_end=True
        print("YOU WIN")