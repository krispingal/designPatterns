class Command:
    def execute(self):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError

class MoveCommand(Command):
    def __init__(self, game_state, start_pos, end_pos):
        self.game_state = game_state
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.captured_piece = None

    def execute(self):
        if not self.is_valid_move():
            print("Invalid move!")
            return
        piece = self.game_state.board[self.start_pos[0]][self.start_pos[1]]
        self.captured_piece = self.game_state.board[self.end_pos[0]][self.end_pos[1]]
        self.game_state.board[self.start_pos[0]][self.start_pos[1]] = "."
        self.game_state.board[self.end_pos[0]][self.end_pos[1]] = piece
        print(f"Moved piece from {self.start_pos} to {self.end_pos}")

    def undo(self):
        piece = self.game_state.board[self.end_pos[0]][self.end_pos[1]]
        self.game_state.board[self.end_pos[0]][self.end_pos[1]] = self.captured_piece if self.captured_piece else "."
        self.game_state.board[self.start_pos[0]][self.start_pos[1]] = piece
        print(f"Undid move from {self.end_pos} to {self.start_pos}")

    def is_valid_move(self):
        return True

class GameState:
    def __init__(self):
        self.board = [["."] * 8 for _ in range(8)]
        self.history = []

    def display(self):
        for row in self.board:
            print(" ".join(row))
        print("\n")

    def make_move(self, move_command: MoveCommand):
        move_command.execute()
        self.history.append(move_command)

    def undo_move(self):
        if self.history:
            last_move = self.history.pop()
            last_move.undo()

if __name__ == '__main__':
    game_state = GameState()
    game_state.board[0][0] = "R"  # Rook
    game_state.board[0][1] = "N"  # Knight
    game_state.board[7][7] = "r"  # Opponent's rook

    print("Initial Game State:")
    game_state.display()
    move = MoveCommand(game_state, (0, 0), (2, 0))  # Move rook from (0, 0) to (0, 2)
    game_state.make_move(move)

    print("After Move:")
    game_state.display()

    game_state.undo_move()

    print("After Undo:")
    game_state.display()


