suits = ['S', 'C', 'H', 'D']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []


def CreateDeck():
    deck = []
    
    for suitsIndex in suits:
        suitArray = []

        for cardsIndex in cards:
            suitArray.append(suitsIndex + cardsIndex)
        
        deck.append(suitArray)

def CheckCard(card):
    
    cardFound = False
    cardLocation = -1

    for cardIndex in deck[GetSuitIndex(card)]:
        cardLocation += 1
        if(cardIndex == card):
            return cardLocation
    
    return -1

def GetSuitIndex(card):
    suit = card[0]
    suitIndex = 0

    if suit == 'C':
        suitIndex = 1
    elif suit == 'H':
        suitIndex = 2
    elif suit == 'D':
        suitIndex = 3

    return suitIndex


def RemoveCard(card):
    
    if(CheckCard(card) == -1): return

    deck[GetSuitIndex(card)].pop(CheckCard(card))

    print(deck)

def main():
     CreateDeck()
     RemoveCard('D4')


main()