"""
Tool for lexical distortion. Takes input from stdin and dumps on stdout.

Usage:
  distort grapheme (random) [--p=<p>]

Options:
  --p=<p>                Perturbation probability [default: 0.2]
"""

import sys

from docopt import docopt
from pydash import py_

from distort.distort import replace_with_p


def main():
    args = docopt(__doc__)

    if args["grapheme"]:
        if args["random"]:
            p = float(args["--p"])

            pieces = [[list(word) for word in line.split()] for line in sys.stdin]
            unique_pieces = list(set(py_.flatten_deep(pieces)))

            for line in pieces:
                d_words = ["".join(replace_with_p(word, [unique_pieces], p=p)) for word in line]
                print(" ".join(d_words))
