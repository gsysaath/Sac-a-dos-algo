import time
import csv

from dataclasses import dataclass
from typing import List


@dataclass
class Item:
    name: str
    cost: float
    gains: float

    def __str__(self):
        return self.name


@dataclass
class Combination:
    items: List[Item]
    _cost: float = None
    _gains: float = None

    def __str__(self):
        return f"{len(self.items)}:{'-'.join([str(item.name) for item in self.items])}:{self.cost}:{self.gains}"

    @property
    def cost(self):
        """
        Returns cost of the combination
        """
        if self._cost is None:
            self._cost = sum(item.cost for item in self.items)
        return self._cost

    @property
    def gains(self):
        """
        Returns gains of the combination
        """
        if self._gains is None:
            self._gains = sum(item.gains for item in self.items)
        return self._gains

    @property
    def actions(self):
        """
        Returns list of actions name
        """
        return [item.name for item in self.items]

    def __gt__(self, other):
        return self.gains > other.gains


def timing(fn):
    """
    Get and print time needed for fn function to finish
    """
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(
            f"Function : {fn.__name__}\n"
            f"Actions : {res.actions}\n"
            f"Cost : {res.cost}\n"
            f"Gains : {res.gains:.2f} \n"
            f"Time : {elapsed:.2f} seconds"
        )
        return res
    return wrapper


def get_dataset(file_name):
    """
    Open and read csv file and return an array of Items
    """
    dataset_1 = []
    with open(f"data/{file_name}", encoding='utf-8-sig') as csvfile:
        # change contents to floats
        reader = csv.DictReader(
            csvfile, quoting=csv.QUOTE_NONNUMERIC)  # skip the headers
        for row in reader:  # each row is a list
            dataset_1.append(Item(row['share'], row['cost'], row['gains']))
    return dataset_1


def filter_dataset(dataset):
    """
    Check if item cost or gains are not negative values.
    return cleaned dataset
    """
    return [item for item in dataset if item.cost > 0.0 and item.gains > 0.0]
