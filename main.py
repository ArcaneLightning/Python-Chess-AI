import board, pieces, ai
from move import Move

class Main:
    def __init__(self, color):
        self.color = color

    def get_user_move(self):
        if self.color == pieces.Piece.WHITE:
            print("Example Move: E2 E4")
        else:
            print("Example Move: E7 E5")
        move_str = input("Your Move: ")
        move_str = move_str.replace(" ", "")

        try:
            xfrom = self.letter_to_xpos(move_str[0:1])
            yfrom = 8 - int(move_str[1:2])  # The board is drawn "upside down", so flip the y coordinate.
            xto = self.letter_to_xpos(move_str[2:3])
            yto = 8 - int(move_str[3:4])  # The board is drawn "upside down", so flip the y coordinate.
            return Move(xfrom, yfrom, xto, yto)
        except ValueError:
            print("Invalid Format. Example: A2 A4")
            return self.get_user_move()

    def get_valid_user_move(self, board):
        while True:
            move = self.get_user_move()
            valid = False
            possible_moves = board.remove_check_moves(self.color)
            # for i in possible_moves:
            #     print(i.to_string(), end= " ")

            # No possible moves
            if (not possible_moves):
                return 0

            for possible_move in possible_moves:
                if (move.equals(possible_move)):
                    valid = True
                    break

            if (valid):
                break
            else:
                try:
                    copy = board.clone(board)
                    copy.perform_move(move)
                except:
                    print("Invalid Move")
                else:
                    if copy.is_check(self.color):
                        print("Invalid Move due to CHECK.")
                    else:
                        print("Invalid Move")

        return move

    def letter_to_xpos(self, letter):
        letter = letter.upper()
        letters = "ABCDEFGH"
        num = [0, 1, 2, 3, 4, 5, 6, 7]
        if letter in letters:
            return num[letters.index(letter)]
        else:
            raise ValueError("Invalid Letter.")

    def get_difficulty(self):
        global choice
        print("\nDifficulty Levels\n1. Easy\n2. Medium I\n3. Medium II (slow)")
        while True:
            while True:
                try:
                    choice = int(input("Enter the number of your choice: "))
                    break
                except:
                    print("Invalid input")
            print()
            if choice == 1:
                # depth = 0
                return 0
            elif choice == 2:
                # depth = 2
                return 2
            elif choice == 3:
                # depth = 3
                return 3
            else:
                print("Invalid input")

    def run(self):
        other_color = pieces.Piece.BLACK
        if self.color == pieces.Piece.BLACK:
            other_color = pieces.Piece.WHITE
        difficulty = self.get_difficulty()
        new_board = board.Board.new()
        print(new_board.to_string())

        if self.color == pieces.Piece.WHITE:
            while True:
                if new_board.is_check(self.color):
                    print("You are under CHECK.")

                move = self.get_valid_user_move(new_board)

                if move == 0:
                    if new_board.is_check(self.color):
                        print("Checkmate. The AI Wins.")
                        break
                    else:
                        print("Stalemate.")
                        break

                new_board.perform_move(move)

                print("User move: " + move.to_letter())
                print(new_board.to_string())

                if new_board.is_check(other_color):
                    print("The AI is under CHECK")

                ai_move = ai.AI.get_ai_move(new_board, difficulty, other_color)
                if (ai_move == 0):
                    if (new_board.is_check(other_color)):
                        print("Checkmate. You win.")
                        break
                    else:
                        print("Stalemate.")
                        break

                new_board.perform_move(ai_move)
                print("AI move: " + ai_move.to_letter())
                print(new_board.to_string())

        else:
            while True:
                if new_board.is_check(other_color):
                    print("The AI is under CHECK.")

                ai_move = ai.AI.get_ai_move(new_board, difficulty, other_color)
                if (ai_move == 0):
                    if (new_board.is_check(other_color)):
                        print("Checkmate. You win.")
                        break
                    else:
                        print("Stalemate.")
                        break

                new_board.perform_move(ai_move)
                print("AI move: " + ai_move.to_letter())
                print(new_board.to_string())

                if new_board.is_check(self.color):
                    print("You are under CHECK.")

                move = self.get_valid_user_move(new_board)

                if move == 0:
                    if new_board.is_check(self.color):
                        print("Checkmate. The AI Wins.")
                        break
                    else:
                        print("Stalemate.")
                        break

                new_board.perform_move(move)

                print("User move: " + move.to_letter())
                print(new_board.to_string())

if __name__ == "__main__":
    while True:
        choice = input("What color do you want (B / W): ")
        if choice.upper() == "B":
            color = pieces.Piece.BLACK
            break
        elif choice.upper() == "W":
            color = pieces.Piece.WHITE
            break
        else:
            print("Invalid Entry")

    main = Main(color)
    main.run()