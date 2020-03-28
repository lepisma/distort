"""
Transforming from one space to other
"""

import re
from typing import List, Optional

import cmudict

CMUDICT = cmudict.dict()
PHONES = cmudict.phones()


def graphemes_to_phonemes(graphemes: List[str]) -> Optional[List[str]]:
    """
    Basic cmudict based English g2p.
    """

    word = "".join(graphemes)

    if word not in CMUDICT:
        return None

    # TODO: Probably should return all the pronunciations
    return CMUDICT[word][0]


def phonemes_to_graphemes(phonemes: List[str]) -> List[str]:
    raise NotImplementedError()


def phoneme_type(phoneme: str) -> Optional[str]:
    """
    Return phone type based on CMUDICT.
    """

    canonical_phoneme = re.sub(r"\d+$", "", phoneme)
    for p, types in PHONES:
        if p == canonical_phoneme:
            return types[0]
