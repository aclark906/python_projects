words = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weaselwhale wolf wombat zebra'.split()
}



while True:
    
    import random
    wordKey = random.choice(list(words.keys()))

    # Second, randomly select a word from the key's list in the dictionary:
    wordIndex = random.randint(0, len(words[wordKey]) - 1)

    category = wordKey
    secret_word = words[wordKey][wordIndex]
    
    guesses = []
    correct_guesses = []
    misses = []
    misses_cnt = 0
    misses_max = 6

    hangman_pics = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
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
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    
    
    print('Let''s play Hangman!')
    print(hangman_pics[0])
    print('The category is ' + category)
    answer = ['_ ' for i in secret_word]
    answer_string = ''.join(answer)
    print(answer_string)
    if ''.join(answer) != secret_word:
        while misses_cnt < misses_max:
            guess = input('Guess a letter: ').strip().lower()
            if guess in guesses:
                 print("You already guessed that letter!")
            for index, letter in enumerate(secret_word):
                if guess in letter:
                    answer[index] = guess
                    correct_guesses.append(guess)
                    guesses.append(guess)
                if guess not in secret_word:
                    if len(guess) == 1 and guess.isalpha() is True and guess not in guesses:
                        misses.append(guess)
                        guesses.append(guess)
                        misses_cnt = misses_cnt + 1
                        print('Incorrect!')
                        print(hangman_pics[misses_cnt])
                    if len(guess) > 1:
                        print("Please enter a single LETTER only.")
                        break
                    if guess.isalpha() is False:
                        print("That is not a letter.")
                        break
            print(''.join(answer))
            misses_cnt = len(list(set(misses)))
            print("Guesses: ", list(set(correct_guesses)))
            print("Misses: ", list(set(misses)))
            if ''.join(answer) == secret_word:
                print("Game over, you win!")
                break
        else:
            print("Game over, you lose! The word was " + secret_word.upper() + '.')

    play_again = str(input("Do you want to play again (y/n)? ").strip().lower())
    if play_again == 'y':
        continue
    else:
        print('Thanks for playing, goodbye!')
        break



###Need to figure out how to not ask twice if you want to play again when answer is n
###Need to figure out how to not ask to play again after n answer
###If possible, add back in 'Good guess!'. Currently lists multiple times if the letter is in the word multiple times.
###https://inventwithpython.com/invent4thed/chapter9.html
###Add a difficulty