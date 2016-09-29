
                    


                                        HANGMAN GAME README
                           
					RUN THE GAME AS BELOW
						
					$python New_Hangman_Game.py



Pre-Requisites:

> This is simple Guess Word HangMan Game
> It uses Python 2.7.11 32bit 
> Please use Python 2.7.11 32 bit Interpreter to run the Script since we are using nltk Package
> It needs following packages to be setup for generating words from the wordnet
1. nltk
2. Supporting Package numpy
The installation steps can be found here:
 http://www.nltk.org/install.html#windows

Please make sure you download and install nltk module along numpy.
 
For Gui development we have used the in-built Tkinter Module
This allows to Draw Picture of Hangman as we play the Game.


						Application Class 


This is a class of Our Application which inherits Tkinter Frame Class
So that we have available features to develop Gui

The following Widgets are added to Frame
1. Main Frame Window Application
2. Button Frame - To Add Button for Each letter
3. Canvas - To Display the Hidden Word on Gui
4. Canvas - To Display Hangman Picture for Each wrong Attempt
5. How To Play Button - A Help Message Guiding to Play the Game
6. Quit -  Quit the Game
7. Play Again - Play the Game Again


 
                       COMPUTING HIDDEN WORD LOGIC  


 Steps:
          1. Obtain Wordlist from words.words(). 
		     This is available in nltk.corpus.words
          2. Generate a random no between 0 to length of WordList
          3. Compute a HiddenWord using that random no as index for Wordlist
          4. Intialize the Canvas to Add the hidden word in Frame
          5. Place the Canvas in the Frame
          6. Intialize Row for each letter in the word
          7. Traverse the HiddenWord
             a. Initialize the Canvas to Add letter
             b. For each letter in the HiddenWord Add text "__"
             c. Append the canvas_id_list to store the canvas_id of each letter
                this id will be used as index or location of letter in that Word,
                after it is guessed correctly by the Player
             d. Increment the row
          8. Add a label "Guess the Hidden Word" to Canvas



                        HANGMAN GAME LOGIC


 Steps:
          1. Convert the HiddenWord to Uppercase
          2. Set letterinwordflag to False . 
             This allows to decide whether the letter is found or not found in the HiddenWord
          3. Traverse the HiddenWord to search the letter
          4. a.If letter found in HiddenWord and Count of IncorrectGuess is 
		       greater than 0 then set letterinwordflag to True
             b.Update the Canvas Text to the Correct Letter
             c.Increment the Count for Correct Guess
             d.Change the State of Letter Button to Disable so that the Player is no longer able to select the same letter
          5. If letterinwordflag is set to False and Correct Count is within length of HiddenWord, 
		     which means the letter is not found 
             a. Draw Hangman Component for the corressponding incorrectcount
             b. Decrement the Count for IncorrectGuess
			 c. Disable the State of Letter Button so that the Player is no longer able to select the same letter
          6. Check if Player has Won
             a. if the Count of Correct Guess is equal to length of letter then
             b. Player has Won the Game. 
             c. Display Congratulations and the step to exit the game
          7. Check if Player has Lost the Game
             a. if the Count of Incorrect Guess is less than or equal to 0 then
             b. Player has Lost the Game.
             c. Display Lost the Game message along with the Correct Word.
             d. Mention steps to Exit



                     Draw HangMan Picture Logic


 Keep a Count of Incorrect Guesses and for each Incorrect Guess draw the component
 of HangMan
 Steps:
            1. If Count of Incorrect Guess is greater than 1
               a. Display the No of Tries Left and Encourage the Player to Try Again
            2. If Count of Incorrect Guess is equal to 1
               a. Display the message that the Player has no more tries left
            3. If Count of Incorrect Guess is 10
               a. Draw the horizontal line for the hangman post
            4. If Count of Incorrect Guess is 9
               a. Draw the vertical line for the post
            5. If Count of Incorrect Guess is 8
               a. Draw the basement line for the post
            6. If Count of Incorrect Guess is 7
               a. Draw the hangman line for the post
            7. If Count of Incorrect Guess is 6
               a. Draw the head of the torso 
            8. If Count of Incorrect Guess is 5
               a. Draw the torso of hangman 
            9. If Count of Incorrect Guess is 4
               a. Draw the right arm
            10.If Count of Incorrect Guess is 3
               a. Draw the left arm
            11.If Count of Incorrect Guess is 2
               a. Draw the left leg
            12.If Count of Incorrect Guess is 1
               a. Draw the right leg



                  POSSIBLE SCENARIOS FOR THE GAME

1. A PLAYER CAN READ INSTRUCTION OF GAME USING HOW_TO_PLAY
2. A PLAYER CAN KEEP GUESSING THE LETTER UPTO 10 Tries
3. ONCE THE TRIES ARE FINISHED AND STILL THE PLAYER SELECTS THE LETTER
   IT WILL KEEP DISPLAYING THE LOST GAME WINDOW AND NOTHING WILL BE UPDATED
4. IF A PLAYER HAS GUESSED THE WORD CORRECT AND STILL HE KEEPS SELECTING THE 
   LETTER THE WIN GAME WINDOW WILL BE DISPLAYED AND NOTHING WILL BE UPDATED
5. IF A PLAYER HAS LOST THE GAME AND THEN HE CLICKS THE CORRECT LETTERS
   THE LOST GAME WINDOW WILL GET DISPLAYED AND NOTHING WILL BE UPDATED
6. A PLAYER CAN QUIT THE GAME ANYTIME BY PRESSING QUIT BUTTON   
7. IF A PLAYER CLICKS PLAY AGAIN HE WE BE ABLE TO START THE GAME AGAIN
8. IF A PLAYER CLICKS QUIT HE IS OUT OF THE GAME GUI
9. IF A PLAYER CLICKS HOW TO PLAY HE WILL SEE INSTRUCTION TO PLAY THE GAME


