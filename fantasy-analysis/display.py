from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

class TableDisplay:

    def __init__(self, data):
        """
        Creates a Table Display that can render data
        :param data: A list of row objects to display
        """
        listed = [[x.name, x.rank, x.position, x.team, x.bye] for x in data]
        self.tabbed = tabulate(listed, headers=['Name', 'Rank', 'Position', 'Team', 'Bye Week'])

    def render(self, stream):
        """
        Renders a tablular display of this data to stream
        :param stream: An object providing the function write(str)
        """
        stream.write(self.tabbed)


class PositionDensity:

    def __init__(self, data, n_players=12):
        n_bins = int(len(data) / n_players)
        colors = ['red', 'lime', 'tan', 'blue', 'green', 'orange']

        position_sets = []
        positions = ['RB', 'WR', 'TE', 'D/ST', 'K', 'QB']

        for row in data:
            position_sets[positions.index(row.position)].append(row.rank)

        self.plot = plt.hist(position_sets, n_bins, label=positions, hyisttype='bar', stacked=True)

    def render(self):
        self.plot.show()





