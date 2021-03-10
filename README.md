# UNO Game
The above python code contains logic for the UNO cards game. The game consists of 4 colours *Blue*, *Red*, *Green* and *Yellow* ranging from cards 0-9. Each of the colours also contains two *Draw 2* cards each also we have support for *Draw 4*.

## How it works
### Run the code
To run the code and start the game
```
> python3 UNO.py
```
### Start the game or leave it
Enter **Y** to start the game or **N** to exit the game
```
> Should we start the game? (Y/N): Y
``` 
### Select the number of players 
Select total number of players atleat 2 players and atmost 6 players are allowed to play the game at once
```
> How many people will play the game?(2-6): 2 
```
### Automated game
Once you insert the total number of players now the python code takes care of the game. You will be able to see all the chances played on the screen.
```
Player 2 played 3 of red
Player 1 played 3 of yellow
Player 2 picked a card!
Player 1 played 7 of yellow
```

### Winner or Draw
The player to use up all the cards wins the game or if none of the players are able to use all the cards then the game is taken as a draw. 
```
player  1  won the game!
```
## Code insight
The whole code consists of 6 functions
* **start()** > This function asks if you want to start a game or leave it. This is the first function that is called in the whole game.
* **initGame()** >  This functions runs upon selecting **Y** and asks for the number of players playing the game.
* **cardSetup()** > Upon entering a number between *2* and *6* the game starts and in this function we setup the deck and randomize it with *random* lib in python.
* **playUNO()** > In this function we distribute *5* cards to each player.
* **playerChance()** > After distributing the cards we start to play the users one after the another in this function.
* **drawCards()** > The drawCards function takes care of *draw 2* or *draw 4* cards in the game.

## Authors
Aman Kumar