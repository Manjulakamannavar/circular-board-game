from game import Game


def main():
    board_layout = "HHBJHHHHJHHBHHHHBHHHJJHHHHHJHBH"
    player_names = ["Alice", "Bob"]
    game = Game(board_layout, player_names)

    while True:
        game.display_board()
        current_player = game.players[game.current_player_index]
        print(f"{current_player.name}'s turn:")
        game.next_turn()


if __name__ == "__main__":
    main()
