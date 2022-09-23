# -*- coding: utf-8 -*-
from item_updater_factory import ItemUpdaterFactory


class GildedRose(object):
    def __init__(self, items):
        self.__items = items
        self.__item_updater_factory = ItemUpdaterFactory()
        self.__item_updaters = []
        self.__build_item_updaters()

    def __build_item_updaters(self):
        for item in self.__items:
            self.__item_updaters.append(self.__item_updater_factory.get_updater_for_item(item))

    def update_quality(self):
        """
        Updates the items
        """
        for item_updater in self.__item_updaters:
            item_updater.update()
