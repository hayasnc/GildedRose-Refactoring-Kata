# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_quality_increase_ten_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 38)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(40, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_backstage_passes_quality_increase_six_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(43, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_passes_quality_decrease_zero_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_backstage_pass_max_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)
        self.assertEqual(3, items[0].sell_in)

    def test_aged_brie_quality_increase(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(1, items[0].quality)

    def test_aged_brie_quality_double(self):
        items = [Item("Aged Brie", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(2, items[0].quality)


if __name__ == "__main__":
    unittest.main()
