import random


def drawCards(player, cards, num, deck):
    if len(deck) > (num + 1):
        for count in range(num):
            cards[0].append(deck.pop())
            deck[:] = deck
        return
    else:
        deck[:] = []
        return


def playerChance(cards, playedCards, deck):
    # the pack of the current player
    currentPack = cards[0]
    played = False
    drawFour = False

    # first play
    if not playedCards:
        playedCards.append(currentPack.pop(1))
        cards.append(cards.pop(0))
        if str(playedCards[-1][0]) != "10":
            print("Player " + str(currentPack[0]) + " played " + str(
                playedCards[-1][0]) + " of " + str(playedCards[-1][1]))
        else:
            print(
                "Player " + str(currentPack[0]) + " played draw 2 of " + str(playedCards[-1][1]))
        # case of draw 4 or draw 2
        if playedCards[-1][1] == "Draw 4":
            drawCards(cards[0][0], cards, 4, deck)
            drawFour = True
        elif playedCards[-1][1] == 10:
            drawCards(cards[0][0], cards, 2, deck)
        return True, cards, playedCards
    else:
        # card on top of the played cards
        currentCard = playedCards[-1]
        for myCard in range(1, len(currentPack)):
            if currentCard[0] == currentPack[myCard][0] or currentCard[1] == currentPack[myCard][1] or currentPack[myCard][1] == "Draw 4":
                # checking if the card is draw 2 or draw 4
                if currentPack[myCard][1] == 11:
                    drawCards(cards[0][0], cards, 2, deck)
                elif currentPack[myCard][1] == "Draw 4":
                    drawCards(cards[0][0], cards, 4, deck)
                    drawFour = True

                playedCards.append(currentPack.pop(myCard))
                cards.append(cards.pop(0))
                if str(playedCards[-1][0]) != "10":
                    print("Player " + str(currentPack[0]) + " played " + str(
                        playedCards[-1][0]) + " of " + str(playedCards[-1][1]))
                else:
                    print(
                        "Player " + str(currentPack[0]) + " played draw 2 of " + str(playedCards[-1][1]))
                played = True
                break

        if played == False:
            drawCards(cards[0][0], cards, 1, deck)
            cards.append(cards.pop(0))
            print("Player " + str(currentPack[0]) + " picked a card!")

    if drawFour:
        playedCards.append(deck.pop())
        drawFour = False

    # returning if the game is tied or won or it is still going on
    if len(cards[-1]) == 1 or len(deck) == 0:
        if len(deck) == 0:
            print("Game tied!", cards, deck)
        else:
            print("player ", str(currentPack[0]), " won the game!")
        return False, cards, playedCards
    else:
        return True, cards, playedCards


def playUNO(players, deck):
    cardsOnHand = []
    status = True
    playedCards = []

    # distributing cards to players
    for player in range(players):
        initArr = [player+1]
        for num in range(5):
            initArr.append(deck.pop())
        cardsOnHand.append(initArr)
    # always checking if any of the players have won
    while status:
        status, cardsOnHand, playedCards = playerChance(
            cardsOnHand, playedCards, deck)


def cardSetup(numOfPlayer):
    deck = []
    color = ["blue", "yellow", "green", "red"]

    # making cards from 0-9 with all the four colors. Card 11 is draw 2 of the color
    for col in range(0, len(color)):
        for num in range(0, 11):
            if num != 0:
                deck.append([num, color[col]])
            deck.append([num, color[col]])

    # adding four draw 4 cards to the mix
    for drawFour in range(0, 4):
        deck.append(["No Color", "Draw 4"])

    # Shuffle the card
    random.shuffle(deck)

    playUNO(numOfPlayer, deck)


def initGame():
    numOfPlayer = input("How many people will play the game?(2-6): ")
    if numOfPlayer != "" and int(numOfPlayer) >= 2 and int(numOfPlayer) <= 6:
        cardSetup(int(numOfPlayer))
    else:
        print("Please enter the valid number of players!")


def start():
    startOrNot = input("Should we start the game? (Y/N): ")
    if startOrNot == "Y" or startOrNot == "y":
        initGame()
    else:
        print("Thanks for playing!")


start()
