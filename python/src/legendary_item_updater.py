from abstract_item_updater import AbstractItemUpdater


class LegendaryItemUpdater(AbstractItemUpdater):
    def _update_quality(self):
        if self._item.quality != 80:
            self._item.quality = 80

    def _update_sell_in(self):
        pass