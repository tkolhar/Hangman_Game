#!/usr/bin/env python 
'''
This is simple Guess Word HangMan Game
It uses Python 2.7.11 32bit 
It needs following packages to be setup for generating words from the wordnet
1. nltk
2. Supporting Package numpy
The installation steps can be found here:
 http://www.nltk.org/install.html#windows

For Gui development we have used the in-built Tkinter Module
This allows to Draw Picture of Hangman as we play the Game.
'''
import Tkinter as tk
from Tkinter import Tk
from nltk.corpus import words
from random import randint
import tkMessageBox
import sys

'''
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

'''
class Application(tk.Frame):
      '''
          Steps:
          1. Intialize the Frame with Width and Height
          2. Set Title of the Game
          3. pack_propagate -Setting the Flag so that Frame is of fixed size and not resizable
          4. pack() - Organizes the Frame Widget
          5. grid() - Place the Frame in Row,Column Format  
          6. Add the button frame to master frame 
          7. grid() - Place the button frame is row-column format
          8. Intialize the Count for Correct Guess
          9. Initialize the Count for Incorrect Guess
          10.Intialize the list of Canvas Id's to store the index of letter from HiddenWord
             (This index will be used to replace the "__" with the guessed letter)
          11. Call to Method which adds Buttons for each letter and Computes the HiddenWord from nltk.corpus.words module
          12. Call to Method placing the Quit Button in the Frame
          13. Call to Method placing the Play Again Button in the Frame
          14. Call to Method placing the How To Play Button in the Frame
      '''
      def __init__(self, master=None):
          tk.Frame.__init__(self, master, width=200, height=200)
          self.master.title("Hangman Game")       
          self.pack_propagate(False)
          self.pack()
          self.grid()
          self.correctcount = 0
          self.incorrectcount = 10
          self.canvas = tk.Canvas(self, width=2000, height=800)
          self.canvas.pack(side="top", fill="both", expand=True)
          self.buttonframe = tk.Frame(self.master)       
          self.buttonframe.grid(row=1, column=0, columnspan=100)
          self.canvas_id_list = []  
          self.displayLetters_And_computeHiddenWord(self.canvas)
          self.quitButton()
          self.newGameButton()
          self.howToPlayButton()
      
      '''
          This Method searches the Letter in the HiddenWord and Proceeds with the Game based on different scenarios
          Steps:
          1. Convert the HiddenWord to Uppercase
          2. Set letterinwordflag to False . 
             This allows to decide whether the letter is found or not found in the HiddenWord
          3. Traverse the HiddenWord to search the letter
          4. a.If letter found in HiddenWord and Count of IncorrectGuess is greater than 0 set letterinwordflag to True
             b.Update the Canvas Text to the Correct Letter
             c.Increment the Count for Correct Guess
             d.Change the State of Letter Button to Disable so that the Player is no longer able to select the same letter
          5. If letterinwordflag is set to False and Correct Count is within length of HiddenWord, which means the letter is not found
             a. Disable the Button so that the Player No long select the same letter 
             b. Draw Hangman Component for the corressponding incorrectcount
             b. Decrement the Count for IncorrectGuess
          6. Check if Player has Won
             a. if the Count of Correct Guess is equal to length of letter then
             b. Player has Won the Game. 
             c. Display Congratulations and the step to exit the game
          7. Check if Player has Lost the Game
             a. if the Count of Incorrect Guess is less than or equal to 0 then
             b. Player has Lost the Game.
             c. Display Lost the Game message along with the Correct Word.
             d. Mention steps to Exit 
        
      '''        
      def searchLetter(self, letter, hiddenWord, canvas, canvas_id_list, letterButton):
          hiddenWordupper = hiddenWord.upper()
          letterinwordflag = False
          letterButton.config(state = 'disabled')
          
          for i in range(0, len(hiddenWordupper)):
              if letter == hiddenWordupper[i] and self.incorrectcount > 0:
                 letterinwordflag = True 
                 canvas.itemconfig(canvas_id_list[i], text = letter)
                 self.correctcount +=1
                
          if not letterinwordflag and self.correctcount != len(hiddenWordupper):
                 self.hangmanPic(self.incorrectcount, canvas)
                 self.incorrectcount -= 1 

          if self.correctcount == len(hiddenWordupper):
             self.winGame(canvas,hiddenWordupper)
          if self.incorrectcount <= 0:
             self.loseGame(canvas,hiddenWordupper)
        
      '''
          Method to display Winner Message    
      '''
      def winGame(self, canvas, word):          
          tkMessageBox.showinfo("Congratulation !!", "You WIN! The word was " + word + " !\n" + "Press Quit to exit\n"+ " OR \nPress Play Again to start a New Game\n")

      '''
          Method to display Loser Message 
      '''
      def loseGame(self, canvas, word):
          tkMessageBox.showinfo("Sorry", "Game Over The word was " + word + "!\n" + "Press Quit to exit\n"+ " OR \nPress Play Again to start a New Game")

      '''
            This Method Draws each Component in Case of an Incorrect Guess
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
      '''
      def hangmanPic(self,incorrectcount, canvas):
          if incorrectcount > 1:
             tkMessageBox.showinfo("Tries Left","Come on Keep guessing you have " + str(incorrectcount-1) + " tries left")
          if incorrectcount == 1:
             tkMessageBox.showinfo("Tries Over", "Sorry You have no more tries left")
          if incorrectcount == 10:
             canvas.create_line(25, 50, 128, 50, width = 5.0)
          if incorrectcount == 9:
             canvas.create_line(25, 50, 25, 170, width = 5.0)
          if incorrectcount == 8:
             canvas.create_line(0, 170, 128, 170, width = 5.0)  
          if incorrectcount  == 7:           
             canvas.create_line(128, 50, 128, 75, width = 5.0)
          if incorrectcount == 6:
             canvas.create_oval(170, 75, 90, 95, width = 3.0)
          if incorrectcount == 5:
             canvas.create_line(128, 95, 128, 140, width = 5.0)
          if incorrectcount == 4:
             canvas.create_line(128,95,150,110,width = 5.0)
          if incorrectcount == 3:
             canvas.create_line(128,95,100,110, width=5.0) 
          if incorrectcount == 2:
             canvas.create_line(128,140, 100,155, width=5.0)
          if incorrectcount == 1:
             canvas.create_line(128,140,150,155, width=5.0)  
  
      '''
          Display Instructions to Play the Game
      '''
      def howToPlay(self):
          tkMessageBox.showinfo("Welcome to Hangman Game", "This is a word guess game\n Our Computer Brain has generated a word for you\nPlease Click on Alphabets in the Grid to Guess the word\n Each time you select a wrong letter we are going Complete the Hangman Picture. So BEWARE Try to guess Correct letter\n Have Fun\n")

      '''
          Add the How to Play Button to the Frame
          Steps:
          1. Intialize the help frame
          2. Place the help frame in row-column format
          3. Add the Button to frame with Text "How to Play" on it
          4. Place the button in row-column format
          5. Call to method on Button Click Event 
      '''
      def howToPlayButton(self):
          self.helpframe = tk.Frame(self.master)
          self.helpframe.grid(row=2,column=0,columnspan=100)
          helpbutton = tk.Button(self.helpframe, text = "How to Play")
          helpbutton.grid(row =0, column = 0)
          helpbutton.config(command=lambda:self.howToPlay()) 
         
      '''
          This Method Compute the HiddenWord from the list of Words from nltk.corpus.words.words() and also
          Add the grid of buttons for each letter in the Frame
          Steps:
          1. Obtain Wordlist from words.words()
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
          10. Intialize the list of letters upto [A-Z]
          11. Traverse the list of letters
              a. Intialize and Add a Button for each the letter
              b. Place each button in row-column format
              c. Set the Method to be Called on Click Event of the Button  
      '''
      def displayLetters_And_computeHiddenWord(self, canvas):
          word_list = words.words()   
          index = randint(0,len(word_list))
          hiddenWord = word_list[index]  
          self.canvas = canvas
          rowx = 10
          for i in range(0, len(hiddenWord)):
              canvas_id = canvas.create_text(rowx, 10, anchor="nw")
              canvas.itemconfig(canvas_id, text="__")
              self.canvas_id_list.append(canvas_id)         
              rowx = rowx + 10
          canvas_id_label = canvas.create_text(10, 25, anchor = "nw")  
          canvas.itemconfig(canvas_id_label, text="Guess the Hidden Word\n")
          letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
          for index in range(0, len(letters)):
              n = letters[index]
              letterButton = tk.Button(self.buttonframe, text = n)
              letterButton.grid(row = 0, column = index)    
              letterButton.config(command=lambda n=n,hiddenWord=hiddenWord,canvas=canvas, canvas_id_list=self.canvas_id_list, letterButton=letterButton:self.searchLetter(n, hiddenWord,canvas, canvas_id_list, letterButton))     

      '''
          Play Again - Start the Game with New Letter
      '''  
      def newGame(self): 
          self.correctcount = 0
          self.incorrectcount = 10
          self.canvas_id_list = []  
          self.canvas.destroy()
          canvas = tk.Canvas(self, width=2000, height=800)
          canvas.pack(side="top", fill="both", expand=True)
          self.displayLetters_And_computeHiddenWord(canvas)
         
         
      '''
          Method to Intialize and Add Play Again Button to Frame
      '''
      def newGameButton(self): 
          self.newButton = tk.Frame(self.master)
          self.newButton.grid(row=4, column=0, columnspan = 100)        
          tk.Button(self.newButton, text = "Play Again",command = lambda:self.newGame()).grid(row = 0, column = 0)
      
      '''
          Display the Message before Quitting the Game
      '''  
      def quitNow(self):
          tkMessageBox.showinfo("Hangman in Python, by Tazimbanu Kolhar", "Thanks for playing! See you soon!")
          sys.exit()

      '''
          Method to Intialize and Add Quit Button to Frame
      '''
      def quitButton(self): 
          self.buttonQuit = tk.Frame(self.master)
          self.buttonQuit.grid(row=3, column=0, columnspan = 100)    
          tk.Button(self.buttonQuit, text = "Quit",command = lambda:self.quitNow()).grid(row = 0, column = 0)

# Create a Instance of Application and place a Call to Frame
app = Application()
app.mainloop() 
