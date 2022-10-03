import deck
from my_list import MyList
import random
import time


def main():
    number_of_decks = 1
    bj = Blackjack(number_of_decks)
    bj.play()


class Blackjack:
    def __init__(self, num_of_decks):
        self.shoe = Shoe(num_of_decks)
        self.shoe.shuffle()
        self.player = Player("Player")
        self.dealer = Player("Dealer")

    def play(self):
        self.bet()
        self.deal()
        self._print_hidden_hands()
        if self.player.hand.total_value == 21:
            self.natural_twenty_one_settlement()
        else:
            self.player_turn()
            if self.player.is_bust():
                self.settle()
            else:
                self.dealer_turn()
                self.settle()

    def bet(self):
        pass

    def deal(self):
        self.player.new_hand(self.shoe)
        self.dealer.new_hand(self.shoe)

    def player_turn(self):
        # TODO handle splitting and doubling down
        print("--Player turn--")
        can_hit = True
        while can_hit:
            action = self.get_player_action()
            if action == "hit":
                self.hit(self.player)
                self._print_hidden_hands()
                can_hit = not self.player.is_bust()
            elif action == "stand":
                break
            else:
                raise Exception(Exception)

    def get_player_action(self):
        player_action = ""
        while player_action.lower() not in ["hit", "stand"]:
            player_action = input("What do you do: ")
        return player_action

    def dealer_turn(self):
        _print_line()
        _print_line()
        print("--Dealer turn--")
        self.dealer._print_revealed_hand()
        wait()
        while self.dealer.hand.total_value < 16:
            self.hit(self.dealer)
            self.dealer._print_revealed_hand()
        wait()
        if self.dealer.hand.total_value <= 21:
            print("Dealer stands")
        else:
            print("Dealer is bust")
        wait()

    def settle(self, winner=None):
        if winner is None:
            winner = self.winner()
        _print_line()
        self._print_revealed_hands()
        _print_line()
        print(f"{winner.name} won")

    def winner(self):
        if self.player.is_bust():
            return self.dealer
        elif self.dealer.is_bust():
            return self.player
        elif self.dealer.hand.total_value >= self.player.hand.total_value:
            return self.dealer
        else:
            return self.player

    def natural_twenty_one_settlement(self):
        if self.dealer.hand.total_value == 21:
            self.settle(self.dealer)
        else:
            self.settle(self.player)

    def hit(self, player):
        _print_line()
        print(f"{player.name} hits")
        player.hand.add_card(self.shoe.get_card())

    def _print_revealed_hands(self):
        _print_line()
        self.dealer._print_revealed_hand()
        self.player._print_revealed_hand()

    def _print_hidden_hands(self):
        _print_line()
        self.dealer._print_hidden_hand()
        self.player._print_revealed_hand()


class Player:
    def __init__(self, name):
        self.name = name
        self.set_hand([])

    def set_hand(self, hand):
        self.hand = Hand(hand)

    def new_hand(self, shoe):
        self.set_hand([shoe.get_card() for _ in range(2)])

    def is_bust(self):
        return self.hand.total_value > 21

    def _print_hidden_hand(self):
        print("<" + f"{self.name}" + ">")
        print(self.hand[0], "\n", "hidden", sep="")
        print(self.hand[0].value)
        print()

    def _print_revealed_hand(self):
        print("<" + f"{self.name}" + ">")
        print("\n".join([str(card) for card in self.hand]))
        print(self.hand.total_value)
        print()


class Hand(MyList):
    def __init__(self, card_list):
        super().__init__(card_list)
        self._update_total_value()

    def add_card(self, card):
        self.append(card)
        self._update_total_value()

    def _update_total_value(self):
        self.total_value = sum(card.value for card in self)

    def _print_total_value(self):
        print(self.total_value)


class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        if face in ["T", "J", "Q", "K"]:
            self.value = 10
        elif face == "A":
            self.value = 11
        else:
            self.value = int(face)

    def __str__(self):
        return f"{self.face} of {self.suit}"


class Shoe(MyList):
    def __init__(self, num_of_decks):
        super().__init__()
        for _ in range(num_of_decks):
            for face in deck.FACES:
                for suit in deck.SUITS:
                    self.append(Card(face, suit))

    def shuffle(self):
        random.shuffle(self)

    def get_card(self):
        return self.pop()


def _print_line():
    print("-" * 80)


def wait():
    time.sleep(1.5)


if __name__ == "__main__":
    main()
