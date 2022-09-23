# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """
        Updates the quality of items
        """
        for thing_to_adjust in self.items:
            # loop through all items
            if thing_to_adjust.name != "Aged Brie" and thing_to_adjust.name != "Backstage passes to a TAFKAL80ETC concert":
                if thing_to_adjust.quality > 0:
                    if thing_to_adjust.name != "Sulfuras, Hand of Ragnaros":
                        thing_to_adjust.quality = thing_to_adjust.quality - 1
            else:
                # threshold
                if thing_to_adjust.quality < 50:
                    thing_to_adjust.quality = thing_to_adjust.quality + 1
                    if thing_to_adjust.name == "Backstage passes to a TAFKAL80ETC concert":
                        if thing_to_adjust.sell_in < 11:
                            if thing_to_adjust.quality < 50:
                                thing_to_adjust.quality = thing_to_adjust.quality + 1
                        if thing_to_adjust.sell_in < 6:
                            if thing_to_adjust.quality < 50:
                                thing_to_adjust.quality = thing_to_adjust.quality + 1
            # ignore
            if thing_to_adjust.name != "Sulfuras, Hand of Ragnaros":
                thing_to_adjust.sell_in = thing_to_adjust.sell_in - 1
            if thing_to_adjust.sell_in < 0:
                # aged brie does not age
                if thing_to_adjust.name != "Aged Brie":
                    if thing_to_adjust.name != "Backstage passes to a TAFKAL80ETC concert":
                        if thing_to_adjust.quality > 0:
                            if thing_to_adjust.name != "Sulfuras, Hand of Ragnaros":
                                thing_to_adjust.quality = thing_to_adjust.quality - 1
                    else:
                        thing_to_adjust.quality = thing_to_adjust.quality - thing_to_adjust.quality
                else:
                    if thing_to_adjust.quality < 50:
                        thing_to_adjust.quality = thing_to_adjust.quality + 1
        # items should be up to date at this point


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
