from tkinter import *
from tkinter import messagebox
import wordle_template

root = Tk()
word = wordle_template.get_word()

Green = '#007d21'
Yellow = '#e2e600'
Black = '#000000'
White = '#FFFFFF'

root.config(bg=Black)

guessnum = 1

wordInput = Entry(root)
wordInput.grid(row=999, column=0, padx=10, pady=10, columnspan=3)

def getGuess():
    global word
    guess = wordInput.get()
    
    global guessnum
    guessnum += 1
    
    if guessnum <= 5:
        if len(guess) == 5:
            if word == guess:
                messagebox.showinfo("correct!", f"Correct! the word was {word.title()}")
            else:#incorrect
                for i, letter in enumerate(guess):
                    label = Label(root, text=letter.upper())
                    label.grid(row=guessnum, column=i, padx=10, pady=10)
                
                    if letter == word[i]:
                        label.config(bg =Green, fg=Black)
                
                    if letter in word and not letter == word[i]: #if letter is in word but not in right spot
                        label.config(bg=Yellow, fg=Black)
                    
                    if letter not in word:
                        label.config(bg=Black, fg=White)
                    
        else:
            messagebox.showerror('Use a five letter word')
    else:
        messagebox.showerror('Better luck next time!', f'Game over, The word was {word}')

wordguessbutton = Button(root, text="guess", command=getGuess)
wordguessbutton.grid(row=999, column=3, columnspan=2)


root.mainloop()