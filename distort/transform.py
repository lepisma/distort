"""
Transforming from one space to other
"""

from typing import List, Optional
import re
import cmudict

CMUDICT = cmudict.dict()
PHONES = cmudict.phones()


def g2p(graphemes: List[str]) -> Optional[List[str]]:
    """
    Basic cmudict based English g2p.
    """

    word = "".join(graphemes)

    if word not in CMUDICT:
        return None

    # TODO: Probably should return all the pronunciations
    return CMUDICT[word][0]


def p2g(phonemes: List[str]) -> List[str]:
    raise NotImplementedError()


def p2type(phoneme: str) -> Optional[str]:
    """
    Return phone type based on CMUDICT.
    """

    canonical_phoneme = re.sub(r"\d+$", "", phoneme)
    for p, types in PHONES:
        if p == canonical_phoneme:
            return types[0]
