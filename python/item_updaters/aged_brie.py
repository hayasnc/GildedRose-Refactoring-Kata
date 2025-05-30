from .base import ItemBaseUpdater


class AgedBrie(ItemBaseUpdater):
    """
    Quality increases increases
    Quality increases twice as fast afer sell_in period”
    """

    def update(self):
        self.item.sell_in -= 1
        if self.item.quality < 50:
            self.item.quality += 1
        if self.item.sell_in < 0 and self.item.quality < 50:
            self.item.quality += 1
