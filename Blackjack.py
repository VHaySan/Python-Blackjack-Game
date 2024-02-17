
import random

#gobal variable
#using tuples because the variable never changes
suits = ('Diamonds', 'Hearts', 'Clubs', 'Spades')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

#using a dictionaries
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight' :8, 'Nine': 9, 'Ten' :10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
 
class Card:
    #when you get the card, only two info you get
    def __init__(self, suit, rank) -> None :
        self.suit = suit
        self.rank = rank

    #string, print out. speacial method
    def __str__(self) -> str:
        return self.rank + ' of' + self.suit 

#make a class to deal with the card, e.g shuffle the card, it needs multiple card and deal the card
class Deck:
    def __init__(self) -> None:
        self.deck = list()
        #append things to the list using loop
        #loop to get full desk of card and add to the list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank)) 
    
    #print what is stored in the instance
    def __str__(self) -> str:
        deck_check = '' #empty string
        for card in self.deck:
            deck_check += '\n ' + card.__str__()
        return 'The deck you are using has:' + deck_check
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self) :
        single_card = self.deck.pop()
        return single_card

class hand:
    #invidual hand for deal and player
    #player starts with no hand
    #how many ace does the player have because it can be 1 or 11 depending on the value
    #add card to hand, stand or hit
    
    def __init__(self) -> None:
        #when the hand is empty when game start
        self.cards = list()
        self.value = 0   
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        #access the gobal variable values
        self.value += values[card.rank]
        #check if the hand have ace, wither make it 1 or 11
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self) :
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    

#tracking chip count and placing a bet
class ChipAccount:
    def __init__(self) -> None:
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet   
    
    def lose_bet(self):
        self.total -= self.bet 

    def take_bet(chips):
        while True:
            try:
                chips.bet = int(input('Place your bet! How many chips? '))

            except ValueError:
                print('you must enter an integer!')
            
            else:
                if chips.bet > chips.total:
                    print('You dont have enough chips. you only have', chips.total)
                else:
                    break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input("Would you like to hit or stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print('Player stands. Dealer is playing')
            playing = False
        else:
            print('Sorry, please try again')
            continue
        break