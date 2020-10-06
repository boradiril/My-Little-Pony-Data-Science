import unittest

from ..mentions import *

class MentionsTestCase(unittest.TestCase):
    # test pony name in the beginning, middle and end of a sentence
    def test_check_mention(self):
        dialog = "My best friend, Applejack is currently studying."
        result_bool = check_mention(dialog, "Applejack", 0)
        self.assertTrue(dialog)
    
    def test_analyze_for_one_word_pony(self):
        dialog = "Applejack is the best pony ever! I've been friends with Applejack since grade three. I love Applejack!"
        count = analyze_for_one_word_pony(dialog, "Applejack") 
        self.assertEqual(3, count)

    def test_analyze_for_one_word_pony2(self):
        dialog = "Applejack is the best pony ever! I've been friends with Applejack since grade three. I love applejack!"
        count = analyze_for_one_word_pony(dialog, "Applejack") 
        self.assertEqual(2, count)
    
    def test_analyze_for_two_word_pony_Pinkie_Pie(self):
        dialog = "Pinkie Pie loves to eat pie. Although she has gained some weight, Pinkie still eats and loves to be called Pie."
        count = analyze_for_two_word_pony(dialog, "Pinkie Pie") 
        self.assertEqual(3, count)

    def test_analyze_for_two_word_pony_Twilight_Sparkle(self):
        dialog = "Twilight Sparkle is a great pony. She goes out at twilight and likes to be called Twilight, not Sparkle."
        count = analyze_for_two_word_pony(dialog, "Twilight Sparkle") 
        self.assertEqual(3, count)

