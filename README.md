# Simplified Poker Game ![image](https://github.com/user-attachments/assets/8f1ca9cd-7acb-41c5-a177-e4ec2ced9cb8)


This project implements a simplified version of the popular card game Poker. The game allows players to engage in different Poker scenarios, including identifying various hands like Straight Flush, Four of a Kind, Full House, and more. The project also features a specialized Texas Hold'em variant.

## Features

- **Deck of Cards:** Automatically shuffles and deals cards to players and the table.
- **Hand Evaluation:** Determine the strength of a player's hand by checking for:
  - Straight Flush
  - Four of a Kind
  - Full House
  - Flush
  - Straight
  - Three of a Kind
  - Two Pairs
  - One Pair
  - High Card (default if no other hand is formed)
- **Texas Hold'em Variant:** Simulates a game where each player is dealt two cards, and five community cards are laid on the table. The best possible five-card hand is determined from the seven cards available to each player.

## Classes & Methods

- **PokerGame Class**
  - `__init__(self, num_players=2)`: Initializes the game with the specified number of players, shuffles the deck, and prepares player hands and the table.
  - `add_card(self, player_index)`: Adds the top card from the deck to the specified player's hand.
  - `add_to_table(self)`: Adds the top card from the deck to the table.
  - Various methods to evaluate Poker hands, e.g., `IsStraightFlush`, `IsFourofaKind`, `IsFullHouse`, etc.

- **TexasHoldem Class** (inherits from `PokerGame`)
  - `__init__(self, num_players=2)`: Initializes the Texas Hold'em game.
  - `deal(self)`: Deals two cards to each player and five community cards to the table.
  - `hands(self)`: Evaluates the best possible hand for each player.
