from item_updaters.base import ItemBaseUpdater


class NormalItem(ItemBaseUpdater):
    """
    decrease in quality by 1 each day.
    After sell_in date, quality decreases by 2 each day.
    cannot be negative.
    """

    def update(self):
        self.item.sell_in -= 1
        self.item.quality -= 1 if self.item.quality > 0 else 0
        if self.item.sell_in < 0 and self.item.quality > 0:
            self.item.quality -= 1
