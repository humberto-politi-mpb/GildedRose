from abstract_item_updater import AbstractItemUpdater


class ConjuredItemUpdater(AbstractItemUpdater):
    def _update_sell_in(self):
        self._item.sell_in -= 1

    def _update_quality(self):
        decrease_value = self.__get_item_quality_decrease_value()
        new_quality = self._item.quality - decrease_value
        self._item.quality = max(0, new_quality)

    def __get_item_quality_decrease_value(self):
        value = 2
        if self._item.sell_in < 0:
            value = 4
        return value
