from game import Game

def main():
    # Define your board layout and player names
    board_layout = "HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH"
    player_names = ["Player 1", "Player 2"]

    # Create a Game instance
    game = Game(board_layout, player_names)

    # Game loop
    while True:
        # Display board and player positions
        game.display_board()

        # Display player statuses (balance and debt)
        game.display_status()

        # Roll the dice and move the player
        game.next_turn()

if __name__ == "__main__":
    main()
