# -*- coding: utf-8 -*-
from typing import Callable


class GildedRose(object):
    MAX_QUALITY = 50
    MIN_QUALITY = 0

    def __init__(self, items) -> None:
        self.items = items

    def update_quality(self) -> None:
        for item in self.items:
            handler_func = self._fetch_handler(item=item)
            handler_func(item=item)

    def _fetch_handler(self, item: "Item") -> Callable:
        item_name = item.name.lower()
        if item_name == "aged brie":
            return self._cheese_handler

        if item_name.startswith("sulfuras "):
            return self._legendary_handler

        if item_name.startswith("backstage passes "):
            return self._ticket_handler

        if item_name.startswith("conjured "):
            return self._conjured_handler

        return self._default_handle

    def _has_expired(self, item: "Item") -> bool:
        return item.sell_in <= 0

    def _cheese_handler(self, item: "Item") -> None:
        if self._has_expired(item=item):
            item.quality += 2
        else:
            item.quality += 1
            item.sell_in -= 1

    def _legendary_handler(self, item: "Item") -> None:
        pass

    def _ticket_handler(self, item: "Item") -> None:
        has_expired = self._has_expired(item=item)
        if has_expired:
            item.quality = self.MIN_QUALITY
        elif item.sell_in > 10:
            item.quality += 1
            item.sell_in -= 1
        elif item.sell_in > 5:
            item.quality += 2
            item.sell_in -= 1
        else:
            item.quality += 3
            item.sell_in -= 1

    def _conjured_handler(self, item: "Item") -> None:
        item.quality -= 2
        item.sell_in -= 1

    def _default_handler(self, item: "Item") -> None:
        is_max_quality = item.quality == self.MAX_QUALITY
        is_min_quality = item.quality == self.MIN_QUALITY
        has_expired = self._has_expired(item=item)

        if has_expired:
            item.quality -= 2
        elif is_min_quality or is_max_quality:
            item.sell_in -= 1
        else:
            item.sell_in -= 1
            item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
