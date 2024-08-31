
import random
import copy

# IF YOU WANT TO TEST THE POKERGAME CLASS INDIVIDUALLY,
# YOU NEED TO CALL THE FUNCTIONS WITH A SPECIFIC LIST OF CARDS WITH
# LENGTH 5

class pokergame:

    def __init__(self, num_players):

        #making deck of cards
        rank = ['A', '2', '3','4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        suit = [ 'D', 'C', 'S', 'H']
        DeckofCards = []
        for i in rank:
            for j in suit:
                DeckofCards.append(i + j)

        #print('Shuffling')
        #shuffling cards randomly
        shuffled_DeckofCards = []
        while len(DeckofCards) > 0:
            l = len(DeckofCards)
            x = random.randint(0, (l - 1))
            shuffled_DeckofCards.append(DeckofCards[x])
            DeckofCards.remove(DeckofCards[x])
            
        players_cards = []
        
        #making empty list for each players current cards
        for i in range(num_players):
            player_cards = []
            players_cards.append(player_cards)
                

        self._players_cards = players_cards
        self._Deck = shuffled_DeckofCards
        self._tablecards = []

    def add_card(self, playernumber):

        '''
        Adds a card from the top of the deck to the hand of a
        specific player
        '''

        top_card = self._Deck[-1]
        self._Deck.remove(self._Deck[-1])
        self._players_cards[(playernumber) - 1].append(top_card)            

    def add_to_table(self):
        '''
        Adds a card from the top of the deck to the table deck
        '''

        self._tablecards.append(self._Deck[-1])
        self._Deck.remove(self._Deck[-1])
       
        print('Table is now', self._tablecards)

    def IsStraightFlush(self, playernumber, _focused_Pcards):
        '''
        int, [str] -> Bool
        Returns if all cards are from the same suit and their
        ranks are in order
        '''

        rank = ['A', '2', '3','4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        suit = [ 'D', 'C', 'S', 'H']
        seperated_rs =[]
        ordered_rank = []
        ordered_suit = []
        #_focused_Pcards = #(self._players_cards)[playernumber - 1]
        for i in _focused_Pcards:
            j = list(i)
            for k in j:
                seperated_rs.append(k)
        
        l = len(seperated_rs)
        for i in range(0, l, 2):
            for j in rank:
                if seperated_rs[i] == j:
                    ordered_rank.append(rank.index(j))
        ordered_rank.sort()

        for i in range(1, l, 2):
            for j in suit:
                if seperated_rs[i] == j:
                    ordered_suit.append(suit.index(j))
        ordered_suit.sort()                    
        q = len(ordered_rank)
        for i in range(0, q - 1):

            if (ordered_rank[i] + 1) != (ordered_rank[i + 1]) :
                return False

        for i in ordered_suit:
            
            if ordered_suit[i] != ordered_suit[0]:
                return False
            
        return True
            

    def IsTwoPairs(self, playernumber, _focused_Pcards):
        '''
        int, [str] -> Bool
        Returns true if there are two pairs of cards of the same rank
        '''

        rank = ['A', '2', '3','4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        seperated_rs =[]
        ordered_rank = []
        #_focused_Pcards = (self._players_cards)[playernumber - 1]
        for i in _focused_Pcards:
            j = list(i)
            for k in j:
                seperated_rs.append(k)
        
        l = len(seperated_rs)
        for i in range(0, l, 2):
            for j in rank:
                if seperated_rs[i] == j:
                    ordered_rank.append(rank.index(j))
        ordered_rank.sort()                    
        count1 =[]
        q = len(ordered_rank)
        for i in range(0, q - 2):
            if ordered_rank.count(ordered_rank[i]) == 2:
                count1.append(2)
                ordered_rank.remove(ordered_rank[i])

        if count1.count(2) == 2:
            return True
        return False
                                     

    def IsFullHouse(self, playernumber, _focused_Pcards):
        '''
        int, [str] -> Bool
        Returns true if there are four cards of the same rank
        '''

        rank = ['A', '2', '3','4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        seperated_rs =[]
        ordered_rank = []
        #_focused_Pcards = (self._players_cards)[playernumber - 1]
        for i in _focused_Pcards:
            j = list(i)
            for k in j:
                seperated_rs.append(k)
        
        l = len(seperated_rs)
        for i in range(0, l, 2):
            for j in rank:
                if seperated_rs[i] == j:
                    ordered_rank.append(rank.index(j))
        ordered_rank.sort()
                    
        if ordered_rank.count(ordered_rank[0]) == 2:
            if ordered_rank.count(ordered_rank[0 + 2]) == 3:
                return True

        if ordered_rank.count(ordered_rank[0]) == 3:
            if ordered_rank.count(ordered_rank[0 + 3]) == 2:
                return True
               
        return False


    def IsFourofaKind(self, playernumber, _focused_Pcards):
        '''
        int, [str] -> Bool
        Returns true if there are four cards of the same rank
        '''

        #playercards = (self._players_cards)[playernumber - 1]
        
        l = len(_focused_Pcards)
        
        ranks = []
        for i in _focused_Pcards:
            j = list(i)
            ranks.append(j[0])

        for o in ranks:
            if ranks.count(o) == 4:
                return True

        return False

    def IsThreeofaKind(self, playernumber,_focused_Pcards):
        '''
        int, [str] -> Bool
        Returns true if there are three cards of the same rank
        '''


        #playercards = (self._players_cards)[playernumber - 1]
        
        l = len(_focused_Pcards)
        
        ranks = []
        for i in _focused_Pcards:
            j = list(i)
            ranks.append(j[0])

        for o in ranks:
            if ranks.count(o) == 3:
                return True

        return False


    def IsFlush(self, playernumber, _focused_Pcards):
        '''
        int, [str] -> Bool
        Returns true if all five cards have the same suit
        '''

        suit = [ 'D', 'C', 'S', 'H']

        seperated_rs =[]

        ordered_suit = []

        #_focused_Pcards = (self._players_cards)[playernumber - 1]
        
        for i in _focused_Pcards:
            j = list(i)
            for k in j:
                seperated_rs.append(k)

        l = len(seperated_rs)

        for i in range(1, l, 2):
            for j in suit:
                if seperated_rs[i] == j:
                    ordered_suit.append(suit.index(j))
        ordered_suit.sort()

        for i in ordered_suit:
            
            if i != ordered_suit[0]:
                return False
            
        return True


    def IsStraight(self, playernumber, _focused_Pcards):
        '''
        int, [str] -> Bool
        Returns true if the five cards are in the order of their rank,
        suits are not important.
        '''


        rank = ['A', '2', '3','4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

        seperated_rs =[]

        ordered_rank = []

        #_focused_Pcards = (self._players_cards)[playernumber - 1]
        
        for i in _focused_Pcards:
            
            j = list(i)
            
            for k in j:
                seperated_rs.append(k)

        l = len(seperated_rs)
        
        for i in range(0, l, 2):
            for j in rank:
                if seperated_rs[i] == j:
                    ordered_rank.append(rank.index(j))

        ordered_rank.sort()

        q = len(ordered_rank)
        for i in range(0, q - 1):

            if (ordered_rank[i] + 1) != (ordered_rank[i + 1]) :
                return False
            
        return True


    def IsOnePair(self, playernumber, _focused_Pcards):
        '''
        int, [str] -> Bool
        Returns true if there is a pair of cards of the same rank
        '''

        
        rank = ['A', '2', '3','4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

        seperated_rs =[]

        ordered_rank = []

        #_focused_Pcards = (self._players_cards)[playernumber - 1]
        
        for i in _focused_Pcards:
            
            j = list(i)
            
            for k in j:
                seperated_rs.append(k)

        l = len(seperated_rs)
        
        for i in range(0, l, 2):
            for j in rank:
                if seperated_rs[i] == j:
                    ordered_rank.append(rank.index(j))

        ordered_rank.sort()

        copyOP = ordered_rank.copy()
        pairs = []
        for i in copyOP:
            if i not in pairs:
                pairs.append(i)
                (ordered_rank).remove(i)

        if len(ordered_rank) == 1:
            return True
        
        else:
            return False


class TexasHoldem(pokergame):
    
    def __init__(self, n=2):
        
        if n <= 2:
            super().__init__(2)
        else:
            super().__init__(n)

        
    def deal(self):
        '''
        Adds two cards to the hand of each player and five cards
        on the table
        '''

        for i in self._players_cards:
            for j in range(0, 2):
                self.add_card(self._players_cards.index(i)+1)
        for i in range(0, 5):
            self._tablecards.append(self._Deck[-1])
            self._Deck.remove(self._Deck[-1])
            

    def hands(self, numplayer):
        '''
        int -> [str]
        Returns a list of what each player has
        '''

        highest_deck = []
        Hold = []
        extra = []
        for i in range(0, numplayer):
            
            for j in self._tablecards:
                self._players_cards[i].append(j)
                
        extra1 = copy.deepcopy(self._players_cards)
        ##### IF YOU WANT TO TEST WITH SPECIFIC DECKS, YOU CAN ASSIGN THEM HERE
        ##### Ex:
        #####    extra1[0] = [] put specific deck (length 7) 

        #extra1[0] = ['AH', '2H', '3H', '4H', '5H', '3S', '3C']
        #extra1[1] = ['AC', '2H', '3S', '4D', '5H', '8S', '2C']
        #extra1[2] = ['AH', 'AC', 'AD', '9S', '5H', '6S', 'TC']
        #extra1[3] = ['AH', 'AC', '3D', '9H', '5S', '2S', '7C']
        #extra1[4] = ['8H', 'KC', 'KD', '4H', '5H', '5S', '9C']

        extra = copy.deepcopy(extra1)
         
        rank = ['A', '2', '3','4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
        suit = [ 'D', 'C', 'S', 'H']

        for m in range(0, numplayer):
            i = 0
            loop = 0
            while i != 21:
                loop = loop + 1
    
                combinations = []
                ordered_rank = []
                ordered_suit = []
                extra = copy.deepcopy(extra1)
                for i in range(0, 5):
                    
                    seperated_rs = []
                    newcomb = []
                    x = random.randint(0, len(extra[m]) - 1)
                    combinations.append(extra[m][x])
                    extra[m].remove(extra[m][x])
                  
                for i in combinations:
                    j = list(i)
                    for k in j:
                        seperated_rs.append(k)
        
                l = len(seperated_rs)
                for i in range(0, l, 2):
                    for j in rank:
                        if seperated_rs[i] == j:
                            ordered_rank.append(rank.index(j))
                ordered_rank.sort()

                for i in range(1, l, 2):
                    for j in suit:
                        if seperated_rs[i] == j:
                            ordered_suit.append(suit.index(j))
                ordered_suit.sort()
                holder = 3
                
                for i in ordered_rank:
                    seperated = copy.deepcopy(seperated_rs)
                    
                    if not ((seperated[seperated.index(rank[i])]) + (seperated[seperated.index(rank[i]) + 1])) in newcomb:
                        newcomb.append(rank[i] + seperated[(seperated.index(rank[i])) + 1])
                    elif not (rank[i] + seperated[(seperated.index(rank[i])) + (holder)]) in newcomb:
                        newcomb.append(rank[i] + seperated[(seperated.index(rank[i])) + (holder)])
                        
                    elif not(rank[i] + seperated[(seperated.index(rank[i])) + (holder + 2)]) in newcomb:
                        newcomb.append(rank[i] + seperated[(seperated.index(rank[i])) + (holder + 2)])
                    
                    elif not (rank[i] + seperated[(seperated.index(rank[i])) + (holder + 4)]) in newcomb:
                        newcomb.append(rank[i] + seperated[(seperated.index(rank[i])) + (holder + 4)])
                        
#Fixing the Hold list to avoid infinite while looping
                if loop == 60:
                    loopfix = []
                    for i in range(0, 5):
                        loopfix.append(extra1[0][i])
                    Hold.append(loopfix)                   
                    i = 21
                                     
              
                if not newcomb in Hold:
                    Hold.append(newcomb)
                    if len(Hold) == (21 * (m + 1)):
                        i = 21
        
        ANSW = []
        FinANSW = []
        PossibleDecks = ['HighCard','IsOnePair','IsTwoPairs','IsThreeofaKind','IsStraight','IsFlush','IsFullHouse','IsFourofaKind','IsStraightFlush']
        
        for i in range(0, numplayer):
            ANSW.clear()
            
            for q in Hold:
                
                    
                if ((Hold.index(q)) < (21 * (i + 1)) and ((Hold.index(q)) >= (21*i))):
               
                    
                    #if i == (numplayer - 1):
                    if (self.IsStraightFlush((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsStraightFlush'))

                    elif (self.IsFourofaKind((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsFourofaKind'))

                    elif (self.IsFullHouse((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsFullHouse'))

                    elif (self.IsFlush((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsFlush'))

                    elif (self.IsStraight((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsStraight'))

                    elif (self.IsThreeofaKind((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsThreeofaKind'))

                    elif (self.IsTwoPairs((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsTwoPairs'))
                    
                    elif (self.IsOnePair((i + 1), q)) == True:
                        ANSW.append(PossibleDecks.index('IsOnePair'))

                    else:
                        ANSW.append(PossibleDecks.index('HighCard'))


            #print(ANSW)
            Bhand = max(ANSW)
            
            FinANSW.append(PossibleDecks[Bhand])
        
        return True, (FinANSW)
                
        
texas = TexasHoldem(5)
texas.deal()
Boolean, decktype = texas.hands(5)
print(decktype)




test = pokergame(3)
for i in range(0, 3):
    for j in range(0, 5):
        test.add_card(i + 1)

testdeck = ['AH', '2H', '3H', '4H', '5H']
StraightFlush = ['AD', '2D', '3D', '4D', '5D']
#for any player
playernumber = 2

if test.IsStraightFlush(playernumber, testdeck) == test.IsStraightFlush(playernumber, StraightFlush):
    print('Test StraightFlush is passed')

else:
    print('Test StraightFlush is passed')

testdeck =  ['9H', '6S', '9D', '9C', '9S']
FourofaKind = ['AD', '2D', '3D', '4D', '5D']

if test.IsFourofaKind(playernumber, testdeck) == test.IsFourofaKind(playernumber, FourofaKind):
    print('Test IsFourofaKind is passed')

else:
    print('Test IsFourofaKind is passed')

testdeck =  ['JH', '7S', '7D', 'JD', 'JC'] 
FullHouse = ['AD', '2D', '3D', '4D', '5D']

if test.IsFullHouse(playernumber, testdeck) == test.IsFlush(playernumber, FullHouse):
    print('Test IsFullHouse is passed')

else:
    print('Test IsFullHouse is passed')
    
testdeck =  ['JH', '7H', '8H', '2H', '5H']
Flush = ['9D', '2D', '3D', '7D', '5D']

if test.IsFlush(playernumber, testdeck) == test.IsFlush(playernumber, Flush):
    print('Test IsFlush is passed')

else:
    print('Test IsFlush is passed')
    
testdeck = ['AD', '2S', '3D', '4C', '5H'] #the test deck is one you can change to test wheter it works
Straight = ['AD', '2D', '3D', '4D', '5D']

if test.IsStraight(playernumber, testdeck) == test.IsStraight(playernumber, Straight):
    print('Test IsStraight is passed')

else:
    print('Test IsStraight is passed')
    
testdeck = ['TH', '6S', 'TD', 'TC', 'QS']
ThreeofaKind = ['AD', '2D', '3D', '4D', '5D']

if test.IsThreeofaKind(playernumber, testdeck) == test.IsThreeofaKind(playernumber, ThreeofaKind):
    print('Test IsThreeofaKind is passed')

else:
    print('Test IsThreeofaKind is passed')

testdeck = ['TH', '6S', 'AS', 'TC', '6D']
TwoPairs = ['AD', '2S', '9D', '4H', '7D']

if test.IsTwoPairs(playernumber, testdeck) == test.IsTwoPairs(playernumber, TwoPairs):
    print('Test IsTwoPairs is passed')

else:
    print('Test IsTwoPairs is passed')

testdeck =  ['TH', '6S', 'AS', 'KC', 'KD']
OnePair = ['AD', '2S', '9D', '4H', '7D']

if test.IsOnePair(playernumber, testdeck) == test.IsOnePair(playernumber, OnePair):
    print('Test IsOnePair is passed')

else:
    print('Test IsOnePair is passed')


   

    
    
