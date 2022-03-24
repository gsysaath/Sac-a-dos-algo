import sys
from itertools import combinations

from utils import (
    Combination,
    filter_dataset,
    timing,
    get_dataset,
    filter_dataset,
)


def minimum_r(dataset) -> int:
    """
    Calculate minimum repeat for a combination
    """
    sorted_by_price_desc = sorted(dataset, key=lambda item: -item.cost)
    sum = 0
    for i, item in enumerate(sorted_by_price_desc):
        sum += item.cost
        if sum > 500.0:
            break
    return i


def maximum_r(dataset) -> int:
    """
    Calculate maximum repeat for a combination
    """
    sorted_by_price_asc = sorted(dataset, key=lambda item: item.cost)
    sum = 0
    for j, item in enumerate(sorted_by_price_asc):
        sum += item.cost
        if sum > 500.0:
            break
    return j


def find_best_combination(dataset, max_cost, rep) -> Combination | None:
    """
    Find best combination in a set of combinations with the condition of
    less than or equal to max_cost where rep is the number of elements
    """
    best_combination = None
    for item in combinations(dataset, rep):
        comb = Combination(item)
        if comb.cost <= max_cost:
            if best_combination is None or (best_combination is not None and comb > best_combination):
                best_combination = comb
    return best_combination


@timing
def bruteforce(dataset, max_cost) -> Combination | None:
    """
    Returns best combination with rep between minimum_r and maximum_r
    """
    previous_combination = None
    for rep in range(minimum_r(dataset), maximum_r(dataset) + 1):
        combination = find_best_combination(dataset, max_cost, rep)
        if previous_combination is None or (previous_combination is not None and previous_combination < combination):
            previous_combination = combination
        else:
            return previous_combination


if __name__ == '__main__':
    bruteforce(
        dataset=filter_dataset(get_dataset(str(sys.argv[1]))),
        max_cost=int(sys.argv[2]),
    )
