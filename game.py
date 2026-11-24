import random

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


def create_deck():
    """Return a shuffled deck of 52 cards as (rank, suit) tuples."""
    deck = [(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def card_to_text(card):
    rank, suit = card
    return f"{rank} of {suit}"


def card_value(card):
    """Value of a single card. Aces count as 11 here; we fix that in hand_value."""
    rank = card[0]
    if rank in ("J", "Q", "K"):
        return 10
    if rank == "A":
        return 11
    return int(rank)


def hand_value(hand):
    """Total of a hand, counting Aces as 11 or 1 so the hand doesn't bust if possible."""
    total = sum(card_value(card) for card in hand)
    aces = sum(1 for card in hand if card[0] == "A")

    while total > 21 and aces > 0:
        total -= 10  # turn one Ace from 11 into 1
        aces -= 1

    return total


def hand_to_text(hand):
    return ", ".join(card_to_text(card) for card in hand)


def show_welcome():
    print("=" * 40)
    print("        WELCOME TO 21 (BLACKJACK)")
    print("=" * 40)


def show_rules():
    print()
    print("=" * 40)
    print("           HOW TO PLAY")
    print("=" * 40)
    print("GOAL")
    print("  Get a hand total closer to 21 than the dealer,")
    print("  without going over 21.")
    print()
    print("CARD VALUES")
    print("  2-10        : face value")
    print("  J, Q, K     : 10")
    print("  Ace         : 11 or 1, whichever helps your hand")
    print()
    print("EACH ROUND")
    print("  1. You and the dealer each get 2 cards.")
    print("  2. You see both of your cards, but only one dealer card.")
    print("  3. On your turn, type 'h' to Hit (take a card)")
    print("     or 's' to Stand (keep your total).")
    print("  4. If your total goes over 21, you Bust and lose.")
    print("  5. If you reach exactly 21, you stand automatically.")
    print("  6. Then the dealer reveals the hidden card.")
    print("     The dealer must hit until reaching 17 or more.")
    print()
    print("WINNING")
    print("  - Dealer busts            -> you win")
    print("  - Your total is higher    -> you win")
    print("  - Dealer's total is higher-> dealer wins")
    print("  - Same total              -> push (tie)")
    print()
    print("NOTES")
    print("  - This version has no betting, splitting or doubling.")
    print("  - A new shuffled deck is used for every round.")
    print("=" * 40)


def player_turn(deck, player_hand, dealer_hand):
    """Let the player hit or stand. Returns the final hand value."""
    while True:
        print()
        print("Dealer shows:", card_to_text(dealer_hand[0]), "and a hidden card")
        print("Your hand:   ", hand_to_text(player_hand), "->", hand_value(player_hand))

        if hand_value(player_hand) == 21:
            print("21! You stand automatically.")
            break

        choice = input("Hit or stand? (h/s): ").strip().lower()

        if choice == "h":
            card = deck.pop()
            player_hand.append(card)
            print("You drew:", card_to_text(card))

            if hand_value(player_hand) > 21:
                print()
                print("Your hand:   ", hand_to_text(player_hand), "->", hand_value(player_hand))
                print("Bust! You went over 21.")
                break
        elif choice == "s":
            print("You stand on", hand_value(player_hand))
            break
        else:
            print("Please type h or s.")

    return hand_value(player_hand)


def dealer_turn(deck, dealer_hand):
    """Dealer reveals the hidden card and hits until reaching 17 or more."""
    print()
    print("Dealer reveals:", hand_to_text(dealer_hand), "->", hand_value(dealer_hand))

    while hand_value(dealer_hand) < 17:
        card = deck.pop()
        dealer_hand.append(card)
        print("Dealer draws:  ", card_to_text(card), "->", hand_value(dealer_hand))

    return hand_value(dealer_hand)


def decide_winner(player_total, dealer_total):
    """Print the result of the round."""
    print()
    print(f"You: {player_total}   Dealer: {dealer_total}")

    if player_total > 21:
        print("You busted. Dealer wins.")
    elif dealer_total > 21:
        print("Dealer busted. You win!")
    elif player_total > dealer_total:
        print("You win!")
    elif player_total < dealer_total:
        print("Dealer wins.")
    else:
        print("It's a push (tie).")


def play_round():
    """Play one full round of 21."""
    deck = create_deck()

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    player_total = player_turn(deck, player_hand, dealer_hand)

    if player_total > 21:
        dealer_total = hand_value(dealer_hand)  # dealer doesn't need to play
    else:
        dealer_total = dealer_turn(deck, dealer_hand)

    decide_winner(player_total, dealer_total)


def main():
    show_welcome()

    while True:
        print()
        print("MENU:  [p] Play   [r] Rules   [q] Quit")
        choice = input("Choose: ").strip().lower()

        if choice == "p":
            play_round()
        elif choice == "r":
            show_rules()
        elif choice == "q":
            print("Thanks for playing. Goodbye!")
            break
        else:
            print("Please type p, r or q.")


if __name__ == "__main__":
    main()