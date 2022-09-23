from item import Item
from abc import ABC, abstractmethod


class AbstractItemUpdater(ABC):
    def __init__(self, item: Item):
        self._item = item

    @abstractmethod
    def _update_sell_in(self):
        pass

    @abstractmethod
    def _update_quality(self):
        pass

    def update(self):
        self._update_sell_in()
        self._update_quality()
