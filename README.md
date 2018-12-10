## boggle-solver
Command line Boggle board solver written in Python.

#### Usage
Start the program:

`python boggle.py`

This will load the English dictionary into memory. When it's done, it will print out instructions and wait for your input. When the program is waiting for input, you will see the following:

`>>`

To solve a board, enter a valid file path when the program prompts for input. For example, if you have a file called `test_board.txt` stored in a directory called `boards`:

`boards/test_board.txt`

To stop the program, enter the word exit:

`exit`

#### Expected Input
The program expects a text (`.txt`) file where:

* Every line is a row of the board
* Every line contains English letters separated by a single space
* Every line must contain the same number of letters
* There is no trailing space around lines
* There are no empty lines

#### Example Board File
```
c a t a
l p o o
i c k w
r a s a
```