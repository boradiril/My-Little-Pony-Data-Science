import unittest

from ..non_dictionary_words import *

class NonDictionaryWordsTestCase(unittest.TestCase):
    # test pony name in the beginning, middle and end of a sentence
    def test_find_non_words(self):
        dialog = "Aargh! AYE! We are, ehhem, <U+0098> pirates!"
        sample_word_set = {"we", "are", "pirates"}
        non_words_list = find_non_words(dialog, sample_word_set)
        self.assertEqual(set(non_words_list), set(["Aargh", "AYE", "ehhem"]))
    
    def test_find_non_words2(self):
        dialog = "Yo! Yo! Uhh! I love it when you call me Big Poppa!"
        sample_word_set = {"i", "love", "it", "when", "you", "call", "me", "big"}
        non_words_list = find_non_words(dialog, sample_word_set)
        self.assertEqual(set(non_words_list), set(["Yo", "Uhh", "Poppa"]))
    
    def test_find_top_non_words(self):
        all_non_words_list = ["aargh", "aargh", "aargh", "ugh", "ugh", "ugh", "yo", "yo", "yo", "shhh", "shhh", "shhh", "shhh", "weeee", "weeee", "weeee", "weeee", "aww", "aww", "wha" ]
        top_non_words_list = find_top_non_words(all_non_words_list)
        self.assertEqual(set(top_non_words_list), set(["aargh", "ugh", "yo", "shhh", "weeee"]))
    