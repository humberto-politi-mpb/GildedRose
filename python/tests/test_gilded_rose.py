# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import  Item


class TestGildedRoseUpdateQualityWithCommonItem(unittest.TestCase):
    def setUp(self) -> None:
        self.common_item = Item(
            name="Common",
            quality=1,
            sell_in=1,
        )
    def test_sell_in_decreased(self):
        self.common_item.sell_in = 2
        items = [self.common_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_sell_in = 1
        self.assertEquals(expected_sell_in, self.common_item.sell_in)

    def test_positive_sell_in__quality_decreased_by_one(self):
        self.common_item.quality = 2
        self.common_item.sell_in = 2
        items = [self.common_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 1
        self.assertEquals(expected_quality, self.common_item.quality)

    def test_zeroed_sell_in__quality_decreased_by_one(self):
        self.common_item.quality = 2
        self.common_item.sell_in = 1  # call to update_quality will decrease this to 0
        items = [self.common_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 1
        self.assertEquals(expected_quality, self.common_item.quality)

    def test_negative_sell_in__quality_decreased_by_two(self):
        self.common_item.quality = 4
        self.common_item.sell_in = 0  # call to update_quality will decrease this to -1
        items = [self.common_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 2
        self.assertEquals(expected_quality, self.common_item.quality)

    def test_zeroed_quality__quality_not_decreased_to_negative_number(self):
        self.common_item.quality = 0
        self.common_item.sell_in = 1
        items = [self.common_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 0
        self.assertEquals(expected_quality, self.common_item.quality)

class TestGildedRoseUpdateQualityWithAgedItem(unittest.TestCase):
    def setUp(self) -> None:
        self.aged_item = Item(
                name="Aged Brie",
                quality=1,
                sell_in=1,
            )

    def test_sell_in_decreased(self):
        self.aged_item.sell_in = 2
        items = [self.aged_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_sell_in = 1
        self.assertEquals(expected_sell_in, self.aged_item.sell_in)

    def test_positive_sell_in__quality_increased_by_one(self):
        self.aged_item.sell_in = 10
        self.aged_item.quality = 1
        items = [self.aged_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 2
        self.assertEquals(expected_quality, self.aged_item.quality)

    def test_zeroed_sell_in__quality_increased_by_one(self):
        self.aged_item.quality = 1
        self.aged_item.sell_in = 1  # call to update_quality will update this value to 0
        items = [self.aged_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_sell_in = 0
        self.assertEquals(expected_sell_in, self.aged_item.sell_in)
        expected_quality = 2
        self.assertEquals(expected_quality, self.aged_item.quality)

    def test_negative_sell_in__quality_increased_by_two(self):
        self.aged_item.quality = 1
        self.aged_item.sell_in = 0  # call to update_quality will update this value to -1
        items = [self.aged_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_sell_in = -1
        self.assertEquals(expected_sell_in, self.aged_item.sell_in)
        expected_quality = 3
        self.assertEquals(expected_quality, self.aged_item.quality)

    def test_quality_is_50__quality_does_not_increase(self):
        self.aged_item.sell_in = 10
        self.aged_item.quality = 50
        items = [self.aged_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 50
        self.assertEquals(expected_quality, self.aged_item.quality)

class TestGildedRoseUpdateQualityWithBackstagePasses(unittest.TestCase):
    def setUp(self) -> None:
        self.backstage_pass_item = Item(
                name="Backstage passes to a TAFKAL80ETC concert",
                quality=1,
                sell_in=1,
            )

    def test_sell_in_decreased(self):
        self.backstage_pass_item.sell_in = 2
        items = [self.backstage_pass_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_sell_in = 1
        self.assertEquals(expected_sell_in, self.backstage_pass_item.sell_in)

    def test_sell_in_greater_than_10__quality_increased_by_one(self):
        self.backstage_pass_item.sell_in = 20
        self.backstage_pass_item.quality = 1
        items = [self.backstage_pass_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 2
        self.assertEquals(expected_quality, self.backstage_pass_item.quality)

    def test_sell_in_equal_to_10__quality_increased_by_two(self):
        self.backstage_pass_item.quality = 1
        self.backstage_pass_item.sell_in = 11  # call to update_quality will update this value to 10
        items = [self.backstage_pass_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_sell_in = 10
        self.assertEquals(expected_sell_in, self.backstage_pass_item.sell_in)
        expected_quality = 3
        self.assertEquals(expected_quality, self.backstage_pass_item.quality)

    def test_sell_in_greater_than_5_and_less_than_10__quality_increased_by_two(self):
        self.backstage_pass_item.quality = 1
        self.backstage_pass_item.sell_in = 8  # call to update_quality will update this value to 7
        items = [self.backstage_pass_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_sell_in = 7
        self.assertEquals(expected_sell_in, self.backstage_pass_item.sell_in)
        expected_quality = 3
        self.assertEquals(expected_quality, self.backstage_pass_item.quality)

    def test_sell_in_equal_to_5__quality_increased_by_three(self):
        self.backstage_pass_item.quality = 1
        self.backstage_pass_item.sell_in = 6  # call to update_quality will update this value to 5
        items = [self.backstage_pass_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_sell_in = 5
        self.assertEquals(expected_sell_in, self.backstage_pass_item.sell_in)
        expected_quality = 4
        self.assertEquals(expected_quality, self.backstage_pass_item.quality)

    def test_negative_sell_in__quality_dropped_to_0(self):
        self.backstage_pass_item.quality = 10
        self.backstage_pass_item.sell_in = 0  # call to update_quality will update this value to -1
        items = [self.backstage_pass_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_sell_in = -1
        self.assertEquals(expected_sell_in, self.backstage_pass_item.sell_in)
        expected_quality = 0
        self.assertEquals(expected_quality, self.backstage_pass_item.quality)

    def test_quality_is_50__quality_does_not_increase(self):
        self.backstage_pass_item.sell_in = 20
        self.backstage_pass_item.quality = 50
        items = [self.backstage_pass_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 50
        self.assertEquals(expected_quality, self.backstage_pass_item.quality)

class TestGildedRoseUpdateQualityWithLegendaryItem(unittest.TestCase):
    def setUp(self) -> None:
        self.legendary_item = Item(
                name="Sulfuras, Hand of Ragnaros",
                quality=1,
                sell_in=1,
            )

    def test_sell_in_never_decreased(self):
        self.legendary_item.sell_in = 10
        items = [self.legendary_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_sell_in = 10
        self.assertEquals(expected_sell_in, self.legendary_item.sell_in)

    def test_quality_always_80(self):
        self.legendary_item.sell_in = 10
        self.legendary_item.quality = 10
        items = [self.legendary_item]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        expected_quality = 80
        self.assertEquals(expected_quality, self.legendary_item.quality)

class TestGildedRoseUpdateQualityWithConjuredItem(unittest.TestCase):
    def setUp(self) -> None:
        self.conjured = Item(
            name="Conjured",
            quality=1,
            sell_in=1,
        )

    def test_sell_in_decreased(self):
        self.conjured.sell_in = 2
        items = [self.conjured]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_sell_in = 1
        self.assertEquals(expected_sell_in, self.conjured.sell_in)

    def test_positive_sell_in__quality_decreased_by_two(self):
        self.conjured.quality = 4
        self.conjured.sell_in = 2
        items = [self.conjured]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 2
        self.assertEquals(expected_quality, self.conjured.quality)

    def test_zeroed_sell_in__quality_decreased_by_two(self):
        self.conjured.quality = 4
        self.conjured.sell_in = 1  # call to update_quality will decrease this to 0
        items = [self.conjured]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 2
        self.assertEquals(expected_quality, self.conjured.quality)

    def test_negative_sell_in__quality_decreased_by_four(self):
        self.conjured.quality = 8
        self.conjured.sell_in = 0  # call to update_quality will decrease this to -1
        items = [self.conjured]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 4
        self.assertEquals(expected_quality, self.conjured.quality)

    def test_zeroed_quality__quality_not_decreased_to_negative_number(self):
        self.conjured.quality = 0
        self.conjured.sell_in = 1
        items = [self.conjured]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        expected_quality = 0
        self.assertEquals(expected_quality, self.conjured.quality)

if __name__ == '__main__':
    unittest.main()
