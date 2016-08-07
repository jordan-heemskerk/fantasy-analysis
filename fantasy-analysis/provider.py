
class Provider():
    """
    @brief A provider provides data in a standardized format. This is meant to be extended to allow for arbitraty inputs
    to be specified.
    """

    def __init__(self):
        self.data = []



class FileProvider(Provider):
    """
    @brief A FileProvider is a provider that reads from a file
    """

    def __init__(self, fh, format_specifier):
        """
        Creates a new FileProvider
        :param fh: A file handle that provides the readline functionality
        :param format_specifier: A function that when called with the output of fh.readline returns a Row object
        reflecting that line of input.
        """
        self.fh = fh
        self.format_specifier = format_specifier

    def data(self):
        """
        Get the data associated with this provider, sorted by player rank
        :return: A list of row objects, sorted by player rank
        """
        retr = [self.format_specifier(k) for k in self.fh.readlines()]
        retr.sort(key=lambda x: x.rank)
        return retr
