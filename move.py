class Move:

    def __init__(self, xfrom, yfrom, xto, yto):
        self.xfrom = xfrom
        self.yfrom = yfrom
        self.xto = xto
        self.yto = yto
    
    # Returns string representation of move as move notation (piece type NOT included)
    def __str__(self):
        letters = "ABCDEFGH"

        new_xfrom = letters[self.xfrom]
        new_yfrom = 8 - self.yfrom
        new_xto = letters[self.xto]
        new_yto = 8 - self.yto

        return f"{new_xfrom}{new_yfrom} {new_xto}{new_yto}"

    # Returns true if (xfrom,yfrom) and (xto,yto) are the same.
    def __eq__(self, other_move):
        return self.xfrom == other_move.xfrom and self.yfrom == other_move.yfrom and self.xto == other_move.xto and self.yto == other_move.yto

