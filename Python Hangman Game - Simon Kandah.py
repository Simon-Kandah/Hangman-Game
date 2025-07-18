import random
import time

#Asking the player's name to start off
hangman= print("Welcome To HANGMAN!!! ")
time.sleep(0.5)
name= input("What Is Your Name!? ")
time. sleep (0.25)
print("Hello,",name, "Lets Play HANGMAN!!! ")
print("\033[0;34;48n", )
#Asking If They Would Like To Read Instructions
time.sleep(1)
instructions= input("Would You Like To Read The Instructions? Enter Yes or No: ").strip()
if instructions=="yes":
    print("\033[0;34;48n", )
    time.sleep(0.5)
    print("You Will Be Required To Select A Category/Theme For Your Secret Word")
    time.sleep(2)
    print("Once You Chose The Theme You Like, The Program Will Give You The Word's Length.")
    time.sleep(2)
    print("Then You Will Be Granted A Certain Amount Of Guesses To Guess The SECRET WORD!!!")
    time.sleep(2)
    print("You Can Not Guess The Same Letter Twice. If You Get 10 Incorrect Letters The Hangman Will Be... Hanged")
    time.sleep(2)
    print("Dont Worry Though You Will Be Able To Play Again :)")
    if instructions== "no":
        getword()
print("\033[0;34;48n", )
time.sleep(1)
#Asking The Player To Select A Category
def getword():
    category= input("Okay! Please Select Which Category You Would Like: Animals, Countries Or Colours: ").lower().strip()
    if category== "animals":
        words1= ["monkey", "camel", "lion", "panther", "jaguar", "zebra", "penguin", "giraffe", "tiger", "cheetah", "dog", "lizard", "fish", "shark", "octopus", "koala",]
        return random.choice(words1)
    if category== "countries":
        words2= ["jordan", "canada", "sweeden", "australia", "nigeria", "new zealand", "russia", "america", "brazil", "argentina", "germany","france", "italy", "spain", "south africa", "england"]
        return random.choice(words2)
    if category== "colours":
        words3= ["red", "orange", "green", "blue", "purple", "black", "white", "grey", "brown", "pink", "turquoise", "yellow", "gold", "magenta", "violet", "navy"]
        return random.choice(words3)
#Function For Selected Hangman Visual
def draw(attempts):

    hangman = (
        """
                   -----
                   |   |
                   |   0
                   | /-+-\ 
                   |   | 
                   |   | 
                   |  | | 
                   |  | | 
                   |
                   --------
        """,
        """
                -----
                |   |
                |   0
                | /-+-\ 
                |   | 
                |   | 
                |  | | 
                |  | |
                |
                --------
         """,
        """
              -----
              |   |
              |   0
              | /-+-\ 
              |   | 
              |   | 
              |  | 
              |  | 
              |
              --------
        """,
        """
              -----
              |   |
              |   0
              | /-+-\ 
              |   | 
              |   | 
              |  |
              |
              |
              --------
        """,
        """
              -----
              |   |
              |   0
              | /-+-\ 
              |   | 
              |   | 
              |
              |
              |
              --------
       """,
        """
          -----
          |   |
          |   0
          | /-+-\ 
          |   | 
          |
          |
          |
          |
          --------
          """,
        """
               -----
               |   |
               |   0
               | /-+-\ 
               |
               |
               |
               |
               |
               --------
        """,
        """
              -----
              |   |
              |   0
              | /-+-
              |
              |
              |
              |
              |
              --------
        """,
        """
              -----
              |   |
              |   0
              |  -+-
              |
              |
              |
              |
              |
              --------
        """,
        """
             -----
             |   |
             |   0
             |
             |
             |
             |
             |
             |
             --------
        """,
        """
           -----
           |   |
           |
           |
           |
           |
           |
           |
           |
           --------
        """,)
    print("\033[0;34;48n",hangman[attempts])

def game():
    #Inputing Variables Required
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    word = getword()
    print("\033[0;34;48n", )
    print("This Word Contains", len(word), "Letters.")
    unsolvedWord = ["-"] * len(word)
    print(unsolvedWord)
    lettersGuessed = []
    attempts = 10
    correct = 0
    guessed = False

#Giving the player their game stats/ how much attempts left
    while guessed == False and attempts > 0:
        print("\033[0;34;48n", )
        time.sleep(0.5)
        print("You Have", attempts, "Attempts Left")

        #Asking player to guess a letter or the secret word
        guess = input("You Can Guess A Letter Or The Full Word- ").lower()
        for i in range(0, len(word)):
            if guess == word[i:i + 1]:
                unsolvedWord[i] = guess
        for i in range(0, len(word)):
            if unsolvedWord[i] == word[i:i + 1]:
                correct += 1

#If player guesses letter and gets word correct
        if correct == len(word):
            time.sleep(0.35)
            print("\033[0;34;48n", )
            print("You got it! The Word Was",word,"!!!")
            time.sleep(0.35)
            print("CONGRATS!!! You Guessed The Word!!!")
            lettersGuessed.append(word)
            break
        else:
            correct = 0

        # User Inputs A Letter Check To See If It Is In The Alphabet Or Already Been Guessed
        if len(guess) == 1:
            if guess not in alphabet:
                print("\033[0;34;48n", )
                print("You have Entered An Invalid Character!")
            elif guess in lettersGuessed:
                print("\033[0;34;48n", )
                print("You have Already Tried/Guessed This Letter")
                time.sleep(0.65)

                #Check to see if the letter the User inputed is in the word or not
            elif guess in word:
                print("\033[0;34;48n", )
                print("GREAT JOB, AMAZING!!! You have Guessed A Letter!!!")
                lettersGuessed.append(word)
            elif guess not in word:
                print("TRY AGAIN! This Word Does Not Contain This Letter.")
                draw(attempts)
                lettersGuessed.append(guess)
                attempts = attempts - 1

            if unsolvedWord == word:
                print("GOTTEM")

        # User Enters Full Word, Checks To See If Correct
        elif len(guess) == len(word):
            if guess == word:
                print("\033[0;34;48n", )
                print("You got it! The Word Was",word,"!!!")
                time.sleep(0.35)
                print("CONGRATS!!! You Guessed The Word!!!")
                time.sleep(1)
                guessed = True
                for i in range(0, len(word)):
                    unsolvedWord[i] = word[i]

#Giving the User encouragement :)
            else:
                print("\033[0;34;48n", )
                print("That Aint It Chief :(")
                print("\033[0;34;48n", )
                attempts = attempts - 1
                if attempts > 1:
                    time.sleep(0.35)
                    print("You Still Have Some Attempts Left KEEP GOING!")

        # Incase The Player Inputs Word Where The Letters Do Not Equal The Secret Word
        else:
            print("\033[0;34;48n", )
            print("You Must Of Made A Mistake! Make Sure The Word You Enter Equals The Letters In The Secret Word.")
            time.sleep(0.65)
        # Inputting Letters Guessed, Into The Hangman Blanks/Lines
        display = ''

        '''
        for letter in word:
            if letter in lettersGuessed:
                display = display + letter
            else:
                display = display + '-'
                '''
        print(unsolvedWord)
# Printing Out The Correct Secret Word
        if display == word:
            print("YOU GUESSED IT!!! The Secret Word Was", word)
            guessed = True
        elif attempts == 0:
            print("YOU GOT THE HANGMAN... HANGED!!! The Word Was", word, "Try Again If You Dare!!!")

    # Function For Player To Play Again
    def again():
        time.sleep(1)
        print("\033[0;34;48n", )
        answer = input("Would You Like To Play Again??? I Hope So :)  Enter Yes To Play Again Or No To End- ").strip()
        if answer == "yes":
            print("\033[0;34;48n", )
            game()
        else:
            pass

    again()


game()