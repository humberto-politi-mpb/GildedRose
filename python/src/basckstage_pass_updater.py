from abstract_item_updater import AbstractItemUpdater


class BackstagePassUpdater(AbstractItemUpdater):
    def _update_sell_in(self):
        self._item.sell_in -= 1

    def _update_quality(self):
        update_value = self.__get_backstage_pass_update_value()
        new_value = self._item.quality + update_value
        new_value = min(50, new_value)
        new_value = max(0, new_value)
        self._item.quality = new_value

    def __get_backstage_pass_update_value(self):
        update_value = 1
        if self._item.sell_in < 0:
            update_value = -self._item.quality
        else:
            if 10 >= self._item.sell_in > 5:
                update_value = 2
            elif 5 >= self._item.sell_in:
                update_value = 3
        return update_value