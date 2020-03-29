import random
from typing import List


def replace_with_p(items: List, eq_classes: List[List], p: float) -> List:
    """
    Raw uniform replacement where each item is likely to be replaced with
    another item from the set with probability p. `eq_classes` define which
    classes are equivalent.
    """

    def _get_equivalents(it):
        for equivalents in eq_classes:
            if it in equivalents:
                return equivalents

    replaced = []
    for it in items:
        replacement = it
        if random.random() < p:
            equivalents = _get_equivalents(it)
            if equivalents:
                replaced.append(random.choice(equivalents))

        replaced.append(replacement)

    return replaced
