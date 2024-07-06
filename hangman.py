
import random
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
s = ['''
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
word=["hangman","python","office","microsoft","intel","google","claculator","palace","albert","aircraft","honda","cruise","submarine"]
lives=6
choose_word=random.choice(word)
print("Hint:",choose_word[0],"     ",choose_word[-1])
dis=[]
for _ in range(len(choose_word)):
    dis +=  "_"
endgame=True
while not endgame==False:
    guess=input("enter the letter:").lower()
    if guess in dis:
        print(f"you have already chosen:{guess}")
    for p in range(len(choose_word)):
        a=choose_word[p]
        if guess==a:
            dis[p]=guess
    print(dis)
    
    if guess not in choose_word:
        print("Wrong letter")
        lives=lives-1
        if lives==0:
            print("you lost")
            print(s[lives])
            break
    if "_" not in dis:
        endgame=True
        print("You got it")
        break

    print(s[lives])

    
    
    
    
    