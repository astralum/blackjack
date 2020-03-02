import random
from sys import exit
from time import sleep


# Running this file in the command line allows you to play American Blackjack.
# Features:
# One card deck
# Dealer must stand on all 17 except soft 17.
# Double on any two cards, including split pairs.
# Split once
# No betting of money

def title():
    print(r"""
 _______   __         ______    ______   __    __
/       \ /  |       /      \  /      \ /  |  /  |
$$$$$$$  |$$ |      /$$$$$$  |/$$$$$$  |$$ | /$$/
$$ |__$$ |$$ |      $$ |__$$ |$$ |  $$/ $$ |/$$/
$$    $$< $$ |      $$    $$ |$$ |      $$  $$<
$$$$$$$  |$$ |      $$$$$$$$ |$$ |   __ $$$$$  \
$$ |__$$ |$$ |_____ $$ |  $$ |$$ \__/  |$$ |$$  \
$$    $$/ $$       |$$ |  $$ |$$    $$/ $$ | $$  |
$$$$$$$/  $$$$$$$$/ $$/   $$/  $$$$$$/  $$/   $$/
       _____   ______    ______   __    __
      /     | /      \  /      \ /  |  /  |
      $$$$$ |/$$$$$$  |/$$$$$$  |$$ | /$$/
         $$ |$$ |__$$ |$$ |  $$/ $$ |/$$/
    __   $$ |$$    $$ |$$ |      $$  $$<
   /  |  $$ |$$$$$$$$ |$$ |   __ $$$$$  \
   $$ \__$$ |$$ |  $$ |$$ \__/  |$$ |$$  \
   $$    $$/ $$ |  $$ |$$    $$/ $$ | $$  |
    $$$$$$/  $$/   $$/  $$$$$$/  $$/   $$/

""")

cards_value = {'♥A': 11, '♥2': 2, '♥3': 3, '♥4': 4, '♥5': 5, '♥6': 6, '♥7': 7, '♥8': 8, '♥9': 9, '♥10': 10, '♥J': 10, '♥Q': 10, '♥K': 10,
'♠A': 11, '♠2': 2, '♠3': 3, '♠4': 4, '♠5': 5, '♠6': 6, '♠7': 7, '♠8': 8, '♠9': 9, '♠10': 10, '♠J': 10, '♠Q': 10, '♠K': 10,
'♦A': 11, '♦2': 2, '♦3': 3, '♦4': 4, '♦5': 5, '♦6': 6, '♦7': 7, '♦8': 8, '♦9': 9, '♦10': 10,'♦J': 10, '♦Q': 10, '♦K': 10,
'♣A': 11, '♣2': 2, '♣3': 3, '♣4': 4, '♣5': 5, '♣6': 6, '♣7': 7, '♣8': 8, '♣9': 9, '♣10': 10, '♣J': 10, '♣Q': 10, '♣K': 10}

class Person:
    #__doc__
    """A class of people involved."""
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        self.ace_count = 0
        self.ace_11 = 0

        self.cards2 = []
        self.points2 = 0
        self.ace_count2 = 0
        self.ace_112 = 0

    def pick_card(self, card_deck): #don't I wish to replace which_cards with self.cards
        num = random.randint(0, len(card_deck)-1) #but because of split
        picked_card = card_deck[num]
        card_deck.remove(picked_card)
        #self.card.append(picked_card)
        self.cards.append(picked_card)

        if "A" in picked_card:
            self.ace_count += 1
            self.ace_11 += 1

        return picked_card

    def pick_card2(self, card_deck): #don't I wish to replace which_cards with self.cards
        num = random.randint(0, len(card_deck)-1) #but because of split
        picked_card = card_deck[num]
        card_deck.remove(picked_card)
        #self.card.append(picked_card)
        self.cards2.append(picked_card)

        if "A" in picked_card:
            self.ace_count2 += 1
            self.ace_112 += 1

        return picked_card

    def tally_points(self):
        self.points = 0
        self.ace_11 = self.ace_count

        for card in self.cards:
                self.points += cards_value[card]

        while self.points > 21:
            if self.ace_11 > 0:
                self.points -= 10
                self.ace_11 -= 1
                continue
            else:
                break
        self.ace_11 = self.ace_count
        return self.points

    def tally_points2(self):
        self.points2 = 0
        self.ace_112 = self.ace_count2
        for card in self.cards2:
            self.points2 += cards_value[card]

        while self.points2 > 21:
            if self.ace_112 > 0:
                self.points2 -= 10
                self.ace_112 -= 1
                continue
            else:
                break
        self.ace_112 = self.ace_count2
        return self.points2

    def dealer_tally_points(self, player):
        self.points = 0
        self.ace_11 = self.ace_count

        player_points = player.tally_points()
        player_points2 = player.tally_points2()

        for card in self.cards:
            if "A" in card: #set A = 1 first
                self.points += 1
                self.ace_11 -= 1
            else:
                self.points += cards_value[card]

        while ((self.points < player_points or (self.points < player_points2 and player_points2 > 0)) and self.ace_11 > 0):
            for card in self.cards:
                if "A" in card:
                    self.points += 10
                    self.ace_11 += 1

        while (self.points > 21 and self.ace_11 > 0):
            self.points -= 10
            self.ace_11 -= 1

        self.ace_11 = self.ace_count
        return self.points

    def check_blackjack(self): #Blackjack only applies to first two drawn cards, for both dealer and player. Not to split
        if ("A" in self.cards[0] and cards_value[self.cards[1]]==10) or (cards_value[self.cards[0]]==10 and "A" in self.cards[1]):
            return "Blackjack"
        else:
            return "No Blackjack"


def list_options(list):
    str = "Choose to "
    for i in range(0, len(list)):
        if i == len(list)-1:
            str += "or " + list[i] + "."
        else:
            str += list[i] + ", "
    print("")
    print(str)

def main():
    title()
    sleep(2)

    print("Dealer must stand on all 17 except soft 17.\nDouble on any two cards including split pairs.")
    sleep(1.8)
    ynans("\nStart? (y/n)", "You have started a game.", "Goodbye.")

    sleep(0.5)
    while True:
        #initialise
        cards = ['♥A', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
        '♠A', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K',
        '♦A', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦10','♦J', '♦Q', '♦K',
        '♣A', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K']
        dealer = Person("dealer")
        player = Person("player")

        print("")
        init_deal(cards, dealer, player)
        sleep(2.5)
        print("")
        ynans("Play again? (y/n)", "You have started a new round.", "Thanks for playing. Goodbye!")
        continue

def ynans(question, y, n):
    while True:
        print(question)
        ans = input("> ").lower()
        sleep(0.3)
        if ans in {"yes", "y", "yeah", "yea", "yah", "ya", "affirmative"}:
            print(y)
            sleep(2.5)
            break
        elif ans in {"no", "n", "nah", "nay", "never"}:
            print(n)
            exit()
        else:
            print("I do not understand.")
            continue

def init_deal(card_deck, dealer, player):
    """Draws initial cards for player and dealer, determines Blackjack and/or asks for insurance."""
    player.pick_card(card_deck) #player draws 2 cards
    player.pick_card(card_deck)

    dealer_upcard = dealer.pick_card(card_deck)
    dealer_holecard = dealer.pick_card(card_deck)

    print(f"You have drawn {player.cards[0]} and {player.cards[1]}.")
    print(f"You have {player.tally_points()} points.")
    sleep(2.5)

    print(f"The dealer has drawn {dealer_upcard} and a holecard.")
    sleep(2.25)

    #check for player Blackjack
    if player.check_blackjack() == "Blackjack":
        if dealer.check_blackjack() == "Blackjack": # both Blackjack, push
            print(f"Dealer holecard is {dealer_holecard}. Dealer Blackjack. Push.")
        else:
            print(f"Dealer holecard is {dealer_holecard}. Blackjack! You win!")
    else: #no player Blackjack
        if "A" in dealer_upcard:
            if dealer.check_blackjack() == "Blackjack":
                #ask for insurance
                while True:
                    insurans = input("Do you want insurance? (y/n)\n> ").lower()
                    sleep(0.3)
                    if insurans in {"yes", "y", "yeah", "yea", "yah", "ya", "affirmative"}:
                        print("You have insurance.")
                        sleep(1.7)
                        print(f"Dealer holecard is {dealer_holecard}.")
                        print("Dealer Blackjack. Break even.")
                        break
                    elif insurans in {"no", "n", "nah", "nay", "never"}:
                        print("You do not have insurance.")
                        sleep(1.7)
                        print(f"Dealer holecard is {dealer_holecard}.")
                        print("Dealer Blackjack. You lose!")
                        break
                    else:
                        print("I do not understand.")
                        continue
            else: # no dealer Blackjack
                #ask for insurance
                while True:
                    insurans = input("Do you want insurance? (y/n)\n> ").lower()
                    sleep(0.3)
                    if insurans in {"yes", "y", "yeah", "yea", "yah", "ya", "affirmative"}:
                        print("You have insurance.")
                        sleep(1.7)
                        print("Dealer does not have Blackjack. You lose your insurance.")
                        sleep(2.5)
                        player_action(card_deck, dealer, player)
                        break
                    elif insurans in {"no", "n", "nah", "nay", "never"}:
                        print("You do not have insurance.")
                        sleep(1.7)
                        print("Dealer does not have Blackjack. You do not lose insurance.")
                        sleep(2.5)
                        player_action(card_deck, dealer, player)
                        break
                    else:
                        print("I do not understand.")
                        continue
        else: #no player Blackjack, no A in dealer_upcard
            player_action(card_deck, dealer, player)

def player_action(card_deck, dealer, player):
    """Executes the player's action after the initial draw."""

    #check if can split
    options = ["hit (h)", "stand (s)"]
    options_extended = ["hit (h)", "stand (s)", "split", "double", "surrender"]
    if cards_value[player.cards[0]] == cards_value[player.cards[1]]: #can split
        while True: #1st round
            list_options(options_extended)
            ans = input("> ").lower()
            sleep(0.3)
            if ans == "surrender":
                print("You have surrendered.")
                to_check_points = False
                break

            elif ans in {"stand", "s"}:
                to_check_points = True
                dealer_action(card_deck, dealer, player)
                break

            elif ans == "double":
                to_check_points = True
                player.pick_card(card_deck)
                break

            elif ans in {"hit", "h"}:
                player.pick_card(card_deck)
                print(f"You have drawn {player.cards[-1]}.")
                player_points = player.tally_points()
                print(f"You have {player_points} points.")
                sleep(2.5)

                if player_points > 21:
                    print("You bust! You lose!")
                    break
                else:
                    player_hitstand(card_deck, dealer, player, "ydealer")
                    break

            elif ans == "split":
                player.cards2.append(player.cards[1]) #copy second card to list 2
                player.cards.remove(player.cards[1]) #remove second card from list 1

                print(f"In deck one, you have {player.cards[0]}.")
                sleep(1)
                player.pick_card(card_deck)
                print(f"You have drawn {player.cards[-1]} into deck one.")
                player_points = player.tally_points()
                print(f"You have {player_points} points in deck one.")
                sleep(2.5)

                #allow them to double
                options_extended.remove("split")
                options_extended.remove("surrender")
                while True:
                    list_options(options_extended)
                    ans = input("> ").lower()
                    sleep(0.3)
                    if ans in {"stand", "s"}:
                        to_check_points = True
                        break
                    elif ans == "double":
                        player.pick_card(card_deck)
                        print(f"You have drawn {player.cards[-1]}.")
                        player_points = player.tally_points()
                        print(f"You have {player_points} points.")
                        sleep(2.5)
                        if player_points > 21:
                            print("You bust! You lose!")
                            to_check_points = False #can't return here, will exit entire function
                            break
                        else:
                            to_check_points = True
                            break
                    elif ans in {"hit", "h"}:
                        player.pick_card(card_deck)
                        print(f"You have drawn {player.cards[-1]}.")
                        player_points = player.tally_points()
                        print(f"You have {player_points} points.")
                        sleep(2.5)

                        if player_points > 21:
                            print("You bust! You lose!")
                            to_check_points = False
                            break
                        else:
                            to_check_points = player_hitstand(card_deck, dealer, player, "ndealer")
                            break
                player_points = player.tally_points()
                sleep(1.5)

                #move on to deck 2
                print("")
                print(f"In deck two, you have {player.cards2[0]}.")
                sleep(1)
                player.pick_card2(card_deck)
                print(f"You have drawn {player.cards2[-1]}.")
                player_points2 = player.tally_points2()
                print(f"You have {player_points2} points.")
                sleep(2.5)

                while True:
                    list_options(options_extended)
                    ans = input("> ").lower()
                    sleep(0.3)
                    if ans in {"stand", "s"}:
                        to_check_points2 = True
                        break
                    elif ans == "double":
                        player.pick_card2(card_deck)
                        print(f"You have drawn {player.cards2[-1]}.")
                        player_points2 = player.tally_points2()
                        print(f"You have {player_points2} points.")
                        sleep(2.5)
                        if player_points2 > 21:
                            print("You bust! You lose!")
                            to_check_points2 = False
                            break
                        else:
                            to_check_points2 = True
                            break
                    elif ans in {"hit", "h"}:
                        player.pick_card2(card_deck)
                        print(f"You have drawn {player.cards2[-1]}.")
                        player_points2 = player.tally_points2()
                        print(f"You have {player_points2} points.")
                        sleep(2.5)

                        if player_points > 21:
                            print("You bust! You lose!")
                            to_check_points2 = False
                            break
                        else:
                            to_check_points2 = player_hitstand2(card_deck, dealer, player, "ndealer")
                            break
                player_points2 = player.tally_points2()
                sleep(2.5)

                #if both decks bust, no need to check dealer action
                if to_check_points == False and to_check_points2 == False:
                    pass
                else: #only one or not both decks bust
                    #dealer action
                    print(f"Holecard is {dealer.cards[1]}.")
                    sleep(2.5)
                    if dealer.check_blackjack() == "Blackjack":
                        print("Dealer Blackjack. You lose!") #drawing A and a 10 after split not considered Blackjack
                    elif dealer.check_blackjack() == "No Blackjack":
                        print(f"The dealer has {dealer.dealer_tally_points(player)} points.")
                        dealer_points = dealer.dealer_tally_points(player)
                        while dealer_points < 17:
                            dealer_drawn_card = dealer.pick_card(card_deck)
                            print(f"Dealer has drawn {dealer_drawn_card}.")
                            dealer_points = dealer.dealer_tally_points(player)
                            print(f"Dealer has {dealer_points} points.")
                            sleep(1.7)
                        #at this point, dealer's points >= 17
                        dealer_points = dealer.dealer_tally_points(player)
                        player_points = player.tally_points()
                        player_points2 = player.tally_points2()
                        if dealer_points> 21:
                            if to_check_points2 == False:
                                print("Dealer busts. Deck one wins!")
                            elif to_check_points == False:
                                print("Dealer busts. Deck two wins!")
                            else:
                                print("Dealer busts. Both decks win!")
                        else: #compare player and dealer's points
                            if to_check_points2 == False: #deck two busts, check deck one
                                if player_points > dealer_points:
                                    print("Deck one wins!")
                                elif player_points < dealer_points:
                                    print("Deck one loses!")
                                else:
                                    print("Deck one pushes.")
                            if to_check_points == False:
                                if player_points2 > dealer_points:
                                    print("Deck two wins!")
                                elif player_points2 < dealer_points:
                                    print("Deck two loses!")
                                else:
                                    print("Deck two pushes.")
                    else:
                        print("Error with determining if dealer Blackjack.")

            break

    else: #cannot split
        options_extended.remove("split")
        while True:
            list_options(options_extended)
            ans = input("> ").lower()
            sleep(0.3)
            if ans == "surrender":
                print("You have surrendered.")
                break

            elif ans in {"stand", "s"}:
                dealer_action(card_deck, dealer, player)
                break

            elif ans == "double":
                player.pick_card(card_deck)
                print(f"You have drawn {player.cards[-1]}.")
                player_points = player.tally_points()
                print(f"You have {player_points} points.")
                sleep(2.5)
                if player_points > 21:
                    print("You bust! You lose!")
                    break
                else:
                    dealer_action(card_deck, dealer, player)
                    break

            elif ans in {"hit", "h"}:
                player.pick_card(card_deck)
                print(f"You have drawn {player.cards[-1]}.")
                player_points = player.tally_points()
                print(f"You have {player_points} points.")
                sleep(2.5)

                if player_points > 21:
                    print("You bust! You lose!")
                    break
                else:
                    player_hitstand(card_deck, dealer, player, "ydealer")
                    break

def player_hitstand(card_deck, dealer, player, want_dealer_action):
    options = ["hit (h)", "stand (s)"]

    while True:
        list_options(options)
        ans = input("> ").lower()
        sleep(0.3)
        if ans in {"hit", "h"}:
            player.pick_card(card_deck) #+++
            print(f"You have drawn {player.cards[-1]}.") #last card of list
            player_points = player.tally_points()
            print(f"You have {player_points} points.")
            if player_points > 21:
                print("You bust! You lose!")
                return False
                break
            else:
                #to_check_points = True
                continue
        elif ans in {"stand", "s"}:
            if want_dealer_action == "ydealer":
                dealer_action(card_deck, dealer, player)
                break
            elif want_dealer_action == "ndealer":
                break
            else:
                print("Error in deciding dealer_action or not")
                break
        else:
            print("I do not understand.")
            continue

def player_hitstand2(card_deck, dealer, player, want_dealer_action):
    options = ["hit (h)", "stand (s)"]

    while True:
        list_options(options)
        ans = input("> ").lower()
        sleep(0.3)
        if ans in {"hit", "h"}:
            player.pick_card2(card_deck) #+++
            print(f"You have drawn {player.cards2[-1]}.") #last card of list
            player_points2 = player.tally_points2()
            print(f"You have {player_points2} points.")
            if player_points2 > 21:
                print("You bust! You lose!")
                return False
                break
            else:
                # to_check_points = True
                continue
        elif ans in {"stand", "s"}:
            if want_dealer_action == "ydealer":
                dealer_action(card_deck, dealer, player)
                break
            elif want_dealer_action == "ndealer":
                break
            else:
                print("Error in deciding dealer_action or not")
                break
        else:
            print("I do not understand.")
            continue

def dealer_action(card_deck, dealer, player):
    sleep(0.5)
    print(f"Holecard is {dealer.cards[1]}.")
    sleep(1)
    if dealer.check_blackjack() == "Blackjack":
        print("Dealer Blackjack. You lose!")
    elif dealer.check_blackjack() == "No Blackjack":
        print(f"The dealer has {dealer.dealer_tally_points(player)} points.")
        sleep(1.4)
        while dealer.dealer_tally_points(player) < 17:
            dealer_drawn_card = dealer.pick_card(card_deck)
            print(f"The dealer has drawn {dealer_drawn_card}.")
            print(f"The dealer has {dealer.dealer_tally_points(player)} points.")
            sleep(1.7)
        #at this point, dealer's points >= 17
        dealer_points = dealer.dealer_tally_points(player)
        player_points = player.tally_points()
        if  dealer_points> 21:
            print("The dealer busts. You win!")
        else: #compare player and dealer's points
            if player_points > dealer_points:
                print("You win!")
            elif player_points < dealer_points:
                print("You lose!")
            else:
                print("Push.")
    else:
        print("Error with determining if dealer Blackjack.")

if __name__ == "__main__":
    main()
