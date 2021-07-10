def hang():
    on = input('\nType "play" to play the game, "exit" to quit: ')
    while on:
        if on == "exit":
            break
        if on != "play" and on != "exit":
            on = input('\nType "play" to play the game, "exit" to quit: ')
            pass
        while on == "play":
           import random
           import string
           random.seed()
           lista = ['python', 'java', 'kotlin', 'javascript']
           word =(random.choice(lista))
           cont = 0
           word_ = len(word)
           s = ""
           abc = string.ascii_letters
           last = word_ * ['-']
           while cont <= 8:
                print()
                print("".join(last))
                user = input('Input a letter:')
                if len(user) != 1:
                    print("You should input a single letter")
                    continue
                if user != abc and user.islower() == False and len(user) == 1:
                    print('Please enter a lowercase English letter')
                    continue
                if s.count(str(user)) >= 1 and len(user) == 1:
                    print("You've already guessed this letter")
                    continue
                if cont < 8:    
                    if user not in word and s.count(str(user)) <= 1:
                        print("That letter doesn't appear in the word")
                        cont += 1
                        s += user
                    if user in word and s.count(user) <= 1:
                        s += user
                        for i in range(word_):
                            if word[i] == user:
                                last[i] = user
                    if '-' not in last:
                         print()
                         print("".join(last))
                         print('You guessed the word!')
                         print('You survived!')
                         return hang()
                if cont == 8:
                     if user not in word:
                         print('You lost!')
                         return hang()
print('H A N G M A N')
hang()