import re


from container import Row

class FormatSpecifierCannotProcessError(Exception):
    pass

class FormatSpecifierFactory():

    _fox_sports_regex = re.compile("(\d+)\.\s(.+)\s\((\w+)\s-\s(\w+)\).+(\d+)")

    def __init__(self):
        pass

    def get_format_specifier(self, fs):
        """
        Gets a format specifier

        Available format specifiers

         - fox_sports

        :param fs: The format specifier to get
        :return: The format specifier
        """
        if (fs == "fox_sports"):
            return FormatSpecifierFactory._fox_sports_format_specifier

    @staticmethod
    def _fox_sports_format_specifier(row):

        match = FormatSpecifierFactory._fox_sports_regex.match(row)

        if not match:
            raise FormatSpecifierCannotProcessError("Could not parse: " + row)

        num_groups = len(match.groups())
        if num_groups != 5:
            raise FormatSpecifierCannotProcessError("Incorrect number of groups (%d!=5) in successful match on: %s" % (num_groups, row))

        g = match.groups()

        return Row(
            g[1],  # name
            g[3],  # position
            int(g[0]),  # rank
            g[2],  # team
            g[4]   # bye
        )


