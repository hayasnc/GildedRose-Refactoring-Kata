from .base import ItemBaseUpdater


class Conjured(ItemBaseUpdater):
    """
    degrades in quality twice as fast as normal items.
    """

    def update(self):
        self.item.sell_in -= 1

        degradation = 2
        if self.item.sell_in < 0:
            degradation *= 2

        self.item.quality = max(self.item.quality - degradation, 0)
