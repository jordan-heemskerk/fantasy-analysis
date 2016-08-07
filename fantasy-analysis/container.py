class Team():

    def __init__(self, abbv):
        self.name = abbv



class Row():
    """
    @brief A row object represents of row of data.
    """

    def __init__(self, name, position, rank, team, bye):
        """
        Initialize a row
        :param name: A string indicating the name of the player
        :param position: position
        :param team: String with team abbreviation
        """

        self.name = name
        self.position = position
        self.rank = rank
        self.team = team
        self.bye = bye
