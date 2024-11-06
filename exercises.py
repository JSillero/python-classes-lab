class Game:
    def __init__(self):
        self.board = Board()
        self.gameStart()

    def gameStart(self):
        print("Welcome to tic,tac and toe!")
        game_on = True
        """  """
        while game_on:
            self.board.resetBoard()
            game_state = 0
            while game_state == 0 or game_state == -1:
                game_state = self.turn_manager()

            """ Once the gamestate ending has been reached there is a prompt to play again. Program ends if no is chosen """
            print(self.board)
            game_on = input("Want to play again? (yes/no)")
            while not (game_on == "yes" or game_on == "no"):
                print("Input invalid, use 'yes' or 'no' answers")
                game_on = input("Want to play again? (yes/no)")

            game_on = True if 'yes' else False

    def turn_manager(self):
        """ set current team by looking at team order """
        team = "X" if self.board.turn % 2 == 0 else "O"

        print(f"""{self.board}
        {team} Turn
        Time to choose where to place your piece!""")
        x = input("Choose the X coordinate:")
        y = input("Choose the Y coordinate:")

        result = self.board.setValue(x, y, team)

        if (type(result) is str):
            print(f"{team} wins!")
        elif (result == 1):
            print("Its a tie!")
            
        return result
    
        
        


class Board:
    def __init__(self):
        self.turn = 0
        self.board = {'11': " ", '21': " ", '31': " ", '12': " ",
                      '22': " ", '32': " ", '13': " ", '23': " ", '33': " ", }

    def resetBoard(self):
        self.turn = 0
        self.board = {'11': " ", '21': " ", '31': " ", '12': " ",
                      '22': " ", '32': " ", '13': " ", '23': " ", '33': " ", }

    """ 
    returns 0 if input was valid, -1 if input was invalid, X/O if a victory condition was met, and 1 in case of tie 
    """

    def setValue(self, X, Y, value):
        try:
            if (self.board[X+Y] == " "):
                self.board[X+Y] = value
                return self.checkWinstate(value)

            else:
                print("That cell already has a value!!")
                return -1

        except KeyError:
            print("Invalid cell value, X and Y can only be values 1 to 3.")
            return -1

    def checkWinstate(self, value):
        """ Check the lines for winstate """
        for x in range(1, 4):
            if (self.board.get(str(x)+"1") != " " and (self.board.get(str(x)+"1") == self.board.get(str(x)+"2") and self.board.get(str(x)+"1") == self.board.get(str(x)+"3"))):
                return value

        """ Check the columns for winstate """
        for y in range(1, 4):
            if (self.board.get("1" + str(y)) != " " and (self.board.get("1" + str(y)) == self.board.get("2" + str(y)) and self.board.get("1" + str(y)) == self.board.get("3" + str(y)))):
                return value

        """ Check the diagonals for winstates """
        if (self.board.get("11") != " " and (self.board.get("11") == self.board.get("22") and self.board.get("11") == self.board.get("33"))):
            return value
        if (self.board.get("31") != " " and (self.board.get("31") == self.board.get("22") and self.board.get("11") == self.board.get("13"))):
            return value

        """ Increase number of turns if nine has been reached and there is no winner its a tie """
        self.turn += 1
        if (self.turn == 9):
            return 1

        """If no endstate is reached, return 0, continue game """
        return 0

    def __str__(self) -> str:
        return (f"""Board:
        __|X 1 | 2 | 3
        Y
        1    {self.board.get("11")}   {self.board.get("21")}   {self.board.get("31")}
        2    {self.board.get("12")}   {self.board.get("22")}   {self.board.get("32")}
        3    {self.board.get("13")}   {self.board.get("23")}   {self.board.get("33")}
___________________________________""")


game = Game()
game.gameStart()
