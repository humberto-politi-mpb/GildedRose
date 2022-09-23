from abstract_item_updater import AbstractItemUpdater


class AgedItemUpdater(AbstractItemUpdater):
    def _update_sell_in(self):
        self._item.sell_in -= 1

    def _update_quality(self):
        increase_value = self.__get_item_quality_increase_value()
        new_value = self._item.quality + increase_value
        self._item.quality = min(50, new_value)

    def __get_item_quality_increase_value(self):
        update_value = 1
        if self._item.sell_in < 0:
            update_value = 2
        return update_value