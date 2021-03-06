suits = ['S', 'C', 'H', 'D']
rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []

def CreateDeck():
    deck.clear()
    
    for suitsIndex in suits:
        suitArray = []

        for rankIndex in rank:
            suitArray.append(rankIndex + suitsIndex)
        
        deck.append(suitArray)

def GetRankIndex(card):

    cardFound = False
    cardLocation = -1

    for cardIndex in deck[GetSuitIndex(card)]:
        cardLocation += 1
        if(cardIndex == card):
            return cardLocation
    
    return -1

def GetSuitIndex(card):

    suit = card[1]
    suitIndex = 0

    if suit == 'C':
        suitIndex = 1
    elif suit == 'H':
        suitIndex = 2
    elif suit == 'D':
        suitIndex = 3

    return suitIndex

def RemoveCard(card):
    
    if(GetRankIndex(card) == -1): return

    deck[GetSuitIndex(card)].pop(GetRankIndex(card))

def ThreeOfKind(cards):

    hasOut = False

    for targetCard in cards:
        counter = 0
        for indexCard in cards:
            if(targetCard == indexCard): continue
            
            targetRank = targetCard[0]
            indexRank = indexCard[0]

            if(targetRank == indexRank): counter += 1
    
        if(counter == 2): hasOut = True
    
    return hasOut
    

def CheckAllOuts(hand, table):

    TotalOuts = 0

    for suitIndex in deck:
        for rankIndex in suitIndex:
            cards = []
            cards.extend(hand)
            cards.extend(table)
            cards.append(rankIndex)
            if(ThreeOfKind(cards)): TotalOuts += 1

    print(TotalOuts)
            

def main():

    CreateDeck()

    ## Entering current hand
    print('Dealt cards')
    print('Example: 2 of Hearts = 2H or Jack of Club = JC')
    currentHand = []

    currentHand.append(input('Enter Your First Card: ').upper())
    currentHand.append(input('Enter Your Second Card: ').upper())

    ## Remove current hand from the deck
    for index in currentHand:
        RemoveCard(index)

    ## Entering the flop cards
    print('Flop')
    currentFlop = []

    currentFlop.append(input('Enter the first flop card: ').upper())
    currentFlop.append(input('Enter the second flop card: ').upper())
    currentFlop.append(input('Enter the third flop card: ').upper())

    ## Remove the flop cards from the deck
    for index in currentFlop:
        RemoveCard(index)
    
    CheckAllOuts(currentHand, currentFlop)
    

main()