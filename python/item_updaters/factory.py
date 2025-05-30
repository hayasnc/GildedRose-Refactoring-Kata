from .aged_brie import AgedBrie
from .backstage import BackstagePass
from .sulfuras import Sulfuras
from .normal import NormalItem
from .conjured import Conjured


def get_updatable_item(item):
    if item.name == "Aged Brie":
        return AgedBrie(item)
    elif item.name == "Backstage passes to a TAFKAL80ETC concert":
        return BackstagePass(item)
    elif item.name == "Sulfuras, Hand of Ragnaros":
        return Sulfuras(item)
    elif item.name == "Conjured Mana Cake":
        return Conjured(item)
    else:
        return NormalItem(item)
