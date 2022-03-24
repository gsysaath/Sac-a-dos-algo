import sys
from random import shuffle

from utils import (
    Combination,
    timing,
    get_dataset,
    filter_dataset,
)


@timing
def optimized(dataset, max_cost, max_random_tries) -> Combination | None:
    """
    Returns a combination with the best time complexity.
    """
    best_comb = None
    if best_comb is None and len(sys.argv) > 3:
        max_random_tries = int(sys.argv[3])
    while max_random_tries > 0:
        items_list_result = []
        actual_cost = 0
        for data_item in dataset:
            if actual_cost + data_item.cost <= max_cost:
                items_list_result.append(data_item)
                actual_cost += data_item.cost
        if best_comb is None:
            best_comb = Combination(items_list_result)
        else:
            best_comb = max(Combination(items_list_result), best_comb)
        max_random_tries -= 1
        shuffle(dataset)
    return best_comb


if __name__ == '__main__':
    optimized(
        dataset=filter_dataset(get_dataset(str(sys.argv[1]))),
        max_cost=int(sys.argv[2]),
        max_random_tries=int(sys.argv[3]),
    )
