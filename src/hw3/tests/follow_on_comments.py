import unittest

from ..follow_on_comments import *

class FollowOnCommentsTestCase(unittest.TestCase):

    def test_get_follow_ratios_dict(self):
        raw_counts = {'applejack': 108, 'rarity': 117, 'pinkie': 212, 'rainbow': 141, 'fluttershy': 121}
        canonical_ponies_without_current_pony_keys = ['applejack', 'rarity', 'pinkie', 'rainbow', 'fluttershy']
        ratio_dict = get_follow_ratios_dict(raw_counts, canonical_ponies_without_current_pony_keys)
        sum_ratios = sum(ratio_dict.values())
        rounded_sum = round(sum_ratios,2)
        self.assertTrue((rounded_sum == 0.99) or (rounded_sum == 1.01))

    def test_get_follow_ratios_dict2(self):
        raw_counts = {'twilight': 99, 'rarity': 76, 'pinkie': 92, 'rainbow': 64, 'fluttershy': 39}
        canonical_ponies_without_current_pony_keys = ['twilight', 'rarity', 'pinkie', 'rainbow', 'fluttershy']
        ratio_dict = get_follow_ratios_dict(raw_counts, canonical_ponies_without_current_pony_keys)
        sum_ratios = sum(ratio_dict.values())
        rounded_sum = round(sum_ratios,2)
        self.assertTrue((rounded_sum == 0.99) or (rounded_sum == 1.01))
