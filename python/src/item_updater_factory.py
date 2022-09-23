from item import  Item
from conjured_item_updater import ConjuredItemUpdater
from common_item_updater import CommonItemUpdater
from legendary_item_updater import LegendaryItemUpdater
from aged_item_updater import AgedItemUpdater
from basckstage_pass_updater import BackstagePassUpdater


class ItemUpdaterFactory:
    def get_updater_for_item(self, item: Item):
        if self.__is_legendary_item(item):
            return LegendaryItemUpdater(item)
        elif self.__is_aged_item(item):
            return AgedItemUpdater(item)
        elif self.__is_backstage_pass(item):
            return BackstagePassUpdater(item)
        elif self.__is_conjured_item(item):
            return ConjuredItemUpdater(item)
        else:
            return CommonItemUpdater(item)

    def __is_legendary_item(self, item):
        return bool("Sulfuras" in item.name)

    def __is_aged_item(self, item):
        return bool("Aged" in item.name)

    def __is_backstage_pass(self, item):
        return bool("Backstage passes" in item.name)

    def __is_conjured_item(self, item):
        return bool("Conjured" in item.name)
