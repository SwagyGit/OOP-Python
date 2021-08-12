#Global Variables
import random
suits = ['Hearts','Spades','Clubs','Diamonds']
ranks = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
values = {'Ace':0,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}

#Card Class
class Card():
    #Attribute to define a card
    def __init__(self,rank,suit,ace_value=0):
        
        self.rank = rank
        self.suit = suit
        #Condition to check if Ace and Assigning Ace value
        if self.rank == 'Ace':
            self.value = ace_value
        else:
            self.value = values[rank]
        
    #print function
    def __str__(self):
        return f"{self.rank} of {self.suit}"

 ##############################################
    # End of Card Class
    ################################################        

#Deck Class
class Deck():
    
    def __init__(self,ace_value=0):
        self.ace_value = ace_value
        self.all_cards = []
        #Creating card objects and making a list of 52 cards
        for s in suits:
            for r in ranks:
                deck_card = Card(r,s,ace_value)
                self.all_cards.append(deck_card)
    
    
    #For shuffling the cards         
    def shuffle_deck(self):
        random.shuffle(self.all_cards)
        
    #Remove one from the deck
    def deal_one(self):
        return self.all_cards.pop(0)

 ##############################################
    # End of Deck class
    ################################################



#Player class
class Player():
    #Attributes initiated
    def __init__(self,name,player_money):
        
        self.name = name
        self.player_cards = []
        self.ace_value = 0
        self.player_money = player_money
        #print(self.player_money)
        
    #When Player wins
    def player_win(self,player_money):
        self.player_money += player_money
        
    #When Player loses
    def player_lose(self,player_money):
        self.player_money -= player_money
    
        
    #Bet amount
    def bet_on(self,bet_amount):
        self.bet_amount = bet_amount
        if self.bet_amount <= 2:
            return 'Bet amount should be more than Rs.2'
        elif self.bet_amount > self.player_money/2:
            return 'Your account balance should be double the bet amount!'
        else:
            self.player_money -= self.bet_amount
            return 'Done'
        
        
    #Show his cards
    def __str__(self):        
        return "Player {} has bet for Rs.{} and now the player's available balance is Rs.{}!".format(self.name,self.bet_amount,self.player_money)

 ##############################################
    # End of Player Class
 ################################################



#Dealer Class
class Dealer():
    
    def __init__(self):
        self.dealer_cards = []
        self.dealer_money = 1200
        
    #When Dealer wins
    def dealer_win(self,money):
        self.dealer_money += money
    
    #When Dealer is busted
    def dealer_lose(self,money):
        self.dealer_money -= money

    #Show his cards
    def __str__(self):        
        return "Dealer's balance is Rs.{}!".format(self.dealer_money)
 
  ##############################################
    # End of Dealer Class
  ################################################       



################################################
# Game Setup
################################################
import time
def setup_game():
    
    amount_flag = True
    ace_flag = True
    bet_flag = True
    
    #Ask name from player
    player_name = input('Enter your name: ')

    #Ask amount from player
    while amount_flag:
        
        player_account = input('\nPlease enter money for the game: Rs.')
        #Validation for int
        if player_account.isdigit():
        
            player_account = int(player_account)
            amount_flag = False
            break
            
        else:
            #if it's not integer ask for input again
            print('Please enter digit.\n')
            #Time delay
            time.sleep(2)
            continue
    
     ##### End of while
    
    #Create Player object        
    new_player = Player(player_name,player_account)
    
    #Ask bet amount from player
    while bet_flag:
        
        bet_amount = input('\nPlease enter your bet: Rs.')
        #Validation for int
        if bet_amount.isdigit():
        
            bet_amount = int(bet_amount)
            
            #Set bet amount
            msg = new_player.bet_on(bet_amount)
            #Validation for bet limit
            if msg =='Done':
                print(new_player)
                bet_flag = False
                break
            else:
                print(msg)
                #Time delay
                time.sleep(2)
                continue
            
        else:
            #if it's not integer ask for input again
            print('Please enter digit.\n')
            #Time delay
            time.sleep(2)
            continue
            
    ##### End of while
    
    
    #Ask ace value from player
    while ace_flag:
        
        player_ace_value = input('\nPlease enter value for Ace(1 or 11): ')
        
        #Validation for int
        if player_ace_value.isdigit():

            player_ace_value = int(player_ace_value)
            #Validation for ace value range
            if player_ace_value == 1 or player_ace_value == 11:
                #Create new deck with ace value set by the player
                new_deck = Deck(player_ace_value)
                ace_flage = False
                break
            else:
                #ask for value again
                print('Sorry, unacceptable value. Please enter value 1 or 11\n')
                #Time delay
                time.sleep(2)
                continue
        else:
            #if it's not integer ask for input again
            print('Sorry, you have entered string. Please enter value 1 or 11\n')
            #Time delay
            time.sleep(2)
            
    #End of while   

    return new_player,new_deck,bet_amount
    
    ##############################################
    # End of setup function
    ################################################
    
################################################
# Game Starts now
################################################
import time
from IPython.display import clear_output

def start_game():
    
    #Setting up the game 
    new_player,new_deck,bet_amount = setup_game()
    
    #Variables to measure number of hit
    hit = 0
    player_card_score = 0
    dealer_card_score = 0
    
    #Flags for actions
    player_action = ''
    dealer_action = ''
    
      
    #Shuffle the deck
    print("\nGame Started!")
    #Time delay
    time.sleep(2)
    print("First, let's shuffle the Deck!")
    new_deck.shuffle_deck()
    #Time delay
    time.sleep(2)
    
    #Create Dealer Object
    dealer = Dealer()
    
    #Distribute the cards
    print("\n===================================")
    print("     1st time drawing card     ")
    print("===================================")
    #Time delay
    time.sleep(2)
    
    #Game begins
    for i in range(2):
        #Drawing cards for Player
        new_player.player_cards.append(new_deck.deal_one())
        #Drawing cards for dealer
        dealer.dealer_cards.append(new_deck.deal_one())
    
    
    #Showing the Cards for Player
    print(f"Player {new_player.name} is having:")
    print("-----------------    -----------------")
    print("|               |    |               |")
    print("|               |    |               |")
    print("|               |    |               |")
    print(f" {new_player.player_cards[0]}      {new_player.player_cards[1]}")
    print("|               |    |               |")
    print("|               |    |               |")
    print("|               |    |               |")
    print("-----------------    -----------------")
    
    #Showing the Cards for Dealer
    print(f"\nDealer is having:")
    print("-----------------    -----------------")
    print("|               |    |               |")
    print("|               |    |               |")
    print("|               |    |               |")
    print(f" {dealer.dealer_cards[0]}          FACE OFF")
    print("|               |    |               |")
    print("|               |    |               |")
    print("|               |    |               |")
    print("-----------------    -----------------")
    
    #Time delay
    time.sleep(3)
    
    ####### Player's turn starts now ############
    # Checking for BlackJack #
    if new_player.player_cards[0].rank == 'Ace' or new_player.player_cards[1].rank == 'Ace':
            if new_player.player_cards[0].value == 10 or new_player.player_cards[1].value == 10:
                
                print(f"{new_player.name} got BlackJack!")
                #Time delay
                time.sleep(1)
                print(f"Dealer is checking if he got a BlackJack too!")
                #Time delay
                time.sleep(3)
                
                #Checking for Dealer got BlackJack
                if dealer.dealer_cards[0].rank == 'Ace' or dealer.dealer_cards[1].rank == 'Ace':
                    if dealer.dealer_cards[0].value == 10 or dealer.dealer_cards[1].value == 10:
                        print(f"Dealer got BlackJack too!\nIt's a PUSH!")
                        new_player.player_win(bet_amount)
                        print(f"\nPlayer got the bet amount back. Now your total balance is Rs.{new_player.player_money}")
                        return
                        
                else:        
                    #When Dealer didn't get BlackJack          
                    print(f"{new_player.name} wins as Dealer didn't get BlackJack!")
                    new_player.player_win(bet_amount+100)
                    print(f"\nPlayer got the bet amount plus bonus. Now your total balance is Rs.{new_player.player_money}")
                    return
    
    # Not a BlackJack situation
    # Player's turn to take an action
    else:
        #Assigning the variable
        player_action_flag = True
        
        #Calculating Total Player Card Score
        for i in range(len(new_player.player_cards)):
            player_card_score += new_player.player_cards[i].value
            
        #Start While loop
        while player_action_flag:
            
            #increase the number of hit
            hit += 1 

            #Showing Total Cards Score for Player
            print("Player {}, your total card score is: {}".format(new_player.name,player_card_score))
            #Ask action from player
            player_action = input('\nYou want to Hit or Stay: ')

            #Validation for action value
            if player_action.capitalize() == "Hit":
                
                #Drawing cards for Player
                new_player.player_cards.append(new_deck.deal_one())
                #Adding score
                player_card_score += new_player.player_cards[-1].value
                
                #Showing the Cards for Player
                print(f"\nAfter {hit}th 'Hit', player {new_player.name} is having:")
                for i in range(len(new_player.player_cards)):
                    print("-----------------")
                    print("|               |")
                    print("|               |")
                    print(new_player.player_cards[i])
                    print("|               |")
                    print("|               |")
                    print("-----------------")
                #Time delay
                time.sleep(3)
                
                #Checking for Player Blust
                if player_card_score > 21:
                    print(f"\n{new_player.name} is BUSTED!\nYou lose!")
                    print(f"Dealer got the Bet amount!")
                    dealer.dealer_win(bet_amount)
                    #new_player.player_lose(bet_amount)
                    #Time delay
                    time.sleep(2)
                    print(f"\nNow the player's total balance is Rs.{new_player.player_money}")
                    player_action_flag = False
                    return
                else:
                    #When Player is not Busted
                    player_action_flag = True
                    continue             
                    
                    
            elif player_action.capitalize() == "Stay":
                print("\nPlayer declared Stay!!\nNow Dealer's turn to play.")
                player_action_flag = False
                #Time delay
                time.sleep(2)
                break
            else:
                print("\nUnacceptable input.\nPlease enter either 'Hit' or 'Stay'.")
                player_action_flag = True
                continue

    ####### Player's turn is over ############
    
    ####### Dealer's turn starts now ############
    #Checking for Dealer got BlackJack
    if dealer.dealer_cards[0].rank == 'Ace' or dealer.dealer_cards[1].rank == 'Ace':
        if dealer.dealer_cards[0].value == 10 or dealer.dealer_cards[1].value == 10:
            print(f"Dealer got BlackJack. Dealer wins!!")
            dealer.dealer_win(bet_amount)
            print("\nDealer got the bet amount.")
            print(dealer)
            #Time delay
            time.sleep(2)
            #new_player.player_lose(bet_amount)
            print(f"\nNow the player's total balance is Rs.{new_player.player_money}")
            return
    # Dealer's turn to take an action
    else: 
        #Assigning the variable
        dealer_action = 'Hit'
        
        #Calculating Total Dealer Card Score
        for i in range(len(dealer.dealer_cards)):
            dealer_card_score += dealer.dealer_cards[i].value
        
        #Start While loop
        while dealer_action == 'Hit':

            #Checking for Dealer Blust
            if dealer_card_score > 21:
                dealer_action == 'Busted'
                print(f"\nDealer is BUSTED!\n{new_player.name} wins!")
                new_player.player_win(bet_amount)
                print(f"\nPlayer got the bet amount. Now your total balance is Rs.{new_player.player_money}")
                return

            #When Dealer has card score of 17 or more
            elif dealer_card_score >= 17:
                dealer_action = 'Stay'
                print('\nDealer declared Stay!!')
                #Time delay
                time.sleep(2)
                break

            else:
                #When Dealer has card score of less 17
                print('Dealer declared Hit!!')
                #Drawing cards for Player
                dealer.dealer_cards.append(new_deck.deal_one())
                #Adding score
                dealer_card_score += dealer.dealer_cards[-1].value
                
                #Showing the Cards for Player
                print(f"\nAfter the 'Hit', Dealer is having:")
                for i in range(len(dealer.dealer_cards)):
                    print("-----------------")
                    print("|               |")
                    print("|               |")
                    print(dealer.dealer_cards[i])
                    print("|               |")
                    print("|               |")
                    print("-----------------")
                    
                #Time delay
                time.sleep(2)
                
    ####### Dealer's turn is over ############
    #When dealer is having greater score card
    if dealer_card_score > player_card_score:
        print(f"\nDealer score is {dealer_card_score} which is more so dealer wins!")
        dealer.dealer_win(bet_amount)
        print(dealer)
        #Time delay
        time.sleep(2)
        #new_player.player_lose(bet_amount)
        print(f"Player {new_player.name} loses!!\nNow the player's total balance is Rs.{new_player.player_money}")
        return
    
    #When both player and dealer are having same score card    
    elif dealer_card_score == player_card_score:
        print("\nIt's a PUSH!")
        #Time delay
        time.sleep(2)
        new_player.player_win(bet_amount)
        print(f"\nNow the player's total balance is Rs.{new_player.player_money}")
        return
        
    else:
        #When player is having greater score card
        print(f"\nPlayer {new_player.name}'s score is {player_card_score} which is more so player wins!!!")
        #Time delay
        time.sleep(2)
        new_player.player_win(bet_amount)
        print(f"\nNow the player's total balance is Rs.{new_player.player_money}")
        return
    
##############################################
    # End of start_game function
    ################################################
    
###################################################
#  Exit Decision function 
##################################################
def exit_game():
    # Flag for exit decision
    check_exit_flag = False
    # While loop starts
    while not check_exit_flag:
    	# Taking input from player
        exit_decision = input('\nDo you want to play again? [Y/N]: ')
        # Validation for digit
        if exit_decision.isdigit():
            print('Sorry, digit is not acceptable! Please enter Y or N')
        # Validation for correct letter
        elif exit_decision.upper() not in ['Y','N']:
            print('Sorry, Please enter Y or N')
        # When input is correct
        else:
            check_exit_flag = True
    # check for yes
    if exit_decision.upper() == 'Y':
       
        print("Let's play the game!")
        return 'Again'
    else:
       # check for no
        print('GAME OVER.\nWell played!')
        return 'Over'

###################################################
#  End of Exit Decision function 
##################################################

def start_button():

    play_flag = True

    # Calling start_game function
    start_game()

    while play_flag:
        # Calling exit_game function
        exit_decision = exit_game()

        if exit_decision == 'Again':
            start_game()
            play_flag = True
            continue

        elif exit_decision == 'Over':
            play_flag = False
            return

###################################################
#  End of start_button function 
##################################################

#Starting the game by calling start_button
start_button()
    ############### End of the Game ###################