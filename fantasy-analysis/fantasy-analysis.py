import argparse
import sys

from display import TableDisplay, PositionDensity
from provider import FileProvider
from format_specifier import FormatSpecifierFactory

def main(fh, format_specifier):

    fsf = FormatSpecifierFactory()
    fp = FileProvider(fh, fsf.get_format_specifier(format_specifier))

    td = TableDisplay(fp.data())
    td.render(sys.stdout)

    pd = PositionDensity(fp.data())
    pd.render()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Analysis of fanatasy-data")
    parser.add_argument('source', type=str)
    parser.add_argument('format', type=str)

    args = parser.parse_args()

    ifh = open(args.source)

    main(ifh, args.format)
