# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_not_expired(self):
        """
        GIVEN an item called "Dave"
        AND has a quality of 10
        AND has 5 days left to be sold
        WHEN calling update_quality
        THEN the quality should be set to 9
        AND the sell in should be 4
        """
        # GIVEN
        item = Item(
            name="Dave",
            sell_in=5,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 9
        expected_sell_in = 4

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)

    def test_has_expired(self):
        """
        GIVEN an item called "Dave"
        AND has a quality of 10
        AND has 0 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 8
        AND the sell in should be 0
        """
        # GIVEN
        item = Item(
            name="Dave",
            sell_in=0,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 8
        expected_sell_in = 0

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)

    def test_has_zero_quality(self):
        """
        GIVEN an item called "Dave"
        AND has a quality of 0
        AND has 10 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 0
        AND the sell in should be 9
        """
        # GIVEN
        item = Item(
            name="Dave",
            sell_in=10,
            quality=0,
        )
        rose = GildedRose(items=[item])
        expected_quality = 0
        expected_sell_in = 9

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)

    def test_aged_brie_increases_quality(self):
        """
        GIVEN an item called "Aged Brie"
        AND has a quality of 10
        AND has 10 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 11
        AND the sell in should 9
        """
        # GIVEN
        item = Item(
            name="Aged Brie",
            sell_in=10,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 11
        expected_sell_in = 9

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)

    def test_aged_brie_expired_increases_quality_double_fast(self):
        """
        GIVEN an item called "Aged Brie"
        AND has a quality of 10
        AND has 0 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 12
        AND the sell in should 0
        """
        # GIVEN
        item = Item(
            name="Aged Brie",
            sell_in=0,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 12
        expected_sell_in = 0

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)

    def test_quality_cannot_exceed_50(self):
        """
        GIVEN an item called "Dave"
        AND has a quality of 50
        AND has 10 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 50
        AND the sell in should 9
        """
        # GIVEN
        item = Item(
            name="Dave",
            sell_in=10,
            quality=50,
        )
        rose = GildedRose(items=[item])
        expected_quality = 50
        expected_sell_in = 9

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)

    def test_sulfuras_never_decreases_quality_or_sell_in(self):
        """
        GIVEN an item called "Sulfuras, Hand of Dave"
        AND has a quality of 50
        AND has 10 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 50
        AND the sell in should 10
        """
        # GIVEN
        item = Item(
            name="Sulfuras, Hand of Dave",
            sell_in=10,
            quality=50,
        )
        rose = GildedRose(items=[item])
        expected_quality = 50
        expected_sell_in = 10

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)

    def test_backstage_passes_increases_in_quality(self):
        """
        GIVEN an item called "Backstage passes to Dave"
        AND has a quality of 10
        AND has 30 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 11
        AND the sell in should be 9
        """
        # GIVEN
        item = Item(
            name="Backstage passes to Dave",
            sell_in=30,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 11
        expected_sell_in = 29

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)
        self.assertEqual(expected_sell_in, actual_sell_in)

    def test_backstage_passes_increases_in_quality_10_days_or_less(self):
        """
        GIVEN an item called "Backstage passes to Dave"
        AND has a quality of 10
        AND has 10 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 12
        AND the sell in should be 9
        """
        # GIVEN
        item = Item(
            name="Backstage passes to Dave",
            sell_in=10,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 12
        expected_sell_in = 9

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)
        self.assertEqual(expected_sell_in, actual_sell_in)

    def test_backstage_passes_increases_in_quality_5_days_or_less(self):
        """
        GIVEN an item called "Backstage passes to Dave"
        AND has a quality of 10
        AND has 5 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 13
        AND the sell in should be 4
        """
        # GIVEN
        item = Item(
            name="Backstage passes to Dave",
            sell_in=5,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 13
        expected_sell_in = 4

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)
        self.assertEqual(expected_sell_in, actual_sell_in)

    def test_backstage_passes_zero_quality_0_days_left(self):
        """
        GIVEN an item called "Backstage passes to Dave"
        AND has a quality of 10
        AND has 0 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 0
        AND the sell in should be 0
        """
        # GIVEN
        item = Item(
            name="Backstage passes to Dave",
            sell_in=0,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 0
        expected_sell_in = -1

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)
        self.assertEqual(expected_sell_in, actual_sell_in)

    def test_backstage_passes_zero_quality_0_days_left(self):
        """
        GIVEN an item called "Backstage passes to Dave"
        AND has a quality of 10
        AND has 0 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 0
        AND the sell in should be 0
        """
        # GIVEN
        item = Item(
            name="Backstage passes to Dave",
            sell_in=0,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 0
        expected_sell_in = -1

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)
        self.assertEqual(expected_sell_in, actual_sell_in)

    def test_conjured_items_degrade_twice_as_fast(self):
        """
        GIVEN an item called "Conjured Dave"
        AND has a quality of 10
        AND has 10 days left to be sold
        WHEN calling update_quality
        THEN the quality should be 8
        AND the sell in should be 9
        """
        # GIVEN
        item = Item(
            name="Conjured Dave",
            sell_in=10,
            quality=10,
        )
        rose = GildedRose(items=[item])
        expected_quality = 8
        expected_sell_in = 9

        # WHEN
        rose.update_quality()
        actual_quality = rose.items[0].quality
        actual_sell_in = rose.items[0].sell_in

        # THEN
        self.assertEqual(expected_quality, actual_quality)
        self.assertEqual(expected_sell_in, actual_sell_in)


if __name__ == "__main__":
    unittest.main()
