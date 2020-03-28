import random
from typing import List, Set


def replace_with_p(items: List, item_set: Set, p: float) -> List:
    """
    Raw uniform replacement where each item is likely to be replaced with
    another item from the set with probability p.
    """

    # TODO: Holy
    item_set_list = list(item_set)

    replaced = []
    for it in items:
        if random.random() < p:
            replaced.append(random.choice(item_set_list))
        else:
            replaced.append(it)

    return replaced
